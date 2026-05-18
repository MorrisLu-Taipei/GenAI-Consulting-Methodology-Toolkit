# L1 OpenWebUI Admin Runbook

> 對應課程 / Course: [L1_OPENWEBUI_COURSE_PLAN.md](../L1_OPENWEBUI_COURSE_PLAN.md) §6.2 + §10 Deliverables
> 版本 / Version: 範本 v1.0（IT / AI Champion 填空式）/ Template v1.0 (fillable by IT / AI Champion)
> 授權 / License: Apache 2.0

## 0. 本 Runbook 定位 / Purpose

讓 **企業 IT / AI Champion** 在 1 天內能完成 OpenWebUI 從**安裝 → 帳號 → 角色 → 群組 → 權限 → 模型 → 功能 → 公告**的完整設定，並產出可審計的 Gate 1 驗收紀錄。
Enable **enterprise IT / AI Champion** to complete OpenWebUI's full configuration (install → accounts → roles → groups → permissions → models → features → announcements) within 1 day, producing auditable Gate 1 evidence.

---

## 1. 安裝與環境 / Install & Environment

### 1.1 部署模式選擇 / Deployment mode

| 模式 / Mode | 適用 / When | 備註 / Notes |
|---|---|---|
| **雲端託管** / Cloud-hosted | 1-100 人試行 / 1-100 user pilot | 最快上線；不適合機敏資料 / Fastest; not for sensitive data |
| **Hybrid（雲 UI + 地端模型）** / Hybrid (cloud UI + on-prem model) | 100-500 人 | UI 在雲，model 在公司 / UI cloud, model on-prem |
| **全地端** / Fully on-prem | 500+ 人 / 受監管產業 / 500+ users / regulated industry | 自主可控 / Self-controlled |

> 選定模式：__________________ / Selected mode: __________________

### 1.2 安裝步驟（Docker）/ Installation steps (Docker)

```bash
# 預備 / Prep
docker --version  # confirm Docker ≥ 24
mkdir -p /opt/openwebui && cd /opt/openwebui

# 拉鏡像 / Pull image
docker pull ghcr.io/open-webui/open-webui:main

# 建立 volume / Create volume
docker volume create openwebui-data

# 啟動 / Start
docker run -d --name openwebui \
  -p 3000:8080 \
  -v openwebui-data:/app/backend/data \
  -e WEBUI_SECRET_KEY="[填入 / fill in random string]" \
  ghcr.io/open-webui/open-webui:main

# 健檢 / Health check
curl http://localhost:3000/health
```

### 1.3 環境健檢清單 / Health-check list

- [ ] 服務啟動成功 / Service started
- [ ] 第一個 Admin 已建立 / First Admin created
- [ ] 至少 1 個模型可用 / At least 1 model available
- [ ] HTTPS 已設定（透過 nginx / cloudflare）/ HTTPS configured (via nginx / cloudflare)
- [ ] 自動備份已設定 / Auto-backup configured
- [ ] 監控 alert 已設定 / Monitoring alerts configured

---

## 2. 帳號管理 / Account Management

### 2.1 角色定義 / Role definitions

| 角色 / Role | 權限 / Permissions | 預設指派對象 / Default assignees |
|---|---|---|
| **Admin** | 全部 / All | IT 主管 + 1 個 backup |
| **User** | 聊天、模型、Prompt 個人區 / Chat, model, personal prompts | 一般員工 / Regular employees |
| **Pending** | 無，等審核 / None, awaiting review | 新註冊未審核 / Newly registered |

### 2.2 開通流程 / Onboarding flow

```text
新員工註冊 / New employee registers
    ↓
Pending（預設）/ Pending (default)
    ↓
Admin 審核：確認 email 屬於公司 + 確認所屬部門 / Admin reviews: confirm email belongs to company + dept
    ↓
指派為 User + 加入部門群組 / Assign as User + add to dept group
    ↓
寄通知信給新員工 / Send onboarding email
```

### 2.3 離職處理 SOP / Offboarding SOP

| # | 動作 / Action | 時限 / SLA |
|---|---|---|
| 1 | 收到 HR 離職通知 / Receive HR notice | T+0 |
| 2 | Disable 帳號（保留資料）/ Disable account (preserve data) | T+0 |
| 3 | 匯出該員工聊天紀錄 / Export employee's chat history | T+1 |
| 4 | 移除個人 Prompt / 個人資料 / Delete personal prompts / data | T+30（依公司資料保留政策 / per data retention policy） |
| 5 | 從所有 group 移除 / Remove from all groups | T+1 |

---

## 3. 群組與權限矩陣 / Groups & Permission Matrix

