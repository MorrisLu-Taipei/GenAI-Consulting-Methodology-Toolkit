#!/usr/bin/env python3
"""
Threads Publisher — posts via Meta Threads API v1.

API:  https://graph.threads.net/v1.0  (current as of 2026)
Auth: Meta OAuth 2.0 (threads_basic + threads_content_publish scopes)
Docs: https://developers.facebook.com/docs/threads

Flow (2 steps):
  Step 1 — Create media container (POST /{user_id}/threads)
  Step 2 — Publish container   (POST /{user_id}/threads_publish)

Token setup:
  1. Create app at https://developers.facebook.com
  2. Add "Threads API" product
  3. Complete OAuth flow for threads_content_publish scope
  4. Set THREADS_ACCESS_TOKEN and THREADS_USER_ID env vars

Note: Threads tokens can last up to 60 days. Use long-lived token exchange.

Usage:
  python3 publish_threads.py --date 2026-05-16 --dry-run
  python3 publish_threads.py --date 2026-05-16 --article-url https://medium.com/...
"""

import argparse
import os
import json
import urllib.request
import urllib.error
import urllib.parse
import sys

THREADS_API_BASE = "https://graph.threads.net/v1.0"


def extract_threads_post(social_posts_path: str, article_url: str) -> str:
    with open(social_posts_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    in_threads = False
    post_lines = []

    for line in lines:
        if "Threads" in line or "threads" in line:
            in_threads = True
            continue
        if in_threads and line.startswith("##"):
            break
        if in_threads:
            post_lines.append(line)

    post = "\n".join(post_lines).strip()
    post = post.replace("[LINK]", article_url)
    return post


def post_to_threads(text: str, dry_run: bool = True):
    if dry_run:
        print("[DRY RUN] Would post to Threads:")
        print(f"  Text ({len(text)} chars): {text[:120]}{'...' if len(text)>120 else ''}")
        return

    access_token = os.environ.get("THREADS_ACCESS_TOKEN")
    user_id      = os.environ.get("THREADS_USER_ID")

    if not access_token or not user_id:
        print("[ERROR] THREADS_ACCESS_TOKEN and THREADS_USER_ID must be set.", file=sys.stderr)
        sys.exit(1)

    def api_post(endpoint: str, params: dict) -> dict:
        qs = urllib.parse.urlencode({**params, "access_token": access_token})
        req = urllib.request.Request(
            f"{THREADS_API_BASE}/{endpoint}?{qs}",
            method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as res:
                return json.loads(res.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8")
            print(f"[ERROR] Threads API HTTP {e.code}: {body}", file=sys.stderr)
            if e.code == 401:
                print("  Token expired? Use long-lived token. Docs: https://developers.facebook.com/docs/threads/get-started", file=sys.stderr)
            sys.exit(1)

    # Step 1: Create container
    container = api_post(f"{user_id}/threads", {
        "media_type": "TEXT",
        "text": text
    })
    container_id = container.get("id")
    if not container_id:
        print(f"[ERROR] Failed to create Threads container: {container}", file=sys.stderr)
        sys.exit(1)

    # Step 2: Publish container
    result = api_post(f"{user_id}/threads_publish", {
        "creation_id": container_id
    })
    post_id = result.get("id", "unknown")
    print(f"✅ Posted to Threads: {post_id}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    parser.add_argument("--article-url", default="https://yourchannel.com")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    posts_path = f"knowledge-base/deliverables/{args.date}/social-posts.md"
    if not os.path.exists(posts_path):
        print(f"[ERROR] social-posts.md not found: {posts_path}")
        sys.exit(1)

    post = extract_threads_post(posts_path, args.article_url)
    if not post:
        print("[ERROR] Could not extract Threads post from social-posts.md")
        sys.exit(1)

    if len(post) > 500:
        print(f"[WARNING] Post is {len(post)} chars — truncating to 500")
        post = post[:497] + "..."

    post_to_threads(post, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
