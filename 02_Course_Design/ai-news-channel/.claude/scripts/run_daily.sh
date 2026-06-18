#!/bin/bash
# run_daily.sh — Master daily orchestration script
# Usage:
#   bash run_daily.sh --dry-run --date 2024-01-15
#   bash run_daily.sh --publish --date 2024-01-15 --article-url https://medium.com/...

set -e

DATE=$(date +%Y-%m-%d)
DRY_RUN=true
PUBLISH=false
ARTICLE_URL="https://yourchannel.com"

while [[ $# -gt 0 ]]; do
  case $1 in
    --date) DATE="$2"; shift 2 ;;
    --dry-run) DRY_RUN=true; shift ;;
    --publish) DRY_RUN=false; PUBLISH=true; shift ;;
    --article-url) ARTICLE_URL="$2"; shift 2 ;;
    *) echo "Unknown: $1"; exit 1 ;;
  esac
done

echo "======================================"
echo "  AI News Channel — Daily Run"
echo "  Date: $DATE"
echo "  Mode: $([ "$DRY_RUN" = true ] && echo 'DRY RUN' || echo 'LIVE PUBLISH')"
echo "======================================"

# Step 1: Verify all deliverables exist and pass checks
echo ""
echo "Step 1/4: Running Supervisor verification..."
bash .claude/scripts/verify_build.sh --date "$DATE"
echo "✅ Verification passed"

# Step 2: Publish article to Medium
echo ""
echo "Step 2/4: Publishing article to Medium..."
if [ "$DRY_RUN" = true ]; then
  python3 .claude/scripts/publish_medium.py --date "$DATE" --dry-run
else
  python3 .claude/scripts/publish_medium.py --date "$DATE"
fi

# Step 3: Post to social platforms
echo ""
echo "Step 3/4: Posting to social platforms..."
if [ "$DRY_RUN" = true ]; then
  python3 .claude/scripts/publish_twitter.py --date "$DATE" --article-url "$ARTICLE_URL" --dry-run
  python3 .claude/scripts/publish_linkedin.py --date "$DATE" --article-url "$ARTICLE_URL" --dry-run
  python3 .claude/scripts/publish_threads.py --date "$DATE" --article-url "$ARTICLE_URL" --dry-run
else
  python3 .claude/scripts/publish_twitter.py --date "$DATE" --article-url "$ARTICLE_URL"
  python3 .claude/scripts/publish_linkedin.py --date "$DATE" --article-url "$ARTICLE_URL"
  python3 .claude/scripts/publish_threads.py --date "$DATE" --article-url "$ARTICLE_URL"
fi

# Step 4: Send newsletter
echo ""
echo "Step 4/4: Sending newsletter digest..."
if [ "$DRY_RUN" = true ]; then
  python3 .claude/scripts/send_newsletter.py --date "$DATE" --article-url "$ARTICLE_URL" --dry-run
else
  python3 .claude/scripts/send_newsletter.py --date "$DATE" --article-url "$ARTICLE_URL"
fi

echo ""
echo "======================================"
echo "  Daily run complete!"
echo "  $([ "$DRY_RUN" = true ] && echo 'DRY RUN — nothing was actually published.' || echo 'PUBLISHED successfully.')"
echo "======================================"
