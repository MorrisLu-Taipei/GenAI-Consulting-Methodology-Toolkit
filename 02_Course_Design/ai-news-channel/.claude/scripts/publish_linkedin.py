#!/usr/bin/env python3
"""
LinkedIn Publisher — posts via LinkedIn UGC Posts API v2.

API: POST https://api.linkedin.com/v2/ugcPosts  (current as of 2026)
Auth: OAuth 2.0 Bearer token (3-legged, w_member_social scope required)
Docs: https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/ugc-post-api

Token setup:
  1. Create app at https://www.linkedin.com/developers
  2. Request r_liteprofile + w_member_social scopes
  3. Complete OAuth 2.0 3-legged flow to get access token
  4. Set LINKEDIN_ACCESS_TOKEN and LINKEDIN_PERSON_ID env vars

Note: LinkedIn access tokens expire in ~60 days. Refresh via OAuth refresh flow.

Usage:
  python3 publish_linkedin.py --date 2026-05-16 --dry-run
  python3 publish_linkedin.py --date 2026-05-16 --article-url https://medium.com/...
"""

import argparse
import os
import json
import urllib.request
import urllib.error
import sys


def extract_linkedin_post(social_posts_path: str, article_url: str) -> str:
    with open(social_posts_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    in_linkedin = False
    post_lines = []

    for line in lines:
        if "LinkedIn" in line or "linkedin" in line:
            in_linkedin = True
            continue
        if in_linkedin and line.startswith("##"):
            break
        if in_linkedin:
            post_lines.append(line)

    post = "\n".join(post_lines).strip()
    post = post.replace("[LINK]", article_url)
    return post


def post_to_linkedin(text: str, dry_run: bool = True):
    if dry_run:
        print("[DRY RUN] Would post to LinkedIn:")
        print(f"  Text ({len(text)} chars): {text[:120]}{'...' if len(text)>120 else ''}")
        return

    access_token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
    person_id    = os.environ.get("LINKEDIN_PERSON_ID")

    if not access_token or not person_id:
        print("[ERROR] LINKEDIN_ACCESS_TOKEN and LINKEDIN_PERSON_ID must be set.", file=sys.stderr)
        sys.exit(1)

    payload = json.dumps({
        "author": f"urn:li:person:{person_id}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.linkedin.com/v2/ugcPosts",
        data=payload,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0",
            "LinkedIn-Version": "202401"  # Pin to stable version
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            result = json.loads(res.read()) if res.read() else {}
            post_id = result.get("id", "unknown")
            print(f"✅ Posted to LinkedIn: {post_id}")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        print(f"[ERROR] LinkedIn API HTTP {e.code}: {body}", file=sys.stderr)
        if e.code == 401:
            print("  Token expired? LinkedIn tokens last ~60 days. Refresh via OAuth.", file=sys.stderr)
        sys.exit(1)


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

    post = extract_linkedin_post(posts_path, args.article_url)
    if not post:
        print("[ERROR] Could not extract LinkedIn post from social-posts.md")
        sys.exit(1)

    if len(post) > 3000:  # LinkedIn actual max is 3000 chars for UGC posts
        print(f"[WARNING] Post is {len(post)} chars — truncating to 3000")
        post = post[:2997] + "..."

    post_to_linkedin(post, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
