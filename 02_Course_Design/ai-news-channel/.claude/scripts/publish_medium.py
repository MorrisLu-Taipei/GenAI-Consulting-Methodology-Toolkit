#!/usr/bin/env python3
"""
Medium Publisher — publishes article.md to Medium via API v1.

IMPORTANT: Medium stopped issuing new integration tokens (as of 2023).
If you have an existing token it still works. New users should use
Medium's Import Story feature or publish manually.
Docs: https://github.com/Medium/medium-api-docs

Usage:
  python3 publish_medium.py --date 2026-05-16 --dry-run
  python3 publish_medium.py --date 2026-05-16
"""

import argparse
import os
import json
import urllib.request
import urllib.error
import sys

MEDIUM_API_BASE = "https://api.medium.com/v1"


def get_user_id(token: str) -> str:
    req = urllib.request.Request(
        f"{MEDIUM_API_BASE}/me",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Accept-Charset": "utf-8"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            data = json.loads(res.read())
            return data["data"]["id"]
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        if e.code == 401:
            print("[ERROR] Medium token invalid or expired. Medium no longer issues new tokens.", file=sys.stderr)
            print("  Existing tokens still work — check yours at: https://medium.com/me/settings", file=sys.stderr)
        else:
            print(f"[ERROR] Medium API HTTP {e.code}: {body}", file=sys.stderr)
        sys.exit(1)


def publish_to_medium(article_path: str, dry_run: bool = True):
    token = os.environ.get("MEDIUM_TOKEN")
    if not token:
        print("[ERROR] MEDIUM_TOKEN not set.", file=sys.stderr)
        print("  Note: Medium no longer issues new integration tokens.", file=sys.stderr)
        print("  If you have an existing token, set: export MEDIUM_TOKEN=your_token", file=sys.stderr)
        sys.exit(1)

    with open(article_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract title from first # heading
    title = next(
        (line.lstrip("# ").strip() for line in content.split("\n") if line.startswith("# ")),
        "AI News Daily"
    )

    if dry_run:
        print("[DRY RUN] Would publish to Medium:")
        print(f"  Title:   {title}")
        print(f"  Length:  {len(content):,} chars")
        print(f"  Status:  draft (change to 'public' to publish directly)")
        return

    user_id = get_user_id(token)

    payload = json.dumps({
        "title": title,
        "contentFormat": "markdown",
        "content": content,
        "publishStatus": "draft",  # Change to "public" to publish immediately
        "license": "all-rights-reserved"
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{MEDIUM_API_BASE}/users/{user_id}/posts",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Accept-Charset": "utf-8"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            result = json.loads(res.read())
            url = result["data"]["url"]
            print(f"✅ Published to Medium (draft): {url}")
    except urllib.error.HTTPError as e:
        print(f"[ERROR] Medium publish HTTP {e.code}: {e.read().decode()}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    article_path = f"knowledge-base/deliverables/{args.date}/article.md"
    if not os.path.exists(article_path):
        print(f"[ERROR] Article not found: {article_path}")
        sys.exit(1)

    publish_to_medium(article_path, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
