# 04 Scenarios — 시나리오, 케이스 & 케이스 인덱스

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

> ⚠️ **중요한 학술 무결성 선언 / Important Academic Integrity Disclaimer**
>
> **본 디렉터리의 7 개 SAMPLE_CLIENT_CASE_*.md 케이스 (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education) 와 명명된 모든 주인공 (예: `00_Overview/CLIENT_JOURNEY_STORY.md` 의 Ming) 은 모두 AI 생성 가상 케이스이며, 실제 고객 데이터가 아닙니다.**
>
> - **용도**: 교육 데모, 방법론 설명, Stage 1-8 도구표 응용 연습
> - **제한**: 모든 숫자 (시간, ROI, 인월, 예산, KPI) 는 예시일 뿐, **대외 홍보, 계약상 약속, 학술적 실증 증거로 사용해서는 안 됨**
> - **에비던스 레벨**: [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md) Tool 8.9 에 따라, 본 디렉터리 케이스는 **L0 (AI-Simulated Teaching Case)**, L1 자기 평가 설문보다 낮음
> - **실제 longitudinal 케이스** 는 [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) 의 18-24 개월 실증 연구 완료 후에만 교체

## 1. 본 디렉터리의 위치

본 디렉터리는 전체 방법론의 **소재 라이브러리와 에비던스 라이브러리** 입니다. `01`-`03`, `05`, `06` 은 「방법과 프로세스」; 본 디렉터리는 「**방법론 구현 시 실제 시나리오, 케이스, 선택 가능한 케이스 제공**」.

해결하는 문제: **AI 도입의 가장 큰 장벽은 「할 줄 모름」 이 아니라 「무엇이 가능한지, 다른 사람은 어떻게 하는지, 도입 후 어떻게 보일지 모름」.** 본 디렉터리는 4 가지 소재 제공: (1) 역할/부서별 **시나리오 스토리** (고객 「자기 투영」), (2) 케이스의 **작성 표준과 통제표** (컨설턴트가 일관된 케이스 작성), (3) 7 산업 **완전 데모 케이스** (설문에서 Roadmap 까지), (4) 150+ 실제 LLM 응용 **케이스 인덱스** (L 레벨과 부서 2 축으로 빠른 검색).

본 디렉터리를 쓰는 사람: 컨설턴트 (Discovery 에서 시나리오 · 케이스 인덱스로 PoC 선정), Sales (케이스로 가치 입증), 강사 (케이스를 데모 주제로), 고객 (완전 케이스로 「도입 후 어떻게 되는지」 이해).

## 2. 방법론 내 위치

| 축 | 매핑 |
| --- | --- |
| 3 단계 서비스 플로우 | **전 과정 가로지름** — Discovery 에서 시나리오 사용, Build 에서 케이스를 주제로, Deliver 에서 케이스로 입증 |
| 8 단계 컨설팅 구조 | 주로 **Stage 1 As-Is Snapshot (현황 시나리오), Stage 3 Best Practice Integration (업계 베스트 실천 벤치마크)** 지원 |
| L1-L5 성숙도 | 케이스 인덱스가 각 케이스를 L 레벨에 매핑 |
| Engagement Lifecycle | Sales (Discovery 자기 투영) + Build (데모 주제) |

## 3. 목표 & 효과

| 목표 | 효과 |
| --- | --- |
| 역할/부서별 시나리오 스토리 제공 | 고객이 「자기 투영」 가능, Discovery 가 더 빨리 초점 |
| 케이스 작성 표준과 통제표 | 컨설턴트가 구조 일관·검증 가능 케이스 작성 |
| 7 산업 완전 데모 케이스 | 고객이 「도입 후 전경」 봄; 신입 컨설턴트에 템플릿 |
| 150+ LLM 응용 인덱스 (2 축 검색) | 고객/컨설턴트가 「L 레벨」 또는 「부서」 로 즉시 검색 |
| 크로스 레벨 기대 관리 | 고객이 L5 케이스 가리키면 인덱스로 「당신은 L2, 먼저 보충해야」 지적 |

**본 디렉터리 건너뛰면**: 고객이 「무엇이 가능한지」 개념 없음, PoC 선정이 추측, 케이스 품질 일관성 없음, 크로스 레벨 기대 관리 불가.

## 4. 워크플로 & 로직

```text
Discovery 단계
   → CUSTOMER_SCENARIO_LIBRARY (역할별 시나리오, 고객 자기 투영)
   → LLM_APPS_CASE_INDEX (L 레벨 + 부서로 「고객이 공감하는」 케이스 선택)
   → 선정 케이스 → PoC 후보

강의 / 제안 단계
   → SAMPLE_CLIENT_CASE_* (동일 산업 완전 케이스를 고객에게 보임)
   → LLM_APPS_CASE_INDEX (클래스 데모 주제, 연습 주제)

컨설턴트가 새 케이스 작성 시
   → CASE_WRITING_STANDARD (작성 표준)
   → CASE_CONTROL_TABLES (통제표, 복붙 작성)
```

