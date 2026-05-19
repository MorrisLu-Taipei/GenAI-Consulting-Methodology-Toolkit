# 如何把 Tiger AI Overlay 套進你的 Fork / How to Apply Tiger AI Overlay to Your Fork

> 🌐 中英雙語 / Bilingual inline

## 0. 適用對象 / Audience

| 你是 / If you are | 用法 / Use |
|---|---|
| **顧問 / AI Champion 接學校案** | Path A 「**完整 fork + overlay**」 |
| **學校 IT / 教務主任，內部試行** | Path B「**本地參考，不公開 fork**」 |
| **方法論研究 / 學者** | Path C「**只讀 overlay 不動 fork**」 |

---

## 1. Path A：完整 fork + overlay（生產用）/ Path A: Full fork + overlay (production)

```bash
# Step 1: 在 GitHub 上 fork 原 repo
#         Fork the original repo on GitHub
# Browser: https://github.com/mihozip/google-workspace-admin-project-workflow
#         → Click "Fork" → 命名為 [your-org]-school-workspace-workflow

# Step 2: clone 你的 fork 到本地
#         Clone your fork locally
git clone https://github.com/[your-org]/[your-org]-school-workspace-workflow.git
cd [your-org]-school-workspace-workflow

# Step 3: 設定 upstream 指向原 repo，方便日後 pull 更新
#         Set upstream remote for future updates
git remote add upstream https://github.com/mihozip/google-workspace-admin-project-workflow.git
git remote -v

# Step 4: 建立 overlay 子資料夾
#         Create overlay subfolder
mkdir -p tigerai-overlay

# Step 5: 從 Tiger AI Methodology Toolkit 複製本 overlay 內容
#         Copy this overlay's contents from Tiger AI Methodology Toolkit
# 9 個檔案 / 9 files:
# - README.md
# - NOTICE.md
# - INSTRUCTIONS_FOR_FORK.md (this file)
# - TIGERAI_METHODOLOGY_LAYER.md
# - TIGERAI_SCHOOL_L1_L3_GUIDE.md
# - TIGERAI_STAGE_GATES_SCHOOL.md
# - TIGERAI_HITL_GATES_SCHOOL.md
# - CHANGELOG.md
# - RELEASE_v0.1.0.md

# Step 6: 在主 README 上方加一段「本 fork 附 Tiger AI overlay」
#         Add "This fork includes Tiger AI overlay" note at the top of main README
# 範例 / example:
cat >> README_TIGERAI_NOTE.md <<'EOF'
> **本 fork 附 Tiger AI overlay**：本 repo 為 mihozip 原作品的 fork，
> 額外附 Tiger AI 教育界 L1-L3 方法論層（位於 `tigerai-overlay/`）。
> 原 repo MIT 授權；overlay Apache 2.0。詳見 `tigerai-overlay/NOTICE.md`。
>
> **This fork includes Tiger AI overlay**: fork of mihozip's original work
> with Tiger AI education-sector L1-L3 methodology layer added in `tigerai-overlay/`.
> Original repo MIT-licensed; overlay Apache 2.0. See `tigerai-overlay/NOTICE.md`.
EOF

# Step 7: commit + push 到你的 fork
#         Commit + push to your fork
git add tigerai-overlay/ README_TIGERAI_NOTE.md
git commit -m "Add Tiger AI methodology overlay v0.1.0 (Apache 2.0)"
git push origin main

# Step 8: 在你的 fork 上發 release tag
#         Cut a release tag on your fork
git tag -a tigerai-v0.1.0 -m "Tiger AI overlay v0.1.0"
git push origin tigerai-v0.1.0
# 在 GitHub UI 把 tag 升級為 Release，貼 RELEASE_v0.1.0.md 內容
```

### 之後上游更新時 / When upstream updates

```bash
git fetch upstream
git merge upstream/main
# 解衝突（如果有）/ Resolve conflicts (if any)
git push origin main
```

