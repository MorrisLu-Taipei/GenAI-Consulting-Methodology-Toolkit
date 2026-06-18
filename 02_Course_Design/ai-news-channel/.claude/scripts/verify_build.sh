#!/bin/bash
# verify_build.sh — Supervisor verification script
# Usage: bash verify_build.sh --date 2024-01-15

set -e

DATE=""
PASS=true
ISSUES=()

# Parse args
while [[ $# -gt 0 ]]; do
  case $1 in
    --date) DATE="$2"; shift 2 ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done

if [ -z "$DATE" ]; then
  echo "[ERROR] --date required (YYYY-MM-DD)"
  exit 1
fi

DELIVERABLES="knowledge-base/deliverables/$DATE"

echo "======================================"
echo "  Supervisor Verification — $DATE"
echo "======================================"

# Check 1: Deliverables directory exists
echo ""
echo "📁 Checking deliverables directory..."
if [ -d "$DELIVERABLES" ]; then
  echo "  ✅ Directory exists: $DELIVERABLES"
else
  echo "  ❌ MISSING: $DELIVERABLES"
  ISSUES+=("Deliverables directory not found: $DELIVERABLES")
  PASS=false
fi

# Check 2: Required files exist
echo ""
echo "📄 Checking required files..."

REQUIRED_FILES=(
  "article.md"
  "social-posts.md"
  "image-prompt.md"
  "newsletter.md"
)

for file in "${REQUIRED_FILES[@]}"; do
  filepath="$DELIVERABLES/$file"
  if [ -f "$filepath" ]; then
    SIZE=$(wc -c < "$filepath")
    echo "  ✅ $file ($SIZE bytes)"
  else
    echo "  ❌ MISSING: $file"
    ISSUES+=("Missing file: $file")
    PASS=false
  fi
done

# Check 3: Article word count
echo ""
echo "📝 Checking article word count..."
if [ -f "$DELIVERABLES/article.md" ]; then
  WORD_COUNT=$(wc -w < "$DELIVERABLES/article.md")
  if [ "$WORD_COUNT" -ge 800 ] && [ "$WORD_COUNT" -le 1200 ]; then
    echo "  ✅ Word count: $WORD_COUNT (target: 800-1200)"
  else
    echo "  ❌ Word count: $WORD_COUNT (out of range 800-1200)"
    ISSUES+=("Article word count $WORD_COUNT is outside 800-1200 range")
    PASS=false
  fi
fi

# Check 4: Source citations in article
echo ""
echo "🔗 Checking source citations..."
if [ -f "$DELIVERABLES/article.md" ]; then
  SOURCE_COUNT=$(grep -c "http" "$DELIVERABLES/article.md" 2>/dev/null || echo "0")
  if [ "$SOURCE_COUNT" -ge 3 ]; then
    echo "  ✅ Sources found: $SOURCE_COUNT URLs"
  else
    echo "  ❌ Only $SOURCE_COUNT source URLs found (minimum: 3)"
    ISSUES+=("Insufficient sources: found $SOURCE_COUNT, need 3+")
    PASS=false
  fi
fi

# Check 5: Twitter char count
echo ""
echo "🐦 Checking Twitter/X post length..."
if [ -f "$DELIVERABLES/social-posts.md" ]; then
  # Extract lines after Twitter section
  TWITTER_POST=$(awk '/Twitter|twitter|X\)/{found=1; next} found && /^##/{exit} found && /\S/{print}' "$DELIVERABLES/social-posts.md" | head -5 | tr -d '\n')
  CHAR_COUNT=${#TWITTER_POST}
  if [ "$CHAR_COUNT" -le 280 ] && [ "$CHAR_COUNT" -gt 0 ]; then
    echo "  ✅ Twitter post: $CHAR_COUNT chars"
  elif [ "$CHAR_COUNT" -eq 0 ]; then
    echo "  ⚠️  Could not parse Twitter post section"
    ISSUES+=("Could not parse Twitter post — verify social-posts.md format")
  else
    echo "  ❌ Twitter post: $CHAR_COUNT chars (max: 280)"
    ISSUES+=("Twitter post too long: $CHAR_COUNT chars")
    PASS=false
  fi
fi

# Check 6: Image prompt dimensions
echo ""
echo "🖼️  Checking image prompt specs..."
if [ -f "$DELIVERABLES/image-prompt.md" ]; then
  if grep -q "2500" "$DELIVERABLES/image-prompt.md" && grep -q "1686" "$DELIVERABLES/image-prompt.md"; then
    echo "  ✅ Article header dimensions (2500×1686) found in prompt"
  else
    echo "  ❌ Article header dimensions 2500×1686 not found in image-prompt.md"
    ISSUES+=("Image prompt missing 2500×1686 dimension spec")
    PASS=false
  fi

  if grep -q "1080" "$DELIVERABLES/image-prompt.md"; then
    echo "  ✅ Social card dimensions (1080×1080) found in prompt"
  else
    echo "  ❌ Social card dimensions 1080×1080 not found in image-prompt.md"
    ISSUES+=("Image prompt missing 1080×1080 social card spec")
    PASS=false
  fi
fi

# Check 7: Newsletter subject line
echo ""
echo "📧 Checking newsletter..."
if [ -f "$DELIVERABLES/newsletter.md" ]; then
  if grep -qi "subject" "$DELIVERABLES/newsletter.md"; then
    echo "  ✅ Subject line present"
  else
    echo "  ❌ No subject line found in newsletter.md"
    ISSUES+=("Newsletter missing subject line")
    PASS=false
  fi
fi

# Final verdict
echo ""
echo "======================================"
if [ "$PASS" = true ]; then
  echo "  ✅ VERIFICATION: PASS"
  echo "  Ready for PM approval and publish."
else
  echo "  ❌ VERIFICATION: FAIL"
  echo ""
  echo "  Issues found:"
  for issue in "${ISSUES[@]}"; do
    echo "    • $issue"
  done
  echo ""
  echo "  Return to Developer for revision."
  exit 1
fi
echo "======================================"
