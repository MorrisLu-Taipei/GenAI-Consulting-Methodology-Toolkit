> 🌐 中文版本 / Chinese version: [L1_OPENWEBUI_COURSE_PLAN.md](L1_OPENWEBUI_COURSE_PLAN.md)

# L1 OpenWebUI Enterprise Enablement Course Plan

Version: v1.0
Author: Morris Lu (盧業興) · Tiger AI 虎智科技
Applicable Level: L1 Controlled AI Access
Reference Video Playlist: DigitalBrainBase OpenWebUI playlist
`https://www.youtube.com/watch?v=oXJ4L1G8kaI&list=PL_rTgQnnMXsXAsEiid-tWhaj03SsP4U5Z`

---

## 1. Repositioning L1

L1 is not merely about teaching employees "how to chat with AI." What enterprises actually need is a governed AI entry point:

> Every employee can sign in to OpenWebUI with their own account and have a personal chat area, conversation history, and individual settings; administrators can manage accounts, roles, groups, models, permissions, features, and data-use boundaries.

Therefore, the L1 course must serve two audiences simultaneously:

| Audience | What They Need to Learn |
|---|---|
| General users | Sign in, choose a model, start a new chat, manage their own conversations, upload permitted data, and use prompts to complete work |
| Admin / IT / HR | Create or review accounts, configure roles, groups, default permissions, model visibility, file upload, Web Search, API Keys, sharing, and data policies |

The completion criterion for L1 is not "everyone can ask questions," but rather "the company can let employees begin using AI in a safe, manageable, and scalable manner."

---

## 2. Essential Enterprise Capabilities

| Capability | Enterprise Requirement | Acceptance Method |
|---|---|---|
| Account sign-in | Each employee signs in with their own account; no shared accounts | Test account list, sign-in screenshots |
| Personal chat area | Each user has their own chat history, folders, personal prompts, and settings | Individual user operation demos |
| Role management | At minimum Admin, User, Pending; new accounts require review or controlled activation | Admin Panel configuration screenshots |
| Group management | Create groups by department or seed team | Groups configuration sheet |
| Permission control | Govern file upload, Web Search, Image, Tools, API Keys, sharing, deletion, and export | Permissions checklist |
| Model control | Different groups can access different models or model presets | Model access sheet |
| Data boundaries | Define which data may be input, must not be input, or requires human confirmation | AI usage policy |
| Usage records and governance | Administrators know how to audit settings, publish policies, and resolve account or permission issues | L1 Admin Runbook |

Note: According to the official OpenWebUI documentation, its RBAC is composed of three layers — Roles, Permissions, and Groups — and permissions follow an additive model. Enterprises should therefore adopt the principle of least privilege, first tightening Global Defaults and then opening advanced features through Groups.

Official documentation references:

- Roles: `https://docs.openwebui.com/features/rbac/roles/`
- Permissions: `https://docs.openwebui.com/features/rbac/permissions/`
- Groups: `https://docs.openwebui.com/features/rbac/groups/`

---

## 3. Course Objectives

After completing the L1 course, the client should be able to:

1. Explain OpenWebUI's role at L1 of the enterprise AI maturity model.
2. Complete OpenWebUI sign-in and basic chat operations.
3. Build a personal chat area: new chats, history, folders, prompts, and files.
4. Use prompts to complete high-frequency work such as emails, meeting minutes, summaries, and report drafts.
5. Use file upload or Knowledge to perform Q&A on low-sensitivity documents.
6. Understand model selection, parameters, hallucinations, and human confirmation.
7. Enable Admins to manage accounts, roles, groups, permissions, models, and features.
8. Enable IT / HR to establish AI usage policies, data classification, and the Gate 1 acceptance checklist.
9. Produce an L2 Skill candidate list.

---

## 4. Prerequisites

| Item | Minimum Requirement |
|---|---|
| OpenWebUI environment | An existing test environment or a classroom demo environment |
| Accounts | Each student has their own test account; the Admin has a management account |
| Models | At least one usable model; either local Ollama or an API model |
| Test data | Low-sensitivity documents, meeting minutes, emails, FAQs, SOPs |
| Permission draft | Decisions on whether to allow file upload, Web Search, sharing, API Keys, and tool use |
| Company policy | If no AI policy exists, the first version is created in class |

---

## 5. L1 OpenWebUI IPOE

