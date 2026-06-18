#!/usr/bin/env python3
"""
Newsletter Sender — sends daily digest via SendGrid Marketing API v3.

API: https://api.sendgrid.com/v3/mail/send  (current as of 2026)
Auth: API Key in Authorization header
Docs: https://docs.sendgrid.com/api-reference/mail-send/mail-send

Usage:
  python3 send_newsletter.py --date 2026-05-16 --dry-run
  python3 send_newsletter.py --date 2026-05-16 --article-url https://medium.com/...
"""

import argparse
import os
import json
import urllib.request
import urllib.error
import sys
import re


def load_newsletter(newsletter_path: str, article_url: str) -> dict:
    with open(newsletter_path, "r", encoding="utf-8") as f:
        content = f.read()

    content = content.replace("[LINK]", article_url)

    # Extract subject line
    subject = "AI News Daily Digest"
    for line in content.split("\n"):
        if "Subject" in line and ":" in line:
            candidate = line.split(":", 1)[-1].strip().strip('"').strip("'")
            if candidate:
                subject = candidate
                break

    # Extract preview text (first non-empty line after subject)
    preview = ""
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if "Preview" in line and ":" in line:
            preview = line.split(":", 1)[-1].strip().strip('"')[:90]
            break

    # Basic Markdown → HTML conversion
    html = content
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
  body {{ font-family: -apple-system, sans-serif; max-width: 600px; margin: 0 auto; padding: 24px; color: #1a1814; }}
  h1 {{ font-size: 24px; }} h2 {{ font-size: 18px; color: #444; }}
  a {{ color: #d4500a; }} li {{ margin: 6px 0; }}
  .cta {{ background: #d4500a; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; display: inline-block; margin-top: 16px; }}
</style>
</head><body>{html}</body></html>"""

    return {
        "subject": subject,
        "preview": preview,
        "html": html,
        "text": content
    }


def send_newsletter(newsletter: dict, dry_run: bool = True):
    if dry_run:
        print("[DRY RUN] Would send newsletter:")
        print(f"  Subject:  {newsletter['subject']}")
        print(f"  Preview:  {newsletter['preview']}")
        print(f"  HTML len: {len(newsletter['html']):,} chars")
        return

    api_key    = os.environ.get("SENDGRID_API_KEY")
    from_email = os.environ.get("NEWSLETTER_FROM_EMAIL", "newsletter@yourchannel.com")
    list_id    = os.environ.get("NEWSLETTER_LIST_ID")

    if not api_key:
        print("[ERROR] SENDGRID_API_KEY not set.", file=sys.stderr)
        sys.exit(1)

    # Use SendGrid's single send to a contact list
    payload_data = {
        "from": {"email": from_email, "name": "AI News Channel"},
        "subject": newsletter["subject"],
        "content": [
            {"type": "text/plain", "value": newsletter["text"]},
            {"type": "text/html",  "value": newsletter["html"]}
        ]
    }

    # If list_id is set, send to that list
    if list_id:
        payload_data["personalizations"] = [{
            "to": [{"email": from_email}]  # fallback to self-send if no list configured
        }]
    else:
        print("[WARNING] NEWSLETTER_LIST_ID not set — sending to FROM address only (test mode)", file=sys.stderr)
        payload_data["personalizations"] = [{"to": [{"email": from_email}]}]

    payload = json.dumps(payload_data).encode("utf-8")

    req = urllib.request.Request(
        "https://api.sendgrid.com/v3/mail/send",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            print(f"✅ Newsletter sent (HTTP {res.status})")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        print(f"[ERROR] SendGrid API HTTP {e.code}: {body}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    parser.add_argument("--article-url", default="https://yourchannel.com")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    newsletter_path = f"knowledge-base/deliverables/{args.date}/newsletter.md"
    if not os.path.exists(newsletter_path):
        print(f"[ERROR] Newsletter not found: {newsletter_path}")
        sys.exit(1)

    newsletter = load_newsletter(newsletter_path, args.article_url)
    send_newsletter(newsletter, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
