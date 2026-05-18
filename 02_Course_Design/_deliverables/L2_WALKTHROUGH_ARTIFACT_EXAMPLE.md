# L2 Walkthrough Artifact 範例 / L2 Walkthrough Artifact Example

> 對應課程 / Course: [L2_ANTIGRAVITY_COURSE_PLAN.md](../L2_ANTIGRAVITY_COURSE_PLAN.md) §3.4 + §6.2 Builder
> 版本 / Version: 範本 v1.0（學員交付 + 講師審查用）/ Template v1.0 (for learner submission + instructor review)
> 授權 / License: Apache 2.0

## 0. 什麼是 Walkthrough Artifact

Antigravity 的核心特色：每個 Agent task 都會產生 **可重現的證據鏈**——learner / reviewer 看完這份 artifact，就能完整理解 Agent **做了什麼、為什麼、結果如何**，不必看 code 也能審查。
Antigravity's core feature: every Agent task produces a **reproducible evidence chain** — by reading this artifact, learner / reviewer can fully understand **what / why / how** the Agent did, without reading code.

本檔示範一個合格的 Walkthrough Artifact 長什麼樣。/ This file shows what a passing Walkthrough Artifact looks like.

---

## 1. Walkthrough 必備 6 欄 / Required 6 fields

| # | 欄位 / Field | 內容 / Content |
|---|---|---|
| 1 | **Task statement** | 1 句話描述任務 / 1-sentence task description |
| 2 | **Agent plan** | Agent 自己拆的步驟（含被學員修改的部分）/ Agent's own decomposition (incl. learner edits) |
| 3 | **Execution log** | 每一步的時間 / 動作 / 結果 / Per-step time / action / outcome |
| 4 | **Decisions made** | Agent 做了哪些選擇 + 為什麼 / Agent's choices + why |
| 5 | **Issues encountered** | 失敗、重試、debug 過程 / Failures, retries, debug |
| 6 | **Final artifact** | 最終產出 + 驗證證據 / Final output + verification evidence |

---

## 2. 範例 Walkthrough：建立 Flask hello-world / Example: Build Flask hello-world

### 2.1 Task statement

> 用 Antigravity Agent 建立一個 Flask app skeleton 含 health endpoint，並用 pytest 驗證。
> Use Antigravity Agent to build a Flask app skeleton with health endpoint, validated by pytest.

### 2.2 Agent plan

```text
Step 1: Create project directory structure
Step 2: Generate app.py (Flask factory pattern)
Step 3: Generate routes/health.py
Step 4: Generate requirements.txt
Step 5: Generate tests/test_health.py
Step 6: Run pytest to verify
Step 7: Generate README.md
```

**學員修改 / Learner edit：** Step 2 改用 application factory pattern（原來 Agent 提議用 single-file），理由：未來好擴充。
**Learner edit:** Step 2 changed to application factory pattern (Agent originally proposed single-file). Reason: easier to extend.

### 2.3 Execution log

| # | 時間 / Time | 動作 / Action | 結果 / Outcome |
|---|---|---|---|
| 1 | 10:01 | `mkdir -p flask-app/routes flask-app/tests` | ✅ |
| 2 | 10:02 | Write `flask-app/app.py` (28 lines) | ✅ |
| 3 | 10:03 | Write `flask-app/routes/__init__.py` (empty) | ✅ |
| 4 | 10:03 | Write `flask-app/routes/health.py` (10 lines) | ✅ |
| 5 | 10:04 | Write `flask-app/requirements.txt` | ✅ |
| 6 | 10:05 | Write `flask-app/tests/conftest.py` (12 lines) | ✅ |
| 7 | 10:05 | Write `flask-app/tests/test_health.py` (8 lines) | ✅ |
| 8 | 10:06 | `pip install -r requirements.txt` | ✅ 18 packages |
| 9 | 10:07 | `pytest` | ❌ ImportError: cannot import `health_bp` |
| 10 | 10:08 | Debug: routes/__init__.py needs to expose `health_bp` | — |
| 11 | 10:08 | Write `flask-app/routes/__init__.py` (1 line: `from .health import health_bp`) | ✅ |
| 12 | 10:09 | `pytest` | ✅ 1 passed in 0.12s |
| 13 | 10:10 | Write `flask-app/README.md` (30 lines) | ✅ |

### 2.4 Decisions made

1. **Factory pattern over single-file** — easier to test, follows Flask docs recommended pattern.
2. **gunicorn over Flask dev server** — production-ready out of the box.
3. **pytest fixture for test client** — DRY, reusable across future tests.
4. **Python 3.11-slim Docker base** — small image (~150MB), modern enough for Flask 3.x.

### 2.5 Issues encountered

| # | Issue | Resolution |
|---|---|---|
| 1 | `pytest` fails with ImportError on first run | Added explicit re-export in `routes/__init__.py` |
| 2 | Agent originally proposed `app.run()` in production | Learner asked Agent to switch to gunicorn |

### 2.6 Final artifact

```text
flask-app/
├── app.py                   ✅
├── requirements.txt         ✅
├── routes/__init__.py       ✅
├── routes/health.py         ✅
├── tests/conftest.py        ✅
├── tests/test_health.py     ✅
└── README.md                ✅
```

**Verification evidence:**

```bash
$ pytest -v
================ test session starts ================
tests/test_health.py::test_health PASSED        [100%]
================ 1 passed in 0.12s ==================

$ python app.py &
$ curl http://localhost:8080/health
{"status": "ok"}
```

---

## 3. 自審 Checklist / Self-review Checklist

學員交件前自審 / Self-check before submission：

- [ ] 6 欄都有填 / All 6 fields filled
- [ ] Execution log 含時間戳 / Execution log includes timestamps
- [ ] Decisions 有寫「為什麼」不只「做什麼」 / Decisions include "why" not just "what"
- [ ] Issues 誠實記錄（含失敗）/ Issues honestly recorded (incl. failures)
- [ ] 最終 artifact 有驗證證據（screenshot / command output）/ Final artifact has verification (screenshot / command output)
- [ ] 非原作者讀完能理解整個流程 / Non-author readers can follow the whole flow

---

## 4. Reviewer Checklist

講師 / 同儕審查時看 / What instructor / peer checks：

- [ ] Plan 合理 + 可重現 / Plan reasonable + reproducible
- [ ] Log 完整（無時間斷層）/ Log complete (no time gaps)
- [ ] Decisions 有思考深度（不只「Agent 建議」）/ Decisions show depth (not just "Agent suggested")
- [ ] Issues 真實（包含失敗才可信）/ Issues realistic (includes failures = credible)
- [ ] Final artifact 可驗證 / Final artifact verifiable
- [ ] 整體：非原作者能用同樣步驟產出同樣結果 / Overall: non-author can reproduce same outcome