| Category | Definition |
|---|---|
| Input | User accounts, low-sensitivity departmental data, prompts, documents, models, groups, permission settings, AI usage policy |
| Process | Sign-in, starting new chats, model selection, prompt practice, document Q&A, chat organization, Admin account review, role/group/permission settings, data case judgement |
| Output | Personal chat records, Prompt Library, low-sensitivity document summaries, AI usage policy, account/group/permission tables, high-frequency work list, L2 Skill candidates |
| Evidence | Sign-in screenshots, personal chat screenshots, Admin Panel screenshots, Groups/Permissions settings, prompt exercises, data case judgement table, Gate 1 acceptance record |

---

## 6. Full Course Versions

### 6.1 L1 All-Hands User Course: 3 Hours

| Time | Topic | Content | Output |
|---|---|---|---|
| 20 min | L1 positioning | Why the enterprise needs a unified AI entry point | L1 consensus |
| 30 min | Sign-in and personal chat area | Sign in with your own account, new chat, history, folders, personal settings | Sign-in and chat screenshots |
| 30 min | Model and chat operations | Choose a model, regenerate answers, continue writing, export, organize chats | Hands-on practice |
| 45 min | Prompt fundamentals | Role, task, context, constraints, output format | Personal prompts |
| 45 min | Daily work practice | Email, summary, meeting minutes, manager's report | Classroom output |
| 30 min | Data boundaries | What may be input, what may not, what requires human confirmation | Data case judgement |

### 6.2 L1 Admin / IT Management Course: 3 Hours

| Time | Topic | Content | Output |
|---|---|---|---|
| 30 min | Admin Panel overview | Users, models, connections, features, documents, announcements | Admin operation checklist |
| 45 min | Account and sign-in management | Admin / User / Pending, review process, default role | Account management sheet |
| 45 min | Groups and permissions | Default Permissions, Groups, departmental permissions, least privilege | Permission matrix |
| 45 min | Model and feature governance | Model visibility, Web Search, File Upload, API Keys, Tools | Model/feature sheet |
| 30 min | Personal area and sharing policy | Personal chats, chat sharing, public resources, export policy | Sharing policy |
| 45 min | Gate 1 acceptance | Environment, accounts, permissions, data policy, Prompt Library | Gate 1 sheet |

### 6.3 L1 Enterprise Adoption Workshop: 1 Day

| Time | Topic | Content | Output |
|---|---|---|---|
| AM 1 | User training | Sign-in, chat, model, prompt, documents | Personal exercises |
| AM 2 | Departmental scenarios | Email, meetings, summaries, reports, FAQ | Departmental prompts |
| PM 1 | Admin configuration | Accounts, roles, groups, permissions, models | Admin Runbook |
| PM 2 | Governance and bridge to L2 | Data policy, high-frequency work, Skill candidates | L2 candidate list |

---

## 7. Admin Control Sheet

| Control | Recommended Setting | Evidence |
|---|---|---|
| First Admin | Assign IT or the AI management focal point | Admin roster |
| User activation | New users default to Pending or controlled User | Default role setting |
| Personal accounts | Prohibit shared accounts; each person signs in individually | Account list |
| Personal chat area | Each user creates their own chats and folders | User screenshots |
| Groups | Build groups by department, seed team, and Power Users | Groups sheet |
| Default Permissions | Adopt least privilege; advanced features opened through Groups | Permission screenshots |
| File Upload | Allow low-sensitivity data first; high-sensitivity data prohibited | Data classification policy |
| Web Search | Open per departmental need; require source citation | Permission sheet |
| API Keys | Disabled by default or granted only to IT / Power Users | API Key policy |
| Share / Public | Public sharing restricted by default | Sharing policy |
| Models | Open local or API models per group | Model access sheet |
| Announcements | Place AI usage policy and data reminders | Banner screenshots |

---

## 8. User Operation Standards

By the end of L1, every student must be able to:

1. Sign in with their own account.
2. Create at least 2 chat topics.
3. Organize chats into folders with clear naming.
4. Build 3 personal go-to prompts.
5. Complete summaries or Q&A on a low-sensitivity document.
6. Judge whether 10 data cases may be input into AI.
7. Know which scenarios require human confirmation rather than accepting the AI answer directly.

---

## 9. Reference Video Map

