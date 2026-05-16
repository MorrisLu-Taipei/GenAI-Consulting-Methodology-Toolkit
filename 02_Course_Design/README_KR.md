# 02 Course Design — L1-L5 강의 설계

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. 본 디렉터리의 위치

본 디렉터리는 3 단계 서비스 플로우의 **두 번째 단계: Build (Build)** 입니다. 진단 (`01`) 은 「고객이 어느 레벨, 무엇이 부족한지」 알려줌; 본 디렉터리는 **그 격차를 메우는 실제 강의** 를 담음.

해결하는 문제: **AI 트랜스포메이션은 도구 구매나 강연만으로 성공할 수 없음 — 기업은 L1-L5 를 한 단계씩 거쳐가며 검수 가능 자산을 만들어야 함.** 본 디렉터리는 L1 부터 L5 까지 각 레벨에 완전한 커리큘럼 설계: 강의 목표, 대상, 전제 조건, 내용, 실습 과제, 숙제, 완료 기준, Stage Gate. 각 레벨에서 **검수 가능 산출물** (L1 Prompt Library, L2 Skill, L3 Workflow, L4 Agent, L5 Agent Team) 생성 — 「강의 후 잊혀짐」 이 아님.

본 디렉터리를 쓰는 사람: 강사, AI Champion, IT, 각 레벨 수강생.

## 2. 방법론 내 위치

| 축 | 매핑 |
| --- | --- |
| 3 단계 서비스 플로우 | **Build** — 두 번째 단계 |
| 8 단계 컨설팅 구조 | **Stage 7 To-Be Design** (강의는 솔루션의 구현) |
| L1-L5 성숙도 | 본 디렉터리는 「**고객을 현재 레벨에서 다음 레벨로 끌어올리는**」 강의 본체; L1-L5 **두 축** 가로지름 |
| Engagement Lifecycle | **Delivery — Build** |

