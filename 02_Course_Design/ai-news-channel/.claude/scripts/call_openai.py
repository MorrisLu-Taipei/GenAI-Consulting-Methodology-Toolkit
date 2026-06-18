#!/usr/bin/env python3
"""
OpenAI API wrapper for AI News Channel agents.
Model: gpt-5.5 (released April 24, 2026 — current flagship)

API: POST https://api.openai.com/v1/chat/completions
Docs: https://platform.openai.com/docs/models

Model options (May 2026):
  gpt-5.5          — flagship, strongest reasoning, 1M+ context ($5/$30 per 1M tokens)
  gpt-5.5-pro      — extended thinking, highest capability
  gpt-4.1          — cost-efficient alternative ($2/$8 per 1M tokens)
  gpt-4.1-mini     — fast and cheap for simple tasks

Usage:
  python3 call_openai.py --prompt "your prompt" --output path/to/output.md
  python3 call_openai.py --test
  python3 call_openai.py --prompt "..." --model gpt-4.1-mini  # cheaper option
"""

import argparse
import os
import json
import urllib.request
import urllib.error
import sys
from datetime import datetime

DEFAULT_MODEL = "gpt-5.5"
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"


def call_openai(prompt: str, api_key: str, model: str = DEFAULT_MODEL) -> str:
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 4096
    }).encode("utf-8")

    req = urllib.request.Request(
        OPENAI_API_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=90) as res:
            data = json.loads(res.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        print(f"[ERROR] OpenAI API HTTP {e.code}: {body}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="OpenAI API wrapper")
    parser.add_argument("--prompt", help="Prompt to send")
    parser.add_argument("--output", help="Output file path (.md)")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"OpenAI model (default: {DEFAULT_MODEL})")
    parser.add_argument("--test", action="store_true", help="Run a connection test")
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("[ERROR] OPENAI_API_KEY not set.", file=sys.stderr)
        print("  export OPENAI_API_KEY=your_key_here", file=sys.stderr)
        sys.exit(1)

    if args.test:
        print(f"Testing OpenAI API (model: {args.model})...")
        result = call_openai(
            "Reply with exactly: 'OpenAI API connection successful'",
            api_key, model=args.model
        )
        print(f"✅ {result.strip()}")
        return

    if not args.prompt:
        print("[ERROR] --prompt required (or --test)", file=sys.stderr)
        sys.exit(1)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Calling {args.model}...")
    result = call_openai(args.prompt, api_key, model=args.model)

    if args.output:
        os.makedirs(os.path.dirname(args.output) if os.path.dirname(args.output) else ".", exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"✅ Saved to {args.output} ({len(result):,} chars)")
    else:
        print(result)


if __name__ == "__main__":
    main()
