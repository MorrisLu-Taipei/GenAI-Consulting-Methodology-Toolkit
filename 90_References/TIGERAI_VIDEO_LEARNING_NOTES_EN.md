> 🌐 中文版本 / Chinese version: [TIGERAI_VIDEO_LEARNING_NOTES.md](TIGERAI_VIDEO_LEARNING_NOTES.md)

# TigerAI Channel Video Learning Notes and L3 Application Summary

Version: v1.0  
Author: Morris Lu (盧業興) · Tiger AI 虎智科技  
Channel: 虎智科技 TigerAI  
Original channel: `https://www.youtube.com/@%E8%99%8E%E6%99%BA%E7%A7%91%E6%8A%80TigerAI`

---

## 1. How to Use This Document

This document organizes videos from the TigerAI channel that can be used for L1-L4 course design, with particular focus on n8n and L3 Workflow AI.

Organization approach:

1. Build learning summaries based on the publicly available video catalog and titles.
2. Map videos to L1 / L2 / L3 / L4 course uses.
3. Organize the n8n videos into L3 course modules and a PoC roadmap.
4. Organize the OpenGenie videos into an adoption thread covering enterprise governance, accounts, permissions, models, Prompts, Channels, n8n integration, RAG/Vision, and feedback systems.

Priority:

| Priority | Description |
|---|---|
| P0 | Must-watch for the L3 n8n core course |
| P1 | Important supporting content for L1 / L2 / L3 / L4 |
| P2 | Industry- or department-specific elective case |
| P3 | Demo or inspirational case |

---

## 2. Overall Conclusion for the L3 Course

The TigerAI n8n videos are not simply tool tutorials; they are a complete enterprise process automation case library. The L3 training logic they reveal should be:

> Pick up where the L2-produced Skill / Workflow Blueprint leaves off, and use n8n to turn it into a process PoC that is executable, verifiable, backed up, operable, and integrable across platforms.

Therefore the L3 course should emphasize:

1. Trigger: Webhook, schedule, Gmail, LINE, Facebook, YouTube, GCS / API event.
2. Data Handling: Data Tables, Sheets, BigQuery, CRM / ERP / API data.
3. AI Processing: Gemini, images, audio, video, documents, copywriting, summarization, classification.
4. Platform Integration: LINE, Facebook, YouTube, social platforms, Gmail, GitHub.
5. Reuse: Sub-workflow modularization.
6. Governance: Credentials, Execution Log, GitHub backup, human review, error handling.
7. L4 Readiness: Make Hermes Agent able to call n8n Workflows in the future.

---

## 3. OpenGenie Enterprise Governance Video Summaries