| 단계 | 누가 | 언제 | 입력 | 출력 |
| --- | --- | --- | --- | --- |
| 고객 자기 투영 | 컨설턴트 | Discovery | 시나리오 스토리 라이브러리 | 고객이 인정하는 페인 포인트 |
| PoC 후보 선정 | 컨설턴트 | 진단 후 | L 레벨 + 부서 → 인덱스 | PoC 후보 리스트 |
| 완전 케이스 고객 제시 | Sales / 컨설턴트 | 제안 | 동일 산업 sample case | 고객이 전경 이해 |
| 새 케이스 작성 | 컨설턴트 | 프로젝트 종료 후 | 작성 표준 + 통제표 | 새 sample case |

> 로직: 시나리오 스토리는 「**공감 유발**」 (고객이 「맞아, 바로 그거」 라고 말함); 케이스 인덱스는 「**소재 즉시 선택**」 (L 레벨/부서로 즉시 검색); 완전 데모 케이스는 「**전경 제시**」 (설문에서 Roadmap); 작성 표준은 「**일관성 보증**」 (새 케이스 품질 안정).

## 5. 파일 설명

### 시나리오와 표준

| 파일 | 용도 |
| --- | --- |
| `CUSTOMER_SCENARIO_LIBRARY.md` | 역할/부서별 시나리오 스토리: CEO, COO, IT, HR 와 Sales, Customer Service, Marketing, Operations, Finance, HR, IT 부서; 각 스토리에 Before, Trigger, AI Flow, Systems, Output, KPI 포함. |
| `CASE_WRITING_STANDARD.md` | 케이스 작성 표준, L1-L5 의 Input / Process / Output / Evidence 와 검증 가능 납품물의 작성법 규정. |
| `CASE_CONTROL_TABLES.md` | 케이스 통제표, 평가 활동, L1-L5 IPOE, Evidence, Stage Gate, 리스크 거버넌스, Deliverables 검수를 복붙 가능. |
| `INDUSTRY_SCENARIOS.md` | 5 산업 추천 시나리오 (소매/교육/물류/소프트웨어/전문 서비스), 산업별: 소개, L1-L5 베이스라인, Top-10 시나리오, 리스크 거버넌스, 30 일 Quick Win, Anti-Patterns. |

### 완전 데모 케이스 (고객 모두 코드네임)

| 파일 | 케이스 |
| --- | --- |
| `SAMPLE_CLIENT_CASE_MANUFACTURING.md` | R&D 제조업 완전 케이스 |
| `SAMPLE_CLIENT_CASE_HOSPITAL.md` | 병원 / 의료 기관 (고민감 데이터, 풀 온프레, 사람 리뷰) |
| `SAMPLE_CLIENT_CASE_MARKETING_AGENCY.md` | 마케팅 에이전시 (코드네임: 에이전시 M) |
| `SAMPLE_CLIENT_CASE_B2B_SALES.md` | B2B 산업 장비 딜러 (코드네임: 산업 장비 B), RFP · CRM 거버넌스 · L5 Pre-RFP Team 포커스 |
| `SAMPLE_CLIENT_CASE_FINANCIAL.md` | 금융업 (코드네임: 지방 은행 F), 풀 온프레, 이중 리뷰 |
| `SAMPLE_CLIENT_CASE_GOVERNMENT.md` | 정부 기관 (코드네임: 시 디지털 국 G), 풀 온프레, 삼중 리뷰 |
| `SAMPLE_CLIENT_CASE_EDUCATION.md` | 교육 기관 (코드네임: 테크 대학 E), Hybrid, 학술 윤리 |

> 각 케이스는 완전 플로우: 설문 결과 → L 레벨 판정 → 강의 비율 → 클래스 내 산출 → 8 단계 분석 → 진단 보고서 요약 → 30/60/90 Roadmap → ROI → 리스크 거버넌스.

### L5 구현과 케이스 인덱스

| 파일 | 용도 |
| --- | --- |
| `CLAWTEAM_WALKTHROUGH.md` | ClawTeam (HKUDS, MIT) 으로 부서 간 Agent Team 완전 walkthrough (제조업 QA Team), 환경 설정, 태스크 체인, Human Gate, Gate 5 매핑 포함. |
| `LLM_APPS_CASE_INDEX.md` | **LLM 응용 케이스 인덱스 (멀티 소스)**. 150+ 실 LLM app, **2 가지 검색 축**: ① L1-L5 / 강의별 ② 기업 부서/프로세스별 (엔지니어링/재무/인사/영업/마케팅/R&D/오퍼레이션/고객 서비스/법무/데이터/디자인/경영진). 소스: awesome-llm-apps (Apache-2.0), ai-engineering-hub (MIT). |

