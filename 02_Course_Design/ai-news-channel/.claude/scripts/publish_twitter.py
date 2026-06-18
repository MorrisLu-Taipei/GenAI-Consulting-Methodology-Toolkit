#!/usr/bin/env python3
"""
X (Twitter) Publisher — posts via X API v2 with OAuth 1.0a.

API: POST https://api.twitter.com/2/tweets  (X API v2, current as of 2026)
Auth: OAuth 1.0a User Context (required for writing/posting tweets)
Docs: https://developer.x.com/en/docs/x-api/tweets/manage-tweets/api-reference/post-tweets

Rate limits (Free tier): 17 posts per 24 hours per user
Rate limits (Basic tier $100/mo): 100 posts per 24 hours per user

Usage:
  python3 publish_twitter.py --date 2026-05-16 --dry-run
  python3 publish_twitter.py --date 2026-05-16 --article-url https://medium.com/...
"""

import argparse
import os
import json
import urllib.request
import urllib.error
import urllib.parse
import hmac
import hashlib
import base64
import time
import uuid
import sys


def extract_twitter_post(social_posts_path: str, article_url: str) -> str:
    with open(social_posts_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    in_twitter = False
    post_lines = []

    for line in lines:
        if any(k in line for k in ["Twitter", "twitter", "X)"]):
            in_twitter = True
            continue
        if in_twitter and line.startswith("##"):
            break
        if in_twitter:
            post_lines.append(line)

    post = "\n".join(post_lines).strip()
    post = post.replace("[LINK]", article_url)
    return post


def build_oauth_header(method: str, url: str, api_key: str, api_secret: str,
                        access_token: str, access_secret: str) -> str:
    """Build OAuth 1.0a Authorization header (current X API v2 auth method)."""
    oauth_params = {
        "oauth_consumer_key": api_key,
        "oauth_nonce": uuid.uuid4().hex,
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(int(time.time())),
        "oauth_token": access_token,
        "oauth_version": "1.0"
    }

    # Signature base string
    param_string = "&".join(
        f"{urllib.parse.quote(k, safe='')}={urllib.parse.quote(v, safe='')}"
        for k, v in sorted(oauth_params.items())
    )
    base_string = "&".join([
        method.upper(),
        urllib.parse.quote(url, safe=""),
        urllib.parse.quote(param_string, safe="")
    ])

    # HMAC-SHA1 signing key
    signing_key = f"{urllib.parse.quote(api_secret, safe='')}&{urllib.parse.quote(access_secret, safe='')}"
    signature = base64.b64encode(
        hmac.new(signing_key.encode(), base_string.encode(), hashlib.sha1).digest()
    ).decode()

    oauth_params["oauth_signature"] = signature

    return "OAuth " + ", ".join(
        f'{urllib.parse.quote(k, safe="")}="{urllib.parse.quote(v, safe="")}"'
        for k, v in sorted(oauth_params.items())
    )


def post_to_twitter(text: str, dry_run: bool = True):
    if dry_run:
        print("[DRY RUN] Would post to X (Twitter):")
        print(f"  Text ({len(text)} chars): {text[:100]}{'...' if len(text)>100 else ''}")
        return

    api_key     = os.environ["TWITTER_API_KEY"]
    api_secret  = os.environ["TWITTER_API_SECRET"]
    acc_token   = os.environ["TWITTER_ACCESS_TOKEN"]
    acc_secret  = os.environ["TWITTER_ACCESS_SECRET"]

    url = "https://api.twitter.com/2/tweets"
    payload = json.dumps({"text": text}).encode("utf-8")
    auth_header = build_oauth_header("POST", url, api_key, api_secret, acc_token, acc_secret)

    req = urllib.request.Request(
        url, data=payload,
        headers={
            "Authorization": auth_header,
            "Content-Type": "application/json"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            result = json.loads(res.read())
            tweet_id = result["data"]["id"]
            print(f"✅ Posted to X: https://x.com/i/web/status/{tweet_id}")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        print(f"[ERROR] X API HTTP {e.code}: {body}", file=sys.stderr)
        if e.code == 429:
            print("  Rate limit hit. Free tier: 17 posts/day. Basic tier: 100 posts/day.", file=sys.stderr)
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

    post = extract_twitter_post(posts_path, args.article_url)
    if not post:
        print("[ERROR] Could not extract Twitter post from social-posts.md")
        sys.exit(1)

    if len(post) > 280:
        print(f"[WARNING] Post is {len(post)} chars — truncating to 280")
        post = post[:277] + "..."

    post_to_twitter(post, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
