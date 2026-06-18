#!/usr/bin/env python3
"""
Gemini API wrapper for AI News Channel agents.
Model: gemini-3-flash-preview (current Gemini 3 series Flash model)

NOTE: gemini-2.5-flash is superseded by gemini-3-flash-preview.
      Gemini 3 Flash uses thinking_level instead of thinking_budget.
      Still in preview (production use supported with billing enabled).
      Docs: https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview

Pricing: $0.50/1M input tokens, $3.00/1M output tokens
Context: 1M token window

Model options (May 2026):
  gemini-3-flash-preview  — Pro-level reasoning at Flash speed (default)
  gemini-3.1-flash-lite   — Ultra-low cost, high-volume tasks ($0.25/$1.50)
  gemini-3.1-pro-preview  — Highest capability, complex reasoning

Usage:
  python3 call_gemini.py --prompt "your prompt" --output path/to/output.md
  python3 call_gemini.py --test
  python3 call_gemini.py --prompt "..." --model gemini-3.1-flash-lite --thinking low
"""

import argparse
import os
import json
import urllib.request
import urllib.error
import sys
from datetime import datetime

DEFAULT_MODEL = "gemini-3-flash-preview"
GEMINI_API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"


def call_gemini(prompt: str, api_key: str, model: str = DEFAULT_MODEL,
                thinking_level: str = "medium") -> str:
    """
    Call Gemini API. Gemini 3 models use thinking_level (minimal/low/medium/high)
    instead of the old thinking_budget parameter.
    """
    generation_config = {
        "temperature": 0.7,
        "maxOutputTokens": 8192
    }

    # Gemini 3 series: use thinking_level parameter
    if model.startswith("gemini-3"):
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": generation_config,
            "thinkingConfig": {
                "thinkingLevel": thinking_level  # minimal | low | medium | high
            }
        }
    else:
        # Gemini 2.x fallback (no thinking config needed)
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": generation_config
        }

    data = json.dumps(payload).encode("utf-8")
    url = f"{GEMINI_API_BASE}/{model}:generateContent?key={api_key}"
    req = urllib.request.Request(
        url, data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as res:
            data = json.loads(res.read().decode("utf-8"))
            candidates = data.get("candidates", [])
            if not candidates:
                print(f"[ERROR] No candidates in response: {data}", file=sys.stderr)
                sys.exit(1)
            parts = candidates[0].get("content", {}).get("parts", [])
            # Filter to text parts only — Gemini 3 may include thoughtSignature parts
            return "\n".join(p["text"] for p in parts if "text" in p)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        print(f"[ERROR] Gemini API HTTP {e.code}: {body}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Gemini API wrapper")
    parser.add_argument("--prompt", help="Prompt to send to Gemini")
    parser.add_argument("--output", help="Output file path (.md)")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Gemini model (default: {DEFAULT_MODEL})")
    parser.add_argument("--thinking", default="medium",
                        choices=["minimal", "low", "medium", "high"],
                        help="Thinking level for Gemini 3 models (default: medium)")
    parser.add_argument("--test", action="store_true", help="Run a connection test")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[ERROR] GEMINI_API_KEY not set.", file=sys.stderr)
        print("  export GEMINI_API_KEY=your_key_here", file=sys.stderr)
        sys.exit(1)

    if args.test:
        print(f"Testing Gemini API (model: {args.model}, thinking: {args.thinking})...")
        result = call_gemini(
            "Reply with exactly: 'Gemini API connection successful'",
            api_key, model=args.model, thinking_level=args.thinking
        )
        print(f"✅ {result.strip()}")
        return

    if not args.prompt:
        print("[ERROR] --prompt required (or --test)", file=sys.stderr)
        sys.exit(1)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Calling {args.model} (thinking: {args.thinking})...")
    result = call_gemini(args.prompt, api_key, model=args.model, thinking_level=args.thinking)

    if args.output:
        os.makedirs(os.path.dirname(args.output) if os.path.dirname(args.output) else ".", exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"✅ Saved to {args.output} ({len(result):,} chars)")
    else:
        print(result)


if __name__ == "__main__":
    main()