### 3.1 建議群組結構 / Recommended group structure

```text
Company-wide / 全公司
├─ Dept-Sales / 業務部
├─ Dept-Marketing / 行銷部
├─ Dept-IT / IT 部
├─ Dept-HR / 人資部
├─ Dept-Finance / 財務部
├─ Power-Users / Power users（可用進階功能 / advanced features）
└─ AI-Champion-Team / AI 種子團隊
```

### 3.2 預設權限矩陣 / Default permission matrix

| 功能 / Feature | Company-wide | Dept-IT | Power-Users | AI-Champion |
|---|---|---|---|---|
| File Upload（低敏感）/ File Upload (low-sensitivity) | ✅ | ✅ | ✅ | ✅ |
| File Upload（高敏感）/ File Upload (high-sensitivity) | ❌ | ⚠️ HITL | ⚠️ HITL | ⚠️ HITL |
| Web Search | ❌ | ✅ | ✅ | ✅ |
| Image Generation | ❌ | ❌ | ✅ | ✅ |
| Code Interpreter | ❌ | ✅ | ✅ | ✅ |
| API Keys 管理 / API Keys mgmt | ❌ | ✅ | ❌ | ❌ |
| Public Sharing | ❌ | ❌ | ❌ | ⚠️ HITL |

> **原則 / Principle：** Least privilege + additive；先全部關，再依群組打開。/ Start fully restricted; open per group.

---

## 4. 模型控管 / Model Control

### 4.1 模型清單 / Model inventory

| 模型 / Model | 部署位置 / Where | 可用群組 / Allowed groups | 用途 / Use |
|---|---|---|---|
| `[填入 / fill in]` | 雲 / Cloud | Company-wide | 日常聊天 / Daily chat |
| `[填入 / fill in]` | 雲 / Cloud | Power-Users | 長文 / Long content |
| `[填入 / fill in]` | 地端 Ollama / On-prem Ollama | Company-wide | 機敏資料 / Sensitive data |
| `[填入 / fill in]` | 雲 / Cloud | AI-Champion | 多模態 / Multimodal |

### 4.2 模型治理規則 / Model governance

- [ ] 機敏資料 → 一律用地端模型 / Sensitive data → on-prem only
- [ ] 公開資料 / 對外文案 → 可用雲端 / Public data → cloud OK
- [ ] 模型新增前必須 Admin 評估 + 通知 AI Champion / New models require Admin review + AI Champion notice
- [ ] 模型成本月度 review / Monthly cost review

---

## 5. 公告與規範 / Announcements & Policy

### 5.1 必貼公告 / Required announcements

```markdown
# 公司 AI 使用規範 / Company AI Usage Policy

1. 不上傳客戶 PII / 信用卡 / 員工身分證號
   No customer PII / credit card / employee ID upload
2. 機敏資料只能用地端模型
   Sensitive data → on-prem model only
3. AI 產出 **必須人工確認** 後才能對外發布
   AI output **must be human-confirmed** before external publishing
4. 違規處理：第一次警告、第二次帳號暫停、第三次依員工守則
   Violations: warning → suspension → per employee handbook
```

### 5.2 規範審核流程 / Policy review flow

- 每季 / Quarterly：AI Champion 帶 review 規範
- 每次政策變動 / Per policy change：全員公告 + 7 天 buffer
- 法規變動觸發 / Regulation change trigger：48 小時內更新

---

## 6. Gate 1 驗收 Checklist / Gate 1 Acceptance Checklist

通過條件 / Pass criteria（全部 ✅ 才算通過）/ All ✅ to pass:

- [ ] 環境健檢 6 項全綠（§1.3）/ Environment health-check 6 items all green
- [ ] 至少 10 個帳號開通 / At least 10 accounts activated
- [ ] 至少 3 個部門群組建立 / At least 3 dept groups created
- [ ] 權限矩陣已套用 / Permission matrix applied
- [ ] 至少 2 個模型可用（1 雲 + 1 地端）/ At least 2 models available (1 cloud + 1 on-prem)
- [ ] AI 使用規範已公告 / AI usage policy announced
- [ ] 學員 80% 完成 §3.3 formative quiz / 80% of learners passed §3.3 quiz
- [ ] 至少 5 個 L2 Skill 候選清單已產出 / At least 5 L2 Skill candidates produced

### 簽核 / Sign-off

| 角色 / Role | 簽名 / Signature | 日期 / Date |
|---|---|---|
| IT 主管 / IT Lead | __________ | __________ |
| AI Champion | __________ | __________ |
| 部門代表 / Dept Rep | __________ | __________ |