| # | Video Title | Course Use | Recommendation |
|---:|---|---|---|
| 1 | Open WebUI: The Free, Private ChatGPT Alternative | L1 opener and value positioning | Required |
| 2 | How to Install OpenWebUI | IT installation and environment preparation | Required for IT |
| 3 | Local AI Model Requirements | Hardware requirements for local models | Required for IT |
| 4 | Exploring the OpenWebUI Admin Panel | Admin Panel, enterprise management | Required for Admins |
| 5 | Exploring Open WebUI: Features, Models, & Tools | Feature overview, concepts of models and tools | Required |
| 6 | Chat with Your Own Documents | File upload and document Q&A | Required |
| 7 | Add Real-Time Web Search | Web Search configuration and use | Elective / permission discussion |
| 8 | Add GPT-4 to Open WebUI | OpenAI API provider configuration | IT / Admin |
| 9 | Community Tools | Community tool adoption | Elective, requires security review |
| 10 | Text-to-Speech with ElevenLabs | TTS | Elective |
| 11 | Create Custom AI Models | Model presets, persona models | Admin / pre-L2 |
| 12 | Generate AI Images with DALL-E 3 | Image generation | Elective |
| 13 | LLAVA Multimodal / GPT-4 Image Analysis | Multimodal image analysis | Elective |
| 14 | AI Clone | Personalization demo | Inspiration, not core |
| 15 | Functions to Build Websites & Apps | Functions in action | L2 / L3 preview |
| 16 | Reduce Hallucinations with Advanced Parameters | Hallucinations, parameters, human confirmation | Required |
| 17 | Choosing the Right Ollama Model | Local model selection | IT / Admin |
| 18 | Mobile Access with Ngrok | Mobile access, remote risks | Elective, requires security review |
| 19 | Choosing the Best Language Model | Model selection methodology | Admin / seed users |
| 20 | Vision LLMs for Local Inference | Vision model evaluation | Elective |
| 21 | AI Recruiter Meets AI Clone | Recruiting demo | HR inspiration |
| 22 | Groq Cloud & OpenWebUI | Cloud model provider | IT / Admin |
| 23 | Docker & Watchtower | Operations and updates | Required for IT |
| 24 | OpenWebUI Pipelines | Pipelines | L3 preview |
| 25 | User Roles in Open Web UI | User roles and secure collaboration | Required for Admins |
| 26 | Writing Better Prompts | Prompt fundamentals | Required for everyone |
| 27 | Arena Model | Model testing and comparison | Admin / evaluation |
| 28 | Run Text-to-Speech Locally | Local TTS | Elective |
| 29 | OpenWebUI Memory Explained | Memory / personalized memory | Elective, requires privacy discussion |
| 30 | Quantization | Quantization and performance | Elective for IT |
| 31 | AI-Powered Recruiter Bot | Recruiting Bot | HR / L2 case |
| 32 | Open WebUI v0.4 Updates | Version update concepts | IT / Admin |
| 33 | Anthropic Claude Models | Claude provider configuration | IT / Admin |
| 34 | Public Access to Chatbots | Publicly shared Chatbot | Elective, requires strict enterprise control |
| 35 | Tools, Functions & Pipelines Deep Dive | Advanced extensibility | L2 / L3 preview |
| 36 | Online? Offline? Both? | Cloud / local / Hybrid discussion | Required |

---

## 10. L1 Deliverables

| Deliverable | Description | Acceptance Method |
|---|---|---|
| OpenWebUI user operation manual | Sign-in, chat, model, documents, prompts, data boundaries | Users can follow the manual to operate |
| Admin Runbook | Accounts, roles, groups, permissions, models, feature toggles | Admins can operate independently |
| Account / group / permission table | Personal accounts, departmental groups, feature permissions | IT / HR sign-off |
| AI usage policy | What may be input, what may not, what requires human confirmation | Management confirmation |
| Prompt Library v1 | Personal and departmental go-to prompts | Classroom exercise |
| High-frequency work list | Work suitable for L2 Skill conversion | Department head confirmation |
| Gate 1 acceptance sheet | Environment, accounts, permissions, data policy, exercises | Pass / Fail |

---

## 11. Gate 1: Eligibility to Enter L2

| Gate | Check Question | Required Evidence | Verdict |
|---|---|---|---|
| Gate 1A: Entry point operational | Can OpenWebUI be signed into, models selected, and chats run? | Sign-in and chat screenshots | Pass / Fail |
| Gate 1B: Accounts manageable | Does each student have their own account, and can Admins review and manage them? | Account sheet, Admin Panel screenshots | Pass / Fail |
| Gate 1C: Personal area usable | Can users create their own chats, history, and folders? | User operation screenshots | Pass / Fail |
| Gate 1D: Permissions controllable | Are roles, groups, features, models, and sharing configured? | RBAC / permission sheet | Pass / Fail |
| Gate 1E: Data policy in place | Are rules defined for permitted input, prohibited input, and human confirmation? | AI usage policy | Pass / Fail |
| Gate 1F: L2 candidates clear | Have high-frequency tasks and Skill candidates been organized? | High-frequency work list | Pass / Fail |

If Gates 1B-1D do not pass, large-scale rollout to employees is not recommended. If Gate 1E does not pass, advanced features such as file upload, Web Search, Tools, and Memory should not be introduced.
