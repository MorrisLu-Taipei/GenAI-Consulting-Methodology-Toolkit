# NOTICE — TigerAI School Workspace Workflow Overlay

## 1. Original Work / 原作品

This overlay is built on top of:
本 overlay 建立於以下原作品之上：

```
Project:   google-workspace-admin-project-workflow
Author:    mihozip
URL:       https://github.com/mihozip/google-workspace-admin-project-workflow
License:   MIT License
```

Per the original repository's LICENSE file (MIT):
依原 repo 之 LICENSE 檔（MIT 授權）：

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

The original author's copyright notice MUST be preserved when:
使用本 overlay 時，原作者的著作權聲明必須在以下情況保留：

- Forking the repository / Fork 本 repo
- Redistributing in any form (commercial or non-commercial) / 任何形式的再散布（含商業與非商業）
- Including substantial portions in derivative works / 將實質部分納入衍生作品
- Using the original repo's `src/Code.gs`, HTML files, or PHP installer in production / 在實際部署中使用原 repo 的 Apps Script、HTML 檔或 PHP installer

If you fork this overlay, you also fork that obligation. Do not strip the original author's name or remove the LICENSE file from the upstream repo.
若您 fork 本 overlay，您也承接此義務。請勿移除原作者署名或上游 repo 的 LICENSE 檔。

---

## 2. Tiger AI Overlay Additions / Tiger AI 新增部分

The following files in this overlay folder are **NEW WORK** by Tiger AI, not derived from the original repository:
本 overlay 資料夾內的以下檔案為 **Tiger AI 全新撰寫**，非衍生自原 repo：

```
TigerAI-School-Workspace-Workflow-overlay/
├── README.md                          (this folder index)
├── NOTICE.md                          (this file)
├── INSTRUCTIONS_FOR_FORK.md           (overlay-application guidance)
├── TIGERAI_METHODOLOGY_LAYER.md       (L1-L5 mapping)
├── TIGERAI_SCHOOL_L1_L3_GUIDE.md      (school-context implementation)
├── TIGERAI_STAGE_GATES_SCHOOL.md      (Stage Gate design)
├── TIGERAI_HITL_GATES_SCHOOL.md       (HITL Gate design)
├── CHANGELOG.md                       (overlay version log)
└── RELEASE_v0.1.0.md                  (release notes)
```

Tiger AI's contributions to this overlay are released under:
Tiger AI 對本 overlay 的貢獻採以下授權發布：

```
Copyright 2026 Tiger AI Morris Lu 盧業興

Original Author: Tiger AI Morris Lu 盧業興
Role: n8n Taipei 大使 / 臺灣科技大學 智慧製造所博士生 / QUT 昆士蘭科技大學 資工碩士
Source: https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit
        (overlay located at Deliverable/10_Consulting/02_Course_Design/TigerAI-School-Workspace-Workflow-overlay/)

This overlay is licensed under the Apache License, Version 2.0.
You may obtain a copy of the License at:
http://www.apache.org/licenses/LICENSE-2.0
```

---

## 3. License Compatibility / 授權相容性

**MIT (original) + Apache 2.0 (this overlay)** are compatible when used together in this overlay-pattern way, because:
**MIT（原作）+ Apache 2.0（本 overlay）** 在 overlay 模式下相容，理由如下：

1. The overlay does **not** modify, redistribute, or incorporate the original MIT-licensed files. It only **references** them as upstream.
   本 overlay **未**修改、再散布或合併原 MIT 授權檔案，只是**引用**為上游。
2. The two sets of files coexist in separate folders / separate git histories.
   兩組檔案位於不同資料夾 / 不同 git 歷史中。
3. Downstream users who clone the original repo AND apply this overlay must comply with both licenses:
   下游使用者若 clone 原 repo **並**套用本 overlay，須同時遵守兩個授權：
   - For original files: MIT (preserve copyright notice and license)
   - For overlay files: Apache 2.0 (preserve NOTICE, mark modifications, retain license header)

If you redistribute the **combined** work (original + overlay), include BOTH the original's `LICENSE` and this overlay's `NOTICE.md`.
如再散布**合併**作品（原作 + overlay），請同時附原作的 `LICENSE` 與本 overlay 的 `NOTICE.md`。

---

## 4. Citation / 引用建議

When citing this overlay in academic / professional contexts:
在學術或專業場合引用本 overlay 時：

```
Lu, Y.-H. (2026). TigerAI School Workspace Workflow Overlay (v0.1.0)
[Methodology overlay on mihozip/google-workspace-admin-project-workflow].
GenAI Consulting Methodology Toolkit.
https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit
(02_Course_Design/TigerAI-School-Workspace-Workflow-overlay/)
```

The original upstream work should be cited separately:
原上游作品應分別引用：

```
mihozip. (2026). google-workspace-admin-project-workflow.
GitHub. https://github.com/mihozip/google-workspace-admin-project-workflow
```

---

## 5. Disclaimer / 免責聲明

The original repository and this overlay are **independent works under independent authorship**. The presence of this overlay does NOT imply endorsement by, partnership with, or affiliation between mihozip and Tiger AI. Each party speaks only for themselves.
原 repo 與本 overlay 為**獨立作者的獨立作品**。本 overlay 的存在**不**代表 mihozip 與 Tiger AI 之間有任何背書、合作或關係聲明。雙方各自為己。

If you are mihozip and you have concerns about this overlay (positioning, attribution, scope, or any other matter), please open an issue at the Tiger AI Methodology Toolkit repository above; we will respond promptly.
若您是 mihozip 且對本 overlay 有任何疑慮（定位、署名、範圍或其他），請至上述 Tiger AI Methodology Toolkit repository 開 Issue，我們會盡速回覆。