### `*_EN.md`

일부 파일의 영어 sibling 버전.

## 6. 다른 디렉터리와의 대응

| 디렉터리 | 본 디렉터리와의 관계 | 데이터 플로우 |
| --- | --- | --- |
| `01_Assessment` | 진단의 L 레벨이 어떤 케이스 선택할지 결정 | `01` L 레벨 → `04` 케이스 필터 |
| `02_Course_Design` | 케이스/PoC 인덱스는 클래스 데모와 연습 주제의 소스 | `04` 케이스 ↔ `02` 강의 주제 |
| `03_Consulting_Report` | 8 단계 Stage 3 업계 베스트 실천 벤치마킹에서 케이스 인용 | `04` 케이스 → `03` Stage 3 |
| `05_Sales` | 완전 케이스와 시나리오는 Sales 소재의 입증 | `04` 케이스 → `05` 입증 |
| `00_Overview` | 시나리오 스토리는 스토리의 소재 | `04` ↔ `00` |
| `90_References` | 케이스 인덱스의 제3자 인용 (awesome-llm-apps / ai-engineering-hub) | `90` 인용 → `04` |

## 7. 일반적 사용 시나리오

- **Discovery 자기 투영**: `CUSTOMER_SCENARIO_LIBRARY.md` 를 고객 역할에 대응, 「어떤 스토리가 당신과 비슷한가?」 질문.
- **PoC 선정**: L 레벨 진단 후, `LLM_APPS_CASE_INDEX.md` §3 L 레벨별 또는 §4 부서별, 고객이 공감하는 3-5 개 선택.
- **제안 입증**: 제조업 고객에게 `SAMPLE_CLIENT_CASE_MANUFACTURING.md` 보여서 완전 도입 전경 시연.
- **크로스 레벨 기대 관리**: 고객이 L5 케이스 지목 → 인덱스로 그의 L 레벨과 전제 강의 지적.
- **새 케이스 작성**: 프로젝트 종료 후 `CASE_WRITING_STANDARD.md` + `CASE_CONTROL_TABLES.md` 에 따라 새 sample case 로 작성.

---

## ⭐ Cross-Topic Quick References: 5 가지 핵심 주제, 어디서 찾는가

방법론 전체에는 모든 디렉터리를 관통하는 5 가지 주동맥이 있습니다. 본 디렉터리가 각각에 어떻게 연결되는지:

| Cross-Topic | 주 위치 | 본 디렉터리가 어떻게 연결되는가 |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 3 엔진 공독** | Root [`README_KR.md`](../README_KR.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | 케이스는 Claude Code Tier 2 워크플로로 실행 가능: `/simulate-engagement` 으로 완전한 6 주 컨설팅 안건 시뮬레이션, `/parallel-perspectives` 로 6 이해관계자 관점, `/devil-pair-debate` 로 가치관 전제 토론 |
| 🎓 **학술 기반 (7 대 기둥)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | 케이스의 ROI 논술은 **Real Options** 에 대응 (왜 Phase 1 NPV ≈ 0 인데도 투자 가치 있음); To-Be Design 은 **Task-Technology Fit** 에 대응 (어느 태스크가 L4 로, 어느 것이 L2 에 머물러야 하는지) |
| 📚 **L1-L5 강의 교육** | [`../02_Course_Design/`](../02_Course_Design/) | LLM Apps Case Index 가 L 레벨로 분류, 직접 PoC 로 선택 가능; `POC_SCENARIO_SPECS.md` + `N8N_WORKFLOW_TEMPLATES.md` 가 케이스를 L3 클래스 핸즈온 주제로 변환 |
| 🔁 **컨설팅 / 8 단계 + Phase A→B→C 폐쇄 루프** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **케이스는 Phase A Discovery 의 「자기 투영」 소재** (고객이 「맞아, 바로 그거」 라고 말함); 업계 베스트 실천이 Stage 3 에 매핑; 7 개 완전 sample case 가 Phase B 보고서의 템플릿 |
| 📖 **참고 자료 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | LLM Apps Case Index 소스: `Shubhamsaboo/awesome-llm-apps` (Apache-2.0) + `patchy631/ai-engineering-hub` (MIT), 완전 appreciation cards 는 [`../90_References/README.md`](../90_References/README.md) §2.4 참조; ClawTeam Walkthrough 는 `HKUDS/ClawTeam` (MIT) 에서 |