| # | Video | Learning Summary | Course Application | Priority |
|---:|---|---|---|---|
| OG-1 | [TigerAI OpenGenie 單元 1：帳號體系與權限佈署](https://www.youtube.com/watch?v=wkgx94TmFE4) | Account, user, and permission deployment. | L1 OpenWebUI / OpenGenie enterprise enablement; covers per-person accounts and permission governance. | P1 |
| OG-2 | [單元 2：後端模型 Ollama 管理與安裝](https://www.youtube.com/watch?v=fyK8lIBEdoU) | Back-end model installation and management. | L1 IT / Admin model management; supports cloud AI / Hybrid / fully on-premise decisions. | P1 |
| OG-3 | [單元 3：API Key 彈性配置](https://www.youtube.com/watch?v=IdI_pqRjEOU) | API Key and cloud-assist strategy. | L1/L3 IT; manages model providers, external APIs, and permissions. | P1 |
| OG-4 | [單元 4：Prompts 專家設定](https://www.youtube.com/watch?v=CZwXcgtKn0Y) | Expert Prompt configuration. | L1 Prompt Library; L2 Skill-ification. | P1 |
| OG-5 | [單元 5：群組與協作權限深度管理](https://www.youtube.com/watch?v=G1MKa10W6K0) | Groups and collaboration permissions. | L1 Admin / L3 process permission design. | P1 |
| OG-6 | [單元 6：Channels 協作與會議摘要](https://www.youtube.com/watch?v=38kkwwRDOpU) | Channels, collaboration, and meeting summaries. | L1 departmental collaboration, L2 meeting summary Skill, L3 meeting flow. | P2 |
| OG-7 | [單元 7：n8n 串接與自動化工作流](https://www.youtube.com/watch?v=xX6e0l-TaWg) | OpenGenie and n8n integration; automated workflows. | Core of the L3 main course, serving as the L3 entry video. | P0 |
| OG-8 | [單元 8：多模態進階應用 RAG & Vision](https://www.youtube.com/watch?v=qN_2KSgbjUM) | RAG, Vision, and multimodal applications. | L3 Gemini / multimodal flow; precursor to L4 Hermes knowledge work. | P1 |
| OG-9 | [單元 9：綜合應用與分享機制](https://www.youtube.com/watch?v=jQPBSZmYLbg) | Integrated applications, sharing, and collaboration. | L1/L3 sharing governance and demo showcase. | P2 |
| OG-10 | [單元 10：管理監督與回饋系統](https://www.youtube.com/watch?v=4Lrgg-vdhi8) | Management supervision and feedback. | L3 operations, feedback, quality improvement, and Gate 3 acceptance. | P1 |

---

## 4. Antigravity / L2 Video Summaries

| # | Video | Learning Summary | Course Application | Priority |
|---:|---|---|---|---|
| AG-1 | [1部曲：AI 全自動寫代碼、測試還幫你錄影](https://www.youtube.com/watch?v=LCO700FzoXg) | Antigravity foundation; AI writing code, testing, recording evidence. | L2 Antigravity Foundation. | P1 |
| AG-2 | [2部曲：AI 寫 Code 鬼打牆怎麼辦](https://www.youtube.com/watch?v=RRWtnqqQI0E) | Debugging mindset; Skill plugin extension. | L2 Debug / Skill-ification. | P1 |
| AG-3 | [3部曲：開發環境零手動](https://www.youtube.com/watch?v=kHywZFPsju8) | AI installing packages and UI. | L2 engineering practice. | P1 |
| AG-4 | [4部曲：爬蟲與架站](https://www.youtube.com/watch?v=K4UMhFj9ztE) | Data scraping and a customized web UI. | L2 App prototype; L3 can pick up data flows from here. | P1 |
| AG-5 | [5部曲：Docker 容器化與打包](https://www.youtube.com/watch?v=IILRXP2cMbo) | Docker containerization. | L2 engineering deliverable and L3 deployment precursor. | P1 |
| AG-6 | [6部曲：互動 App 與個人專屬 Skill](https://www.youtube.com/watch?v=q9rNgnqNXlc) | Building an interactive App and personal Skill. | L2 Skill Library and L2-to-L3 Bridge. | P1 |

---

## 5. n8n / L3 Video Summaries

| # | Video | Learning Summary | L3 Course Application | Priority |
|---:|---|---|---|---|
| N27 | [不寫程式也能用 Gemini：n8n 整合 Google Gemini 全攻略](https://www.youtube.com/watch?v=DT5Gx5tMxGs) | Using n8n to integrate Gemini for images, audio, video, and documents. | L3 AI Node / multimodal processing foundation. | P0 |
| N28 | [n8n 進階教學：Sub-workflow 模組化自動化術](https://www.youtube.com/watch?v=hbvHwjrexds) | Building reusable Sub-workflows. | Must-watch for L3 modularization and process standardization. | P0 |
| N29 | [AI 即時查詢神器：高鐵時刻查詢機器人](https://www.youtube.com/watch?v=T1hzDrIhHSk) | LINE auto-reply for schedule, fares, and timetable. | Case for Webhook / LINE / API query flow. | P0 |
| N30 | [AI 人資革命：自動履歷篩選系統](https://www.youtube.com/watch?v=EgSFZm6hvE8) | n8n + Gemini + Gmail + LINE HR process. | HR process PoC: resume intake, AI screening, notifications. | P0 |
| N31 | [史上最強社群自動化](https://www.youtube.com/watch?v=Eb-DwLnNjUk) | Product image to video, copywriting, multi-platform marketing. | Marketing automation PoC. | P2 |
| N32 | [AI 自動發文 2.0](https://www.youtube.com/watch?v=hlhByT2m28M) | Video generation, copywriting, multi-platform publishing. | Social posting Workflow; requires a human review Gate. | P2 |
| N33 | [YouTube AI 留言機器人](https://www.youtube.com/watch?v=3cB4BtGUA9w) | YouTube auto-reply comments and keyword interaction. | Social interaction and customer service flow. | P2 |
| N34 | [n8n 終極備份術](https://www.youtube.com/watch?v=zrsE4-G6MRY) | Auto-syncing Workflows + Credentials to GitHub. | Must-watch for L3 operations, backup, and version governance. | P0 |
| N35 | [Facebook 聊天機器人實戰](https://www.youtube.com/watch?v=c9VuLN_DasA) | Building a Facebook AI customer service bot with n8n + Webhook. | Main case for customer service automation. | P0 |
| N36 | [Data Tables 實戰：Facebook 智能客服](https://www.youtube.com/watch?v=v4plNZNSG08) | n8n Data Tables, Meta platform integration, customized AI replies. | Must-watch for L3 Data Tables and state management. | P0 |
| N37 | [AI 客服升級版：FB 粉專自動回圖、回訊息](https://www.youtube.com/watch?v=pEWn2yh1Dkg) | Image and message replies for Facebook customer service. | Optional multimodal customer service. | P2 |
| N38 | [AI 自動行銷機器人](https://www.youtube.com/watch?v=njcKlnhEaUM) | Freepik + DataForSEO: auto image sourcing, copywriting, keyword selection, posting. | Marketing content supply chain flow. | P2 |
| N39 | [Sora 2 全自動影片工廠](https://www.youtube.com/watch?v=3NJZ99lY8kU) | n8n + Kie AI: one-click video generation and publishing to FB, IG, Threads, YouTube. | Advanced video factory case; requires review and brand Gates. | P3 |

---

## 6. L3 Course Design Implications

### 6.1 We Cannot Teach Only n8n Basics

The TigerAI videos show that what is truly valuable in L3 is not "dragging nodes," but forming a complete closed loop in the process:

`Trigger → Data → AI → System Action → Human Gate → Log → Backup → Reuse`

### 6.2 L3 Must Have Four Case Pools

| Case Pool | Representative Videos | Suitable Clients |
|---|---|---|
| Customer service automation | N35, N36, N37 | Services, e-commerce, fan pages, customer service centers |
| HR automation | N30 | HR, recruitment, HR shared services |
| Marketing automation | N31, N32, N33, N38, N39 | Marketing, content, social, brand |
| Query / utility Bot | N29 | Operations, customer service, internal queries |

### 6.3 L3 Must Add a Governance Course

The GitHub backup in video N34 is very important and should be a required part of L3, not an elective. After enterprises adopt n8n, without backups, versioning, credential management, Execution Logs, and error notifications, the PoC easily becomes an unmaintainable toy.

---

## 7. Recommended Viewing Paths

### 7.1 L3 Core Track

1. OG-7: OpenGenie and n8n integration.
2. N27: n8n + Gemini multimodal.
3. N28: Sub-workflows.
4. N34: GitHub backup.
5. N35: Facebook Webhook customer service.
6. N36: Data Tables.

### 7.2 Customer Service Track

1. N35.
2. N36.
3. N37.
4. OG-10.

### 7.3 HR Track

1. N30.
2. OG-4.
3. OG-6.
4. N34.

### 7.4 Marketing Track

1. N31.
2. N32.
3. N33.
4. N38.
5. N39.

### 7.5 IT / Operations Track

1. OG-1.
2. OG-3.
3. OG-5.
4. N28.
5. N34.
6. OG-10.

---

## 8. Application to Delivery

TigerAI videos should be turned into the following deliverables:

- L3 n8n Workflow Blueprint.
- n8n Workflow JSON.
- Credential / API / Webhook permission sheet.
- Data Tables Schema.
- Sub-workflow Library.
- Execution Log and test records.
- GitHub backup and version management SOP.
- Human Gate design.
- Error Handling / Retry / Fallback design.
- List of Workflows callable by L4 Hermes Agent.