> 因為 overlay 全在獨立 `tigerai-overlay/` 資料夾，**幾乎不會跟上游衝突**。/ Because overlay sits in its own `tigerai-overlay/` folder, **upstream conflicts almost never happen**.

---

## 2. Path B：本地參考，不公開 fork / Path B: Local reference, no public fork

如果你只是想試用、不打算對外發布修改 / If you just want to try without releasing publicly:

```bash
# 直接 clone 原 repo（不 fork）
git clone https://github.com/mihozip/google-workspace-admin-project-workflow.git
cd google-workspace-admin-project-workflow

# 把本 overlay 的 9 個檔案複製到 ./tigerai-overlay/
# 試用，不 push 到任何公開 repo
```

這條路徑下，你沒有義務 redistribute；只要不把它 push 到公開 repo，不需要展示 NOTICE。
Under this path, you have no redistribution obligations; as long as you don't push to a public repo, no NOTICE display required.

⚠️ 但**任何把這套東西部署到實際工作場景（學校 / 公司 / 顧問案）**仍需要：/ But **any deployment to real-world use (school / company / engagement)** still requires:

- 學校 IT 主管知悉本 overlay 與原 repo 的雙重授權
- 教師 / 行政人員了解 AI 規範
- 學生資料處理符合個資法 / GDPR / FERPA 等

---

## 3. Path C：只讀 overlay 不動 fork / Path C: Read-only, no fork

如果你只是想了解 Tiger AI 怎麼把教育情境對應到 L1-L3 / If you just want to understand the L1-L3 mapping for education:

→ 直接讀 [`TIGERAI_METHODOLOGY_LAYER.md`](TIGERAI_METHODOLOGY_LAYER.md) 與 [`TIGERAI_SCHOOL_L1_L3_GUIDE.md`](TIGERAI_SCHOOL_L1_L3_GUIDE.md)

不需要做任何 git 動作。/ No git actions required.

---

## 4. 客製化建議 / Customization Tips

### 4.1 把學校 / 縣市名稱換進去

範本檔案內所有 `[填入 / fill in]` 占位符請改成 **你自己學校 / 縣市的真實資料**。**但不要把改完的版本 push 到公開 repo**（會洩露學校內部資料）。
All `[填入 / fill in]` placeholders should be replaced with **your real school / district data**. **Do NOT push the filled version to a public repo** (would leak internal data).

### 4.2 Stage Gate 的角色名稱

`TIGERAI_STAGE_GATES_SCHOOL.md` 預設用「校長 / 教務主任 / 學年主任」三個角色。若你學校組織結構不同（如私校用「執行長 / 學務長」），自行調整名稱。
`TIGERAI_STAGE_GATES_SCHOOL.md` defaults to 校長 / 教務主任 / 學年主任. If your school structure differs (e.g., private school uses 執行長 / 學務長), adjust accordingly.

### 4.3 加入自家公文範本

`TIGERAI_HITL_GATES_SCHOOL.md` 的「公文簽核」HITL 範例是通用版，請對接你學校自家的公文系統格式。
The "公文簽核" HITL example is generic; adapt to your school's actual document system.

---

## 5. 何時不要用這個 overlay / When NOT to use this overlay

| 情境 / Scenario | 為什麼不適合 / Why |
|---|---|
| 學校 < 5 人（如小型補習班）| 用 SOHO Path 就好，overlay 太重 |
| 學校已有完整數位轉型 PMO | 你可能已超過 L3，這個 overlay 主打 L1-L3 入門 |
| 學校不用 Google Workspace（用 Microsoft 365） | 原 repo 是 Workspace-specific；本 overlay 的部分概念可移植，但實作部分要重寫 |

---

## 6. 求助 / Getting Help

- Tiger AI Methodology 主 repo Issue：<https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit/issues>
- 原 repo Issue（限原 repo bug，不要在那裡問 Tiger AI overlay 問題）：<https://github.com/mihozip/google-workspace-admin-project-workflow/issues>
