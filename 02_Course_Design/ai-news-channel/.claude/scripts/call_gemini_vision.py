#!/usr/bin/env python3
"""
OpenAI Image Generation wrapper for Designer agent.
Model: gpt-image-2 (released April 21, 2026 — current flagship image model)

Replaces: Gemini Vision (retired from this role)
Reason: gpt-image-2 offers superior text rendering, 2K/4K resolution,
        multilingual support, and reasoning-based image planning.

API:  POST https://api.openai.com/v1/images/generations
Docs: https://platform.openai.com/docs/guides/image-generation

Pricing (per image, approx):
  low quality 1024x1024:  ~$0.006
  medium quality:         ~$0.053
  high quality:           ~$0.211

Usage:
  python3 call_gemini_vision.py --prompt "modern tech infographic" --output out/image-prompt.md
  python3 call_gemini_vision.py --test
  python3 call_gemini_vision.py --generate --prompt "..." --size 1024x1024 --output image.png
"""

import argparse
import os
import json
import urllib.request
import urllib.error
import base64
import sys
from datetime import datetime

IMAGE_MODEL = "gpt-image-2"
IMAGE_API_URL = "https://api.openai.com/v1/images/generations"
TEXT_MODEL = "gpt-5.5"
TEXT_API_URL = "https://api.openai.com/v1/chat/completions"


def refine_image_prompt(raw_prompt: str, api_key: str, spec: str = "2500x1686") -> str:
    """Use gpt-5.5 to refine a rough image prompt for gpt-image-2."""
    system = (
        f"You are a professional creative director. "
        f"Refine the following image prompt for gpt-image-2, which excels at layouts, "
        f"infographics, and text-in-image rendering. "
        f"Target spec: {spec}px. "
        f"Output only the refined prompt — no explanation, no preamble."
    )
    payload = json.dumps({
        "model": TEXT_MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": raw_prompt}
        ],
        "max_tokens": 512,
        "temperature": 0.6
    }).encode("utf-8")

    req = urllib.request.Request(
        TEXT_API_URL, data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as res:
            data = json.loads(res.read())
            return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"[WARNING] Prompt refinement failed: {e} — using raw prompt", file=sys.stderr)
        return raw_prompt


def generate_image(prompt: str, api_key: str,
                   size: str = "1024x1024", quality: str = "medium") -> bytes:
    """Generate an image with gpt-image-2, return PNG bytes."""
    payload = json.dumps({
        "model": IMAGE_MODEL,
        "prompt": prompt,
        "n": 1,
        "size": size,
        "quality": quality,
        "response_format": "b64_json"
    }).encode("utf-8")

    req = urllib.request.Request(
        IMAGE_API_URL, data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as res:
            data = json.loads(res.read())
            return base64.b64decode(data["data"][0]["b64_json"])
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        print(f"[ERROR] gpt-image-2 API HTTP {e.code}: {body}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="gpt-image-2 wrapper (replaces Gemini Vision)")
    parser.add_argument("--prompt", help="Image description or rough prompt")
    parser.add_argument("--output", help="Output path (.md for refined prompt, .png to generate)")
    parser.add_argument("--size", default="1024x1024",
                        help="Image size: 1024x1024, 1536x1024, 1024x1536, 2048x2048")
    parser.add_argument("--quality", default="medium",
                        help="Quality: low | medium | high")
    parser.add_argument("--spec", default="2500x1686",
                        help="Target spec hint for prompt refinement (default: 2500x1686)")
    parser.add_argument("--generate", action="store_true",
                        help="Actually generate the image (saves PNG). Without this, saves refined prompt.")
    parser.add_argument("--test", action="store_true", help="Connection test")
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("[ERROR] OPENAI_API_KEY not set.", file=sys.stderr)
        sys.exit(1)

    if args.test:
        print(f"Testing gpt-image-2 API connection...")
        # Text-only test (cheaper)
        payload = json.dumps({
            "model": TEXT_MODEL,
            "messages": [{"role": "user", "content": "Reply: 'Image API ready'"}],
            "max_tokens": 10
        }).encode()
        req = urllib.request.Request(TEXT_API_URL, data=payload,
                                     headers={"Authorization": f"Bearer {api_key}",
                                              "Content-Type": "application/json"})
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read())
            print(f"✅ {data['choices'][0]['message']['content'].strip()}")
            print(f"   Model: {IMAGE_MODEL} (image generation)")
            print(f"   Text refiner: {TEXT_MODEL}")
        return

    if not args.prompt:
        print("[ERROR] --prompt required (or --test)", file=sys.stderr)
        sys.exit(1)

    if args.generate:
        # Refine prompt then generate actual image
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Refining prompt with {TEXT_MODEL}...")
        refined = refine_image_prompt(args.prompt, api_key, spec=args.spec)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Generating image with {IMAGE_MODEL}...")
        print(f"  Size: {args.size} | Quality: {args.quality}")
        image_bytes = generate_image(refined, api_key, size=args.size, quality=args.quality)

        output_path = args.output or f"image-{datetime.now().strftime('%Y%m%d-%H%M%S')}.png"
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(image_bytes)
        print(f"✅ Image saved to {output_path} ({len(image_bytes):,} bytes)")

    else:
        # Default: refine prompt and save as markdown (no image generation cost)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Refining image prompt with {TEXT_MODEL}...")
        refined = refine_image_prompt(args.prompt, api_key, spec=args.spec)

        output = args.output
        if output:
            os.makedirs(os.path.dirname(output) if os.path.dirname(output) else ".", exist_ok=True)
            with open(output, "w", encoding="utf-8") as f:
                f.write(f"## Refined Image Prompt\n\n**Model:** {IMAGE_MODEL}\n**Spec:** {args.spec}px\n\n{refined}\n\n")
                f.write(f"---\n\n*To generate: `python3 call_gemini_vision.py --prompt \"...\" --generate --size 1024x1024 --output image.png`*\n")
            print(f"✅ Refined prompt saved to {output}")
        else:
            print(refined)


if __name__ == "__main__":
    main()
