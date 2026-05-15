# 案例撰寫標準：L1-L5 IPOE 與可驗證交付物

更新日期：2026-05-13

## 1. 目的

所有客戶案例都不能只寫情境故事，必須寫成顧問交付案例。

每個案例都要回答：

1. 客戶目前經過哪些評估？
2. L1-L5 每一級的 input 是什麼？
3. 每一級的 process 是什麼？
4. 每一級的 output 是什麼？
5. 哪些 deliverables 可以被驗證？
6. 如何判斷該階段完成？

## 2. 案例必備章節

每個完整案例至少包含以下章節：

1. 案例定位。
2. 案例交付邏輯。
3. 客戶故事。
4. 問卷填答摘要。
5. 公司屬性與部署模式判斷。
6. 建議課程比例。
7. 課程中應產出的工作資產。
8. 八階段顧問診斷分析。
9. 三階段 Roadmap。
10. ROI 指標。
11. 最終顧問報告摘要。
12. L1-L5 Input / Process / Output / Evidence。
13. 評估流程與可驗證 Deliverables。
14. Stage Gate 驗收設計。

## 3. L1-L5 IPOE 標準格式

IPOE 代表：

- Input：進入該成熟度階段需要的資料、系統、文件、角色、問卷或流程。
- Process：該階段實際做什麼，包括課程、工作坊、系統串接、治理設計。
- Output：該階段產出的文件、Skill、Workflow、Agent、報告或操作成果。
- Evidence：可以證明 output 存在且可用的證據。

### 標準表格

| 項目 | 定義 |
| --- | --- |
| Input | `[資料、系統、流程、角色、問卷、文件]` |
| Process | `[課程、訪談、整理、建置、串接、測試、審核]` |
| Output | `[Prompt、Skill、Workflow、Agent 任務卡、報告、Roadmap]` |
| Evidence | `[截圖、Log、測試案例、簽核、版本紀錄、執行結果]` |
| 驗收標準 | `[可量測或可確認的完成條件]` |

## 4. L1-L5 最低交付標準

### L1 Controlled AI Access

最低 deliverables：

- AI 使用規範。
- 受控 AI 入口或核准工具清單。
- 個人高頻 Prompt 範本。
- 課程練習成果。

可驗證證據：

- 工具截圖。
- 使用規範文件。
- Prompt 範例。
- 參訓紀錄。

### L2 Knowledge Codification

最低 deliverables：

- Skill Library。
- 3-5 個 Skill。
- Skill Owner。
- Skill 版本紀錄。

可驗證證據：

- Skill 模板。
- 範例輸入輸出。
- 非原作者測試結果。
- Owner 簽核。

### L3 Workflow Automation

最低 deliverables：

- n8n Workflow PoC。
- 系統串接清單。
- Credential / 權限表。
- 人工審核節點。
- Log 與錯誤處理。

可驗證證據：

- Workflow JSON。
- Execution Log。
- 測試資料。
- 錯誤通知截圖。
- 人工審核紀錄。

### L4 Autonomous Agent

最低 deliverables：

- Hermes Agent 任務卡。
- Agent 可用工具清單。
- Agent 權限表。
- Agent 回報格式。
- 人工接手機制。

可驗證證據：

- Agent 測試紀錄。
- 工具呼叫紀錄。
- 輸出樣本。
- 人工審核紀錄。

### L5 Multi-Agent Organization

最低 deliverables：

- ClawTeam 角色卡。
- 多 Agent 任務分派表。
- 輸出整合模板。
- Reviewer / Critic / 人工 Gate 設計。
- ROI 追蹤表。

可驗證證據：

- Agent Team 執行紀錄。
- 各 Agent 輸出。
- 整合報告。
- 主管審核紀錄。

## 5. Stage Gate 驗收邏輯

| Gate | 對應成熟度 | 是否可進下一階段的判斷 |
| --- | --- | --- |
| Gate 1 | L1 | 有受控入口、使用規範、基礎 Prompt，且員工知道資料邊界 |
| Gate 2 | L2 | 有可被他人複用的 Skill，並有 Owner 與版本 |
| Gate 3 | L3 | Workflow 可執行，有 Log、人工審核與錯誤處理 |
| Gate 4 | L4 | Agent 可呼叫 Skill / Workflow，權限邊界清楚，輸出可審核 |
| Gate 5 | L5 | 多 Agent 有角色分工、輸出整合與人工 Gate |

## 6. 案例品質檢查表

完成案例前檢查：

- [ ] 是否寫清楚客戶產業、規模、部門、系統？
- [ ] 是否有問卷分數與成熟度判定？
- [ ] 是否有公司屬性與部署模式判斷？
- [ ] 是否有 L1-L5 課程比例？
- [ ] 是否有八階段顧問診斷？
- [ ] 是否有 L1-L5 Input / Process / Output / Evidence？
- [ ] 是否有可驗證 deliverables？
- [ ] 是否有 Stage Gate？
- [ ] 是否有 ROI 指標？
- [ ] 是否有明確安全邊界與人工審核？