> 핵심 원칙 1: **L1-L5 단계 연결 — 하위 레벨의 output 이 다음 레벨의 input.** L1 전원 사용 없으면 L2 용 Skill 축적 없음; L2 Skill 없으면 L3 Workflow 는 빈 관; L3 Workflow 없으면 L4 Agent 는 도구 없음; L4 Agent 없으면 L5 Team 은 멤버 없음. **레벨 점프 금지.**
>
> 핵심 원칙 2: **L1-L5 는 2 축** — 규모 축 (L1 개인 → L2 부서 → L3 부서 간 / 전사, 인간이 AI 감독) 과 AI 자율 축 (L4 AI 슈퍼 어시스턴트 → L5 AI 팀, AI 자율, 인간은 거버너로 후퇴). L3 → L4 가 분기점. [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0 참조. 용어: **Stage Gate = 단계 검수 관문**, **HITL = Human-in-the-Loop (인간이 리뷰 루프 안)**.

## 3. 목표 & 효과

| 목표 | 효과 |
| --- | --- |
| 각 레벨에 완전하고 납품 가능한 커리큘럼 | 강사가 직접 개강 가능, 설계 재작성 불필요 |
| 클래스 내 산출이 검수 가능 자산 | 강의 성과가 조직 역량으로, 「강의 후 잊혀짐」 이 아님 |
| 각 레벨에 Stage Gate | 통과 없이 진행 불가, 레벨 점프 실패 회피 |
| 강의 비율을 진단 점수로 구성 | 고객 자원을 갭에 집중, 낭비 없음 |
| L3/L4 에 PoC 시나리오 라이브러리 + n8n 골격 | 실습에 기성 주제와 template, 제로부터 불필요 |

**본 디렉터리 건너뛰면**: 고객이 도구 사지만 역량 없음, PoC 가 영원히 데모에 머묾, AI 스케일 불가.

## 4. 워크플로 & 로직

```text
01_Assessment 진단 → L 레벨 + 강의 비율 추천
   ↓
COURSE_REQUIREMENTS_AND_COMPANY_PROFILE (전제 조건, 속성, 배포 방식 확인)
   ↓
COURSE_MODULE_MATRIX (L1-L5 아웃라인과 비율 구성 확인)
   ↓
L1_L5_COMPLETE_COURSE_PLAN (총 커리큘럼) + 각 레벨 심층 커리큘럼:
   L1 OPENWEBUI → L2 ANTIGRAVITY → L3 N8N → L4 HERMES → L5 CLAWTEAM
   ↓ 각 레벨
   수업 → 실습 (POC_SCENARIO_SPECS / N8N_WORKFLOW_TEMPLATES 를 주제로)
   → 검수 가능 자산 산출 → Stage Gate 통과 → 다음 레벨로
```

| 단계 | 누가 | 언제 | 입력 | 출력 |
| --- | --- | --- | --- | --- |
| 전제 조건 확인 | 컨설턴트 + 고객 IT | 개강 전 | 진단 결과, 속성 | 개강 전 체크리스트 통과 |
| 강의 비율 구성 | 컨설턴트 | 개강 전 | L 레벨 + 비율 추천 | L1-L5 시간 구성 |
| 개강 (레벨별) | 강사 | Build 단계 | 각 레벨 심층 커리큘럼 | 수강생 실습 성과 |
| 실습 | 수강생 | 각 레벨 클래스 내 | PoC 시나리오 / n8n 골격 | Prompt/Skill/Workflow/Agent/Team |
| Stage Gate 검수 | 컨설턴트 + 고객 매니저 | 각 레벨 후 | 클래스 내 산출 | Gate 통과 → 다음 레벨 |

> 로직: 강의는 「도구 조작 가르치기」 가 아니라 「성숙도에 따라 검증 가능 조직 역량 구축」. 각 레벨은 「전반 산출, 후반 다음 레벨 연결」 구조 따름.

## 5. 파일 설명

### `COURSE_REQUIREMENTS_AND_COMPANY_PROFILE.md`

L1-L5 강의 요구사항 리스트와 회사 속성 조사. 각 레벨의 개강 전제 조건, 회사 기본 데이터, 데이터·리스크 속성, 시스템 정리, 클라우드 AI / Hybrid / 풀 온프레 3 가지 배포 방식의 적용 조건과 강의 노트 정의. 개강 전 「고객 준비됐는가」 확인.

### `COURSE_MODULE_MATRIX.md`

L1-L5 강의 모듈 매트릭스. 각 레벨의 목표, 실습, 숙제 출력, 강의 패키징 (반나절 체험 / 1 일 워크숍 / 2 일 도입 캠프 / 컨설팅 프로젝트), 성숙도별 비율 추천 규칙 한 표에 표시.

### `L1_L5_COMPLETE_COURSE_PLAN.md`

L1-L5 완전 개강 총 기획. 각 레벨의 목표, 내용, 실습, 숙제, 완료 기준과 Stage Gate 총강 요약. 각 레벨 심층 커리큘럼은 아래 5 파일 참조.

### `L1_OPENWEBUI_COURSE_PLAN.md`

L1 Controlled AI Access 심층 커리큘럼. OpenWebUI 공개 playlist 참조, 각 사람 로그인, 개인 채팅 영역, Admin Panel, 계정/역할/그룹/권한, 모델 제어, 데이터 규범, 비디오 참조 지도 포함.

### `L2_ANTIGRAVITY_COURSE_PLAN.md`

L2 Knowledge Codification 심층 커리큘럼. Google Antigravity 3 codelab 참조, Agentic IDE, App Prototype, Unit Test, GCP Serverless Pipeline, Gate 2A-2E 포함. **§7.6** 에 「기존 Agent 라이브러리 (agency-agents) 활용」 모듈. 후반은 L2→L3 Bridge.

### `L3_N8N_TIGERAI_COURSE_PLAN.md`

L3 Workflow Automation 심층 커리큘럼. **§1.1** 에서 L3 를 전반 (n8n 개념과 수동 구축) 과 후반 (AG + TigerAI-n8n-Skill-Pack 자연어 생성, **§5.5**) 으로 분할. TigerAI 채널 n8n / OpenGenie 비디오 참조, Gemini, 멀티모달, Sub-workflow, Data Tables, Webhook, GitHub Backup, Gate 3A-3G 포함.

### `L4_HERMES_AGENT_COURSE_PLAN.md`

L4 Autonomous Agent 심층 커리큘럼. **§2** 는 「Knowledge-grade Agent 7 대 설계 원칙」 (낮 가벼움 / 밤 무거움, 지식 복리 폐쇄 루프, P1>P2, 쓰기-읽기 동일 출처, 도구/LLM 분담, Failure-mode 주도 학습, 왜 RAG 만이 아닌가). 마스터 + 전문 Skill 조합, Wiki 메모리, ingest/query/update, Gate 4A-4E 포함. **본 강의는 개념만 가져옴, 내부 코드 미포함.**

### `L5_CLAWTEAM_COURSE_PLAN.md`

L5 Multi-Agent Organization 심층 커리큘럼. HKUDS/ClawTeam (MIT) 을 구현 플랫폼으로, Team/Workspace/Task/Inbox/Transport 5 계층 아키텍처, git worktree, CLI 핸즈온, 3 대 현지화 시나리오, Gate 5 포함.

### `POC_SCENARIO_SPECS.md`

L3/L4 강의용 PoC 시나리오 라이브러리. 7 카테고리 총 35 개 구현 가능 PoC (Gmail / Sheets / Notion / CRM / API / ERP + 회계 기장), 각각 trigger, 입력, AI step, systems, 출력, 검수, KPI, 인일, n8n 노드 시퀀스 포함. 클래스 실습은 여기서 직접 주제 선택.

### `N8N_WORKFLOW_TEMPLATES.md`

PoC 를 n8n 가져오기 가능 workflow 골격 (JSON) 으로 정리. 30 PoC 골격, 내보내기/가져오기 플로우, 명명 버전 규범, GitHub Backup SOP, 클래스 사용 플로우 포함.

### `*_EN.md`

위 파일들의 영어 sibling 버전.

## 6. 다른 디렉터리와의 대응

| 디렉터리 | 본 디렉터리와의 관계 | 데이터 플로우 |
| --- | --- | --- |
| `01_Assessment` | 진단의 L 레벨 + 강의 비율이 강의 구성 결정 | `01` 비율 → `02` 구성 |
| `00_Overview` | 강의는 스토리의 「Build」 단계 | `00` 스토리 → `02` 구현 |
| `03_Consulting_Report` | 클래스 내 산출과 관찰을 8 단계 컨설팅 보고서에 기록 | `02` 클래스 내 산출 → `03` 보고서 |
| `04_Scenarios` | 클래스 데모 주제는 케이스 인덱스에서 선택; PoC 가 케이스로 전환 가능 | `04` 케이스 ↔ `02` 강의 주제 |
| `06_Delivery` | 강의는 engagement lifecycle 의 Delivery — Build 에 대응; 산출물이 납품 패키지 검수로 | `02` 산출 → `06` 검수 |
| `90_References` | 각 레벨 강의의 제3자 인용 (OpenWebUI / Antigravity / n8n-Skill-Pack / ClawTeam / agency-agents) | `90` 인용 → `02` |

## 7. 일반적 사용 시나리오

- **강의 구성**: 진단의 강의 비율을 가져옴 → `COURSE_MODULE_MATRIX.md` 로 시수 구성 → 대응 심층 커리큘럼 개강.
- **L3 개강**: `L3_N8N_TIGERAI_COURSE_PLAN.md` 전반에서 개념 교수, 후반에서 AG+Skill Pack; 실습 주제는 `POC_SCENARIO_SPECS.md` 에서, 골격은 `N8N_WORKFLOW_TEMPLATES.md` 에서 가져옴.
- **수강생이 실습 주제 찾기**: 자기 부서와 L 레벨에 따라 `POC_SCENARIO_SPECS.md` 또는 `04_Scenarios/LLM_APPS_CASE_INDEX.md` 에서 선택.
- **검수**: 각 레벨 후 `01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md` 와 대조하여 Stage Gate 통과.

---

## ⭐ Cross-Topic Quick References: 5 가지 핵심 주제, 어디서 찾는가

방법론 전체에는 모든 디렉터리를 관통하는 5 가지 주동맥이 있습니다. 본 디렉터리가 각각에 어떻게 연결되는지:

| Cross-Topic | 주 위치 | 본 디렉터리가 어떻게 연결되는가 |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 3 엔진 공독** | Root [`README_KR.md`](../README_KR.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | **L2 Knowledge Codification 강의가 3 엔진을 직접 가르침** — Antigravity / Codex / Claude Code 는 L2 수강생의 도구; 클래스에서 3 엔진 동원하여 데모 + Skill 캡슐화 + 크로스파일 테스트 |
| 🎓 **학술 기반 (7 대 기둥)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **L1-L5 5 계층 아키텍처는 Capability Maturity (Rosemann/CMMI) 에 기반**; 레벨 점프 금지 철칙은 Absorptive Capacity (Cohen & Levinthal 1990) 에 기반; L4 Hermes 7 대 설계 원칙은 Sociotechnical & Knowledge Compounding 에 대응 |
| 📚 **L1-L5 강의 교육** | [`../02_Course_Design/`](본 디렉터리) ｜ [`L1_L5_COMPLETE_COURSE_PLAN.md`](L1_L5_COMPLETE_COURSE_PLAN.md) | **본 디렉터리는 L1-L5 강의 본체** — 5 개 독립 심층 커리큘럼 (L1 OPENWEBUI / L2 ANTIGRAVITY / L3 N8N / L4 HERMES / L5 CLAWTEAM) + COURSE_MODULE_MATRIX 비율 구성 + POC_SCENARIO_SPECS 35 실습 주제 |
| 🔁 **컨설팅 / 8 단계 + Phase A→B→C 폐쇄 루프** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **클래스 내 산출이 Phase B 보고서에 들어감** (14 장의 「강의 관찰」 챕터가 됨) + Phase C 분기 레이더 추적; 각 레벨 Stage Gate 가 컨설팅 폐쇄 루프의 Gate A/B/C 에 대응 |
| 📖 **참고 자료 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | **L1 → OpenWebUI** ｜ **L2 → Antigravity / Codex / Claude Code + agency-agents** ｜ **L3 → n8n + TigerAI-n8n-Skill-Pack** ｜ **L4 → nousresearch/hermes-agent** ｜ **L5 → HKUDS/ClawTeam**. 완전한 appreciation cards 는 [`../90_References/README.md`](../90_References/README.md) §2.1-2.3 참조 |
