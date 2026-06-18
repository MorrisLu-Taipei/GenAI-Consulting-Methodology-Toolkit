# Skill Stack & Tech Stack

## AI Models in Use

| Role | Model | API |
|---|---|---|
| CTO / Supervisor / Developer | Claude Sonnet / Opus | Anthropic API |
| Researcher | Gemini 3 Flash Preview | Google AI API |
| Designer | Gemini 3 Flash Preview Vision | Google AI API |
| Librarian | Scripts (no LLM required) | — |

---

## Publishing APIs (configure in .env)

| Platform | API / Method |
|---|---|
| Medium | Medium API v1 |
| Substack | RSS / webhook |
| Twitter/X | Twitter API v2 |
| LinkedIn | LinkedIn API v2 |
| Threads | Meta Threads API |
| Email | SendGrid / Mailchimp API |

---

## Scripts in Use

| Script | Purpose |
|---|---|
| `call_gemini.py` | Gemini Pro text API wrapper |
| `call_gemini_vision.py` | gpt-image-2 image analysis |
| `publish_medium.py` | Auto-publish to Medium |
| `publish_twitter.py` | Auto-post to Twitter/X |
| `publish_linkedin.py` | Auto-post to LinkedIn |
| `send_newsletter.py` | Send email digest |
| `verify_build.sh` | Supervisor verification checks |
| `run_daily.sh` | Master orchestration script |

---

## Environment Variables Required

```bash
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
MEDIUM_TOKEN=
TWITTER_BEARER_TOKEN=
TWITTER_API_KEY=
TWITTER_API_SECRET=
TWITTER_ACCESS_TOKEN=
TWITTER_ACCESS_SECRET=
LINKEDIN_ACCESS_TOKEN=
THREADS_ACCESS_TOKEN=
SENDGRID_API_KEY=
NEWSLETTER_FROM_EMAIL=
NEWSLETTER_LIST_ID=
```
