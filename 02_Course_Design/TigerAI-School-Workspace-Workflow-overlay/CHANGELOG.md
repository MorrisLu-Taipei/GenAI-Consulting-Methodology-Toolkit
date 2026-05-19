# Tiger AI School Workspace Workflow Overlay — Changelog

> 🌐 中英雙語 / Bilingual inline
> Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
> Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
>
> 本 overlay 的版本與 Tiger AI Methodology Toolkit 主體 + 原 mihozip repo 都**獨立**。
> This overlay's versioning is **independent** from both the Tiger AI Methodology Toolkit main repo and the upstream mihozip repo.

---

## [v0.1.0] — 2026-05-20

### Added / 新增

- **README.md** —— Overlay 總覽 + 與原 repo 的關係說明（attribution + relationship）
- **NOTICE.md** —— MIT (mihozip) + Apache 2.0 (Tiger AI) 雙重授權聲明 + 引用建議
- **INSTRUCTIONS_FOR_FORK.md** —— 3 條使用路徑（Production fork / Local trial / Read-only）
- **TIGERAI_METHODOLOGY_LAYER.md** —— L1-L5 對位 + 三段式服務流程 + 八階段 + SME Lite Path 對照
- **TIGERAI_SCHOOL_L1_L3_GUIDE.md** —— L1（全員）/ L2（種子科）/ L3（行政自動化）三層詳細實作指南；4 個 L3 主要 use case（公文 / 活動 / 請購 / 家長通知）
- **TIGERAI_STAGE_GATES_SCHOOL.md** —— Gate 1 / 2 / 3 完整驗收設計 + 各 Gate 常見失敗原因 + 退場機制
- **TIGERAI_HITL_GATES_SCHOOL.md** —— 4 大類 HITL（公文 / 學生資料 / 對外公告 / 家長通知）+ Apps Script 層實作建議 + 法律規範對位
- **CHANGELOG.md**（本檔）—— 獨立版本紀錄
- **RELEASE_v0.1.0.md** —— 第一版完整 release notes

### Known Limitations / 已知限制

- 本版本**未實際 fork** 原 repo。Path A（完整 fork + overlay）由使用者手動執行（見 `INSTRUCTIONS_FOR_FORK.md`）。
- 4 個 L3 use case 中，目前只有「公文簽核」與「家長通知」有完整 HITL 範本；「活動申請」與「物資請購」的 HITL 範本將在 v0.2.0 補完。
- 跟原 repo 的 `src/Code.gs` 的具體程式碼修改建議（HITL wrapping pattern）目前是概念範例，尚未提供完整可 paste 的程式碼 fragment。

### Roadmap / 接下來

| Version | Plan | ETA |
|---|---|---|
| v0.2.0 | 補完活動 / 請購 HITL 範本 + 加 Apps Script HITL wrapper 完整 code sample | 視客戶實際導入需求 |
| v0.3.0 | 加 3 個學校 worked example（小型私立 / 公立 K-12 / 大型完全中學）匿名化案例 | v0.2 後 1-2 月 |
| v0.4.0 | 對位台灣《AI 產業人才認定指引》三大類別 + 教師職能對應 | 視 AI 人才指引整合進度 |
| v1.0.0 | 跑過 ≥ 1 個學校真實導入後，將 lessons learned 沉澱 | 視試行客戶簽約進度 |

---

## [Unreleased]

（暫無預告變動 / No planned changes yet）

---

## License & Attribution

- Tiger AI overlay additions: **Apache License 2.0**
- Original upstream repo (`mihozip/google-workspace-admin-project-workflow`): **MIT License**
- Author: Tiger AI Morris Lu 盧業興
- Original upstream author: mihozip ([GitHub](https://github.com/mihozip))

詳見 / See [`NOTICE.md`](NOTICE.md).
