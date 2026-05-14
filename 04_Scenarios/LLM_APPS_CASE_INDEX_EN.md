# LLM Apps Case Index

> 🌐 中文版本 / Chinese version: [LLM_APPS_CASE_INDEX.md](LLM_APPS_CASE_INDEX.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit>
>
> **Reference Sources (multi-source index):**
> - [`Shubhamsaboo/awesome-llm-apps`](https://github.com/Shubhamsaboo/awesome-llm-apps) (Apache-2.0, Shubham Saboo) — 100+ runnable AI Agent / RAG apps. Citation: [`../90_References/AWESOME_LLM_APPS_REFERENCE.md`](../90_References/AWESOME_LLM_APPS_REFERENCE.md).
> - [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) (MIT, patchy631 / Daily Dose of Data Science) — 93+ runnable AI engineering projects across beginner / intermediate / advanced levels. Citation: [`../90_References/AI_ENGINEERING_HUB_REFERENCE.md`](../90_References/AI_ENGINEERING_HUB_REFERENCE.md).
>
> This index is this methodology's original L1-L5 / course mapping; **no app source code is reproduced**. Each row notes its reference source.

---

## 1. Why This Index

The biggest blocker when an enterprise adopts Gen AI is often not "we don't know how" but **"we don't know what we can do."** This index consolidates several high-quality open-source case libraries (currently 2 sources, ~130+ cases) and **maps them onto this methodology's L1-L5 maturity model and courses**, so consultants and clients can quickly answer:
- I'm at L[X] — which cases suit me?
- Which course level should this case be taught at?
- Which cases are not yet suitable for me (out of level)?

> How to use: after diagnosing the client's L level, pick 3-5 cases the client "feels strongly about" from the corresponding L-level table, as PoC candidates or in-class demos.

**The index is continuously expandable** — when evaluating a new open-source case library in the future, add a "source" and merge its cases into the corresponding L-level tables.

---

## 2. Mapping Logic

| Case type | Maps to this methodology | Rationale |
| --- | --- | --- |
| Chat with X, Local ChatGPT, simple Starters | **L1 Chat AI** | Conversing with data, single-shot tasks, individual entry level |
| Agent Skills, single-purpose packaged capabilities, OCR/Vision extraction | **L2 Skill AI** | A reusable packaged capability = a Skill |
| RAG pipelines, MCP integration, document pipelines, Chat with systems | **L3 Workflow AI** | Retrieval pipelines, tool/system integration |
| Advanced Single-Agent, Memory Apps, Agentic/Autonomous RAG | **L4 Auto Agentic AI** | Autonomous multi-step, memory, tool chains, single Agent |
| Multi-agent Teams, Multi-Agent applications | **L5 Agentic Team AI** | Multi-Agent collaboration |
| Voice, Optimization, Fine-tuning, Framework courses, Model comparisons, Game-Playing | **Cross-cutting / technical support / not mapped** | Technical extensions or demos, not a single L-level course |

"Source" column: `awesome-llm-apps` = A · `ai-engineering-hub` = H.

---

## 3. The L1-L5 Index

### 3.1 L1 Chat AI (maps to course: L1 OpenWebUI Enterprise Enablement)

| Case | Source | Original category | Application scenario / Note |
| --- | --- | --- | --- |
| Chat with PDF (GPT & Llama3) | A | Chat with X | Document Q&A — the most core L1 entry point |
| Chat with Research Papers / ArXiv | A | Chat with X | Research document Q&A |
| Chat with YouTube Videos | A | Chat with X | Video summarization and Q&A |
| Chat with Substack | A | Chat with X | Subscription-content Q&A |
| Chat with GitHub | A | Chat with X | L1 entry experience; the integration aspect touches L3 |
| Chat with Gmail | A | Chat with X | L1 entry experience; the integration aspect touches L3 |
| AI Blog to Podcast Agent | A | Starter | Content conversion — single-shot task |
| AI Meme Generator Agent | A | Starter | Fun demo, for icebreaking |
| Gemini Multimodal Agent | A | Starter | Multimodal conversation entry level |
| Local ChatGPT (DeepSeek / Llama / Gemma 3) | H | Chat Interfaces | On-prem ChatGPT — entry point for fully on-premises deployment |
| DeepSeek Thinking UI | H | Chat Interfaces | A chat interface that visualizes the reasoning process |
| Qwen3 Thinking UI | H | Chat Interfaces | A chat interface that visualizes the reasoning process |

### 3.2 L2 Skill AI (maps to course: L2 Antigravity Agentic Developer)

| Case | Source | Original category | Application scenario / Note |
| --- | --- | --- | --- |
| Academic Researcher | A | Agent Skills | 19 reusable Skills — **the best template for the L2 "Skill" concept** |
| Code Reviewer | A | Agent Skills | Engineering Skill |
| Content Creator | A | Agent Skills | Marketing / content Skill |
| Data Analyst | A | Agent Skills | Data Skill |
| Debugger | A | Agent Skills | Engineering Skill |
| Decision Helper | A | Agent Skills | Decision-support Skill |
| Deep Research | A | Agent Skills | Research Skill |
| Editor | A | Agent Skills | Text-editing Skill |
| Email Drafter | A | Agent Skills | Sales / customer-service Skill |
| Fact Checker | A | Agent Skills | Verification Skill |
| Fullstack Developer | A | Agent Skills | Engineering Skill |
| Meeting Notes | A | Agent Skills | Meeting-notes Skill |
| Project Planner | A | Agent Skills | PM Skill |
| Python Expert | A | Agent Skills | Engineering Skill |
| Sprint Planner | A | Agent Skills | Agile / PM Skill |
| Strategy Advisor | A | Agent Skills | Strategy Skill |
| Technical Writer | A | Agent Skills | Documentation Skill |
| UX Designer | A | Agent Skills | Design Skill |
| Visualization Expert | A | Agent Skills | Data-visualization Skill |
| Self-Improving Agent Skills | A | Agent Skills | Advanced — Skill self-improvement (the L2→L4 boundary) |
| AI Data Analysis Agent | A | Starter | Single-purpose packaged capability |
| AI Music Generator Agent | A | Starter | Creative Skill |
| Web Scraping AI Agent | A | Starter | Data-extraction Skill |
| AI Medical Imaging Agent | A | Starter | Domain-expert Skill (healthcare, requires a human Gate) |
| AI Travel Agent (Local & Cloud) | A | Starter | Planning Skill |
| LaTeX OCR with Llama | H | OCR & Vision | Document-extraction Skill |
| Llama OCR | H | OCR & Vision | Document-extraction Skill |
| Gemma-3 OCR | H | OCR & Vision | Document-extraction Skill |
| Qwen 2.5 VL OCR | H | OCR & Vision | Visual document-extraction Skill |

### 3.3 L3 Workflow AI (maps to course: L3 n8n + AG/n8n Skill Pack)

| Case | Source | Original category | Application scenario / Note |
| --- | --- | --- | --- |
| Basic RAG Chain | A | RAG | RAG entry level — the L3 retrieval-pipeline foundation |
| AI Blog Search (RAG) | A | RAG | Content retrieval |
| RAG with Database Routing | A | RAG | Multi-data-source routing |
| Hybrid Search RAG (Cloud) | A | RAG | Hybrid retrieval |
| Local Hybrid Search RAG | A | RAG | On-prem hybrid retrieval |
| Llama 3.1 Local RAG | A | RAG | On-prem RAG (maps to Hybrid/fully on-premises) |
| Deepseek Local RAG Agent | A | RAG | On-prem RAG |
| Local RAG Agent | A | RAG | On-prem RAG |
| RAG Agent with Cohere | A | RAG | Provider-specific RAG |
| Contextual AI RAG Agent | A | RAG | Context-aware RAG |
| Vision RAG | A | RAG | Multimodal retrieval |
| RAG-as-a-Service | A | RAG | RAG as a service |
| Browser MCP Agent | A | MCP | Tool integration — browser |
| GitHub MCP Agent | A | MCP | Tool integration — GitHub |
| Notion MCP Agent | A | MCP | Tool integration — Notion |
| Multi-MCP Agent Router | A | MCP | Multi-tool routing |
| Llama3 Stateful Chat | A | Memory | Stateful conversation (the L3→L4 boundary) |
| Simple RAG Workflow | H | RAG | RAG entry level |
| Document Chat RAG | H | RAG | Document Q&A pipeline |
| Fastest RAG Stack | H | RAG | High-efficiency RAG tech stack |
| GitHub RAG | H | RAG | Code-repository retrieval |
| ModernBERT RAG | H | RAG | Embedding-model implementation |
| Llama 4 RAG | H | RAG | New-model RAG |
| Colbert RAG | H | RAG | Late-interaction retrieval |
| GroundX Document Pipeline | H | Infrastructure | Document-processing pipeline |
| NotebookLM Clone | H | Infrastructure | Document Q&A / summarization application |
| MindsDB MCP | H | Infrastructure | MCP — database integration |
| Graphiti MCP | H | Infrastructure | MCP — knowledge-graph integration |
| Pixeltable MCP | H | Infrastructure | MCP — multimodal data integration |

### 3.4 L4 Auto Agentic AI (maps to course: L4 Hermes Agent)

| Case | Source | Original category | Application scenario / Note |
| --- | --- | --- | --- |
| AI Deep Research Agent | A | Advanced (Single) | Autonomous deep research — a core L4 case |
| AI Research Planner & Executor | A | Advanced (Single) | Planning + execution |
| AI Consultant Agent | A | Advanced (Single) | Consultant-type Agent |
| AI System Architect Agent | A | Advanced (Single) | Architecture-planning Agent |
| AI Movie Production Agent | A | Advanced (Single) | Creative-production Agent |
| AI Investment Agent | A | Advanced (Single) | Investment analysis (requires a human Gate) |
| Earnings Call Analyst Agent | A | Advanced (Single) | Financial-report analysis |
| AI Health & Fitness Agent | A | Advanced (Single) | Health planning (requires a human Gate) |
| AI Fraud Investigation Agent | A | Advanced (Single) | Fraud investigation (high risk, requires a human Gate) |
| AI Journalist Agent | A | Advanced (Single) | News writing |
| AI Meeting Agent | A | Advanced (Single) | Meeting preparation and summarization |
| Autonomous RAG | A | RAG | Autonomous retrieval (RAG → L4) |
| Agentic RAG with Reasoning | A | RAG | Reasoning-based autonomous RAG |
| Agentic RAG with Embedding Gemma | A | RAG | Autonomous RAG |
| Gemini Agentic RAG | A | RAG | Autonomous RAG |
| Multimodal Agentic RAG | A | RAG | Multimodal autonomous RAG |
| Corrective RAG (CRAG) | A | RAG | Self-correcting retrieval |
| Knowledge Graph RAG with Citations | A | RAG | Knowledge graph + citations (close to an L4 knowledge-type Agent) |
| RAG Failure Diagnostics Clinic | A | RAG | RAG failure diagnostics (maps to L4 failure-mode learning) |
| AI ArXiv Agent with Memory | A | Memory | Research Agent with memory |
| AI Travel Agent with Memory | A | Memory | Planning Agent with memory |
| LLM App with Personalized Memory | A | Memory | Personalized memory |
| Multi-LLM App with Shared Memory | A | Memory | Shared memory (the L4→L5 boundary) |
| Local ChatGPT Clone with Memory | A | Memory | On-prem + memory |
| xAI Finance Agent | A | Starter | Finance Agent |
| OpenAI Research Agent | A | Starter | Research Agent |
| AutoGen Stock Analyst | H | Agents | Stock-analysis Agent |
| YouTube Trend Analysis | H | Agents | Trend-analysis Agent |
| Brand Monitoring | H | Agents | Brand-monitoring Agent |
| Hotel Booking Agent | H | Agents | Hotel-booking Agent |
| Paralegal Agent | H | Agents | Paralegal Agent (requires a human Gate) |
| Financial Analyst Agent | H | Agents | Financial-analysis Agent |
| Book Writer Flow | H | Agents | Long-form writing Agent flow |
| Corrective RAG | H | RAG | Self-correcting retrieval |
| Trustworthy RAG | H | RAG | Trust-scored retrieval (maps to the Evidence discipline) |

### 3.5 L5 Agentic Team AI (maps to course: L5 ClawTeam)

| Case | Source | Original category | Application scenario / Note |
| --- | --- | --- | --- |
| AI Competitor Intelligence Agent Team | A | Multi-agent Teams | Competitive-intelligence team |
| AI Finance Agent Team | A | Multi-agent Teams | Financial-analysis team |
| AI Game Design Agent Team | A | Multi-agent Teams | Game-design team |
| AG2 Adaptive Research Team | A | Multi-agent Teams | Adaptive research team |
| AI Legal Agent Team (Cloud & Local) | A | Multi-agent Teams | Legal team (highly sensitive, on-prem option) |
| AI Recruitment Agent Team | A | Multi-agent Teams | Recruitment team |
| AI Real Estate Agent Team | A | Multi-agent Teams | Real-estate team |
| AI Services Agency (CrewAI) | A | Multi-agent Teams | Services-agency team |
| AI Teaching Agent Team | A | Multi-agent Teams | Teaching team |
| Multimodal Coding Agent Team | A | Multi-agent Teams | Multimodal development team |
| Multimodal Design Agent Team | A | Multi-agent Teams | Multimodal design team |
| Multimodal UI/UX Feedback Agent Team | A | Multi-agent Teams | UI/UX feedback team |
| AI Travel Planner Agent Team | A | Multi-agent Teams | Travel-planning team |
| AI VC Due Diligence Agent Team | A | Advanced (Multi) | VC due-diligence team |
| AI Sales Intelligence Agent Team | A | Advanced (Multi) | Sales-intelligence team |
| Trust-Gated Multi-Agent Research Team | A | Advanced (Multi) | Trust-gated research team (maps to the L5 Human Gate) |
| AI Product Launch Intelligence Agent | A | Advanced (Multi) | Product-launch intelligence (maps to manufacturing/retail cases) |
| AI Financial Coach Agent | A | Advanced (Multi) | Multi-Agent financial coach |
| AI Home Renovation Agent | A | Advanced (Multi) | Multi-Agent renovation planning |
| DevPulse AI | A | Advanced (Multi) | Multi-Agent signal intelligence |
| AI Self-Evolving Agent | A | Advanced (Multi) | Self-evolving (advanced) |
| AI News and Podcast Agents | A | Advanced (Multi) | News + Podcast multi-Agent |
| AI Mental Wellbeing Agent | A | Advanced (Multi) | Multi-Agent mental wellbeing (requires a human Gate) |
| Mixture of Agents | A | Starter | Multi-Agent mixture |
| Insurance Claim Live Agent Team | A | Voice | Insurance-claim voice team |
| Multi-Agent Deep Researcher | H | Infrastructure | Multi-Agent deep-research team |

### 3.6 Cross-Cutting / Technical Support / Not Course-Mapped

| Case | Source | Original category | Application scenario / Note |
| --- | --- | --- | --- |
| AI Audio Tour Agent | A | Voice | Voice extension, can layer on L3/L4 |
| Customer Support Voice Agent | A | Voice | Customer-service voice, can layer on L3/L4 |
| Voice RAG Agent (OpenAI SDK) | A | Voice | Voice + RAG, layers on L3 |
| OpenSource Voice Dictation Agent | A | Voice (external link) | Voice dictation tool |
| Real-time Voice Bot | H | Voice & Audio | Real-time voice, can layer on L3/L4 |
| RAG Voice Agent | H | Voice & Audio | Voice + RAG |
| Chat with Audios | H | Voice & Audio | Audio-content Q&A |
| Multilingual Meeting Notes Generator | H | Voice & Audio | Multilingual meeting notes (can map to an L2 Skill) |
| Toonify Token Optimization | A | Optimization | Cross-cutting technical support — API cost optimization |
| Headroom Context Optimization | A | Optimization | Cross-cutting technical support — context reduction |
| Gemma 3 Fine-tuning | A | Fine-tuning | Advanced technique — model customization (maps to fully on-premises) |
| Llama 3.2 Fine-tuning | A | Fine-tuning | Advanced technique — model customization |
| DeepSeek Fine-tuning | H | Fine-tuning | Advanced technique — model customization |
| Build Reasoning Model | H | Fine-tuning | Advanced technique — reasoning-model training |
| Attention Is All You Need Implementation | H | Fine-tuning | Educational — Transformer fundamentals implementation |
| Google ADK Crash Course | A | Framework course | Cross-cutting — framework learning (L4/L5 advanced) |
| OpenAI Agents SDK Crash Course | A | Framework course | Cross-cutting — framework learning (L4/L5 advanced) |
| Llama 4 vs DeepSeek-R1 | H | Model Comparisons | Cross-cutting — model-selection reference |
| Qwen3 vs DeepSeek-R1 | H | Model Comparisons | Cross-cutting — model-selection reference |
| O3 vs Claude Code | H | Model Comparisons | Cross-cutting — tool-selection reference |
| AI 3D Pygame Agent | A | Game-Playing | Not mapped to an enterprise course — for learning / demo |
| AI Chess Agent | A | Game-Playing | Not mapped to an enterprise course — for learning / demo |
| AI Tic-Tac-Toe Agent | A | Game-Playing | Not mapped to an enterprise course — for learning / demo |
| Openwork (Open Browser Automation) | A | Multi-agent (external link) | External project, browser automation |

> ai-engineering-hub has 93+ projects across beginner / intermediate / advanced levels; this table covers its representative, named projects, with more to be added over time.

---

## 4. Quick Lookup by Enterprise Function

> The same cases, looked up along a different axis — grouped by **enterprise department / function**, so people in different departments can quickly see "which ones relate to me."
> Each row notes the L level (maturity) and source (A = awesome-llm-apps, H = ai-engineering-hub). The department classification is this methodology's judgment; some cases span multiple departments.
> Departments are not limited to those below — consultants may add more based on the client's actual organization.

### 4.1 Engineering / IT

| Case | L level | Source |
| --- | --- | --- |
| Code Reviewer / Debugger / Python Expert / Fullstack Developer / Technical Writer | L2 | A |
| AI System Architect Agent | L4 | A |
| Multimodal Coding Agent Team | L5 | A |
| GitHub MCP Agent / Browser MCP Agent | L3 | A |
| Chat with GitHub | L1 | A |
| GitHub RAG / ModernBERT RAG | L3 | H |
| Google ADK / OpenAI Agents SDK Crash Course | Cross-cutting | A |
| Build Reasoning Model / Attention Is All You Need implementation | Cross-cutting | H |

### 4.2 Finance

| Case | L level | Source |
| --- | --- | --- |
| xAI Finance Agent | L4 | A |
| AI Investment Agent / Earnings Call Analyst Agent | L4 | A |
| Financial Analyst Agent / AutoGen Stock Analyst | L4 | H |
| AI Finance Agent Team | L5 | A |
| AI Financial Coach Agent | L5 | A |
| AI VC Due Diligence Agent Team | L5 | A |

### 4.3 HR

| Case | L level | Source |
| --- | --- | --- |
| AI Recruitment Agent Team (incl. resume screening) | L5 | A |
| Meeting Notes (interview notes) | L2 | A |
| Email Drafter (HR notification emails) | L2 | A |
| LLM App with Personalized Memory (new-hire onboarding knowledge) | L4 | A |

### 4.4 Sales

| Case | L level | Source |
| --- | --- | --- |
| Email Drafter (sales email drafts) | L2 | A |
| AI Sales Intelligence Agent Team | L5 | A |
| AI Competitor Intelligence Agent Team | L5 | A |
| AI Product Launch Intelligence Agent | L5 | A |
| Brand Monitoring | L4 | H |
| AI Real Estate Agent Team | L5 | A |

### 4.5 Marketing

| Case | L level | Source |
| --- | --- | --- |
| Content Creator | L2 | A |
| AI Music Generator / AI Meme Generator | L1-L2 | A |
| AI Blog to Podcast Agent | L1 | A |
| AI News and Podcast Agents | L5 | A |
| AI Movie Production Agent | L4 | A |
| YouTube Trend Analysis | L4 | H |
| Multimodal Design Agent Team / UI/UX Feedback Agent Team | L5 | A |

### 4.6 R&D

| Case | L level | Source |
| --- | --- | --- |
| Academic Researcher / Deep Research | L2 | A |
| Chat with Research Papers / ArXiv | L1 | A |
| AI Deep Research Agent / AI Research Planner & Executor / OpenAI Research Agent | L4 | A |
| AI ArXiv Agent with Memory | L4 | A |
| AG2 Adaptive Research Team / Trust-Gated Multi-Agent Research Team | L5 | A |
| Multi-Agent Deep Researcher | L5 | H |

### 4.7 Operations

| Case | L level | Source |
| --- | --- | --- |
| Project Planner / Sprint Planner | L2 | A |
| AI Meeting Agent / Meeting Notes | L2-L4 | A |
| Multilingual Meeting Notes Generator | Cross-cutting | H |
| GroundX Document Pipeline / NotebookLM Clone | L3 | H |
| DevPulse AI (signal intelligence) | L5 | A |
| AI Services Agency (CrewAI) | L5 | A |
| Hotel Booking Agent | L4 | H |

### 4.8 Customer Service

| Case | L level | Source |
| --- | --- | --- |
| Customer Support Voice Agent | Voice extension | A |
| Real-time Voice Bot / RAG Voice Agent | Voice extension | H |
| Insurance Claim Live Agent Team | L5 | A |
| Various RAG (FAQ / knowledge-base Q&A) | L3-L4 | A / H |
| Chat with PDF / Substack (internal knowledge Q&A) | L1 | A |

### 4.9 Legal & Compliance

| Case | L level | Source |
| --- | --- | --- |
| AI Legal Agent Team (Cloud & Local) | L5 | A |
| Paralegal Agent | L4 | H |
| AI Fraud Investigation Agent | L4 | A |
| Fact Checker | L2 | A |
| Trustworthy RAG (trust-scored retrieval) | L4 | H |

### 4.10 Data & Analytics

| Case | L level | Source |
| --- | --- | --- |
| Data Analyst / AI Data Analysis Agent / Visualization Expert | L2 | A |
| Various RAG (retrieval pipelines) | L3 | A / H |
| Knowledge Graph RAG with Citations | L4 | A |
| Model Comparisons (selection reference) | Cross-cutting | H |
| OCR series (LaTeX / Llama / Gemma-3 / Qwen VL OCR) | L2 | H |

### 4.11 Design & Creative

| Case | L level | Source |
| --- | --- | --- |
| UX Designer | L2 | A |
| Multimodal Design Agent Team / UI/UX Feedback Agent Team | L5 | A |
| AI Game Design Agent Team | L5 | A |

### 4.12 Cross-Functional & Management

| Case | L level | Source |
| --- | --- | --- |
| Strategy Advisor / Decision Helper | L2 | A |
| AI Consultant Agent | L4 | A |
| Editor | L2 | A |
| LLM Apps with Memory (organizational knowledge memory) | L4 | A |
| Toonify / Headroom (cost / context optimization) | Cross-cutting | A |

> **Non-enterprise-department cases** (consumer / personal-use scenarios, listed for reference but not the main thrust of enterprise adoption): AI Travel Agent, AI Health & Fitness Agent, AI Mental Wellbeing Agent, AI Home Renovation Agent, AI Breakup Recovery Agent, Game-Playing Agents.

---

## 5. Summary

| Mapped level | Cases (approx.) | Corresponding course |
| --- | ---: | --- |
| L1 Chat AI | 12 | L1 OpenWebUI Enterprise Enablement |
| L2 Skill AI | 29 | L2 Antigravity Agentic Developer |
| L3 Workflow AI | 29 | L3 n8n + AG/n8n Skill Pack |
| L4 Auto Agentic AI | 34 | L4 Hermes Agent |
| L5 Agentic Team AI | 26 | L5 ClawTeam |
| Cross-cutting / not mapped | 24 | Technical support / demo |
| **Total (2 sources)** | **~150+** | — |

> **Observation**: cases are densest at L2, L3, and L4 — reflecting that the industry's current LLM-application focus is on "packaged capabilities → system integration → autonomous Agents." L5 multi-Agent team cases have also taken shape. RAG is the largest category in L3-L4.

---

## 6. How to Use in the Consulting Flow

| Consulting scenario | How to use |
| --- | --- |
| **Discovery phase** | Show the client the case table for their L level and ask "which ones do you feel strongly about?" — quickly find PoC candidates |
| **L1-L5 course design** | Each course level can pick 3-5 cases from the corresponding table as demos / exercises |
| **Cross-level expectation management** | If a client points at an L5 case and says "I want this," use the index to point out "you're at L2 now, this needs L3-L4 first" |
| **PoC scenario library expansion** | Cases can be turned into PoC drafts in `../02_Course_Design/POC_SCENARIO_SPECS.md` |
| **Model / tool selection** | The Model Comparisons in §3.6 can serve as a reference for deployment mode and provider selection |

> ⚠️ Note: these apps are mostly **demo / starter templates / learning projects**; enterprise adoption must still apply this methodology's governance (human Gate, Evidence, Stage Gate, security review). Items marked "requires a human Gate" in the index are high-risk domains.

---

## 7. Citation & License

The **mappings (L1-L5, course mapping, application-scenario notes) in this index are this methodology's original work**; the **case lists and categories** are referenced from two sources:

- `Shubhamsaboo/awesome-llm-apps` (Apache-2.0) — see [`../90_References/AWESOME_LLM_APPS_REFERENCE.md`](../90_References/AWESOME_LLM_APPS_REFERENCE.md)
- `patchy631/ai-engineering-hub` (MIT) — see [`../90_References/AI_ENGINEERING_HUB_REFERENCE.md`](../90_References/AI_ENGINEERING_HUB_REFERENCE.md)

This methodology does **not reproduce any app's source code** — it only cites case names and categories as an index. Learners wishing to build a case should obtain it from the corresponding upstream repo and comply with its license.
