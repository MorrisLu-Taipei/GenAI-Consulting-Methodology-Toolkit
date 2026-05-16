# 01 Assessment — AI 성숙도 진단

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. 본 디렉터리의 위치

본 디렉터리는 3 단계 서비스 플로우의 **첫 단계: 진단 (Diagnose)** 입니다. 컨설팅 업무의 가장 근본적인 문제를 해결합니다: **「기업이 'AI 를 쓴다'고 하지만 실제 어느 레벨인가? 무엇이 부족한가? 어디부터 채워야 하는가?」**

객관적 진단이 없으면 컨설턴트는 고객의 주관적 묘사로만 강의를 구성할 수밖에 없음 — 결과는 종종 레벨 점프 (L1 전원 사용도 안 됐는데 L4 Agent 를 만들고 싶어함) 또는 우선순위 오류 (거버넌스가 부족한데 도구만 계속 추가). 본 디렉터리는 3 가지 길이의 설문 + 채점 모델 + 회사 속성 조사로 「모호한 느낌」을 **객관적·정량적·비교 가능한 L1-L5 점수와 6 차원 갭 레이더** 로 변환.

본 디렉터리를 쓰는 사람: Sales (10 문항 버전으로 리드 개발기 스크리닝), 컨설턴트 (25/50 문항 버전으로 강의 전·면담 전 정리), IT/AI Champion (회사 속성 설문).

## 2. 방법론 내 위치

| 축 | 매핑 |
| --- | --- |
| 3 단계 서비스 플로우 | **진단 (Diagnose)** — 첫 단계 |
| 8 단계 컨설팅 구조 | **Stage 1 현황 파악** (진단 결과는 Stage 1 의 핵심 입력) |
| L1-L5 성숙도 | 본 디렉터리는 「**고객이 어느 레벨인지 판정**」하는 도구 |
| Engagement Lifecycle | **Sales — Lead Qualification (10 문항) / Discovery (25/50 문항)** |

## 3. 목표 & 효과

| 목표 | 효과 |
| --- | --- |
| 주관적 추측을 객관적 점수로 대체 | 컨설턴트가 강의 구성 근거 보유, 감각이 아님 |
| 6 차원 갭 발견 (도구/지식/프로세스/통합/Agent/거버넌스-ROI) | 고객이 어디서 강하고 약한지 파악 |
| 직접 3 가지 추천 도출 | 강의 비율 + 배포 방식 + PoC 시나리오, 한 번에 완성 |
| 3 가지 설문 길이로 3 개 영업 단계 대응 | 리드 개발, 강의 전, 면담 전 — 각자 적절한 도구 |
| 자동화 가능 | 설문 → 채점 → 보고서 전 자동, 컨설턴트는 해석만 |

**본 디렉터리를 건너뛰면**: 강의 비율 추측, 고객 기대 관리 불가 (L5 케이스를 가리키며 "이게 갖고 싶다"고 하지만 자기가 L2 인지 모름), 컨설팅 보고서에 객관적 출발점 없음.

## 4. 워크플로 & 로직

```text
10 문항 빠른 설문 (리드 개발기, 3 분)
   → 리드 적격 판정 + 초기 L 레벨 위치
25 문항 설문 (강의 전, 8 분, 고객 매니저 작성)
   → 6 차원 점수 + 레이더 차트
50 문항 설문 (컨설턴트 면담 전, 20 분, IT/AI Champion)
   → 완전 정리 + 오픈 질문
회사 속성 설문 (35 문항)
   → JSON Profile Bundle (시스템 / 리스크 / 배포 선호 / 예산)
        ↓ Merge
   자동 채점 → L1-L5 레벨 + 6 차원 레이더
        ↓ 도출
   ① 추천 강의 비율  ② 추천 배포 방식  ③ 추천 PoC 시나리오
```

| 단계 | 누가 | 언제 | 입력 | 출력 |
| --- | --- | --- | --- | --- |
| 10 문항 퀵스크린 | Sales | 리드 개발기 | 잠재 고객 | 적격 판정 + 초기 L 레벨 |
| 25 문항 강전 진단 | 고객 매니저 그룹 | L1 개강 1 주 전 | 25 문항 설문 | 6 차원 점수 |
| 50 문항 완전 정리 | 고객 IT / AI Champion | 컨설턴트 면담 전 | 50 문항 + 회사 속성 설문 | 완전 Profile Bundle |
| 자동 채점 | 시스템 (Sheets/Notion/n8n) | 설문 제출 후 | 설문 응답 | L 레벨 + 레이더 + 3 추천 |
| 해석 | 컨설턴트 | 자동 보고서 수령 후 | 자동 보고서 | 맞춤형 제안 방향 |

> 로직: 설문은 단지 **입력**; 진짜 출력은 「**L 레벨 + 6 차원 갭 + 3 추천**」. 이 세 개는 각각 — 강의 비율 → `02_Course_Design`; 배포 방식 → `03` 의 To-Be Design; PoC 시나리오 → `04_Scenarios` 의 케이스 인덱스로 전달. 진단은 종점이 아니라 후속 3 디렉터리를 「점등」하는 스위치.

## 5. 파일 설명

### `AI_MATURITY_QUESTIONNAIRE.md`

10 / 25 / 50 문항 3 가지 길이의 AI 성숙도 설문 본체. 10 문항 버전은 Sales 빠른 판정용; 25 문항 버전은 차원별 4-5 문항, 강의 전용; 50 문항 버전은 배포 방식과 시스템 정리 추가, 컨설턴트 면담 전용. 3 버전 공통: 0-4 점 척도와 6 차원 아키텍처.

### `AI_MATURITY_SCORING_MODEL.md`

채점 로직과 판정 규칙. 포함: 6 차원 (도구 사용, 지식 축적, 프로세스 표준화, 시스템 통합, Agent 응용, 거버넌스-ROI) 채점 계산, 총점이 L1-L5 에 대응하는 임계값, **주 성숙도 vs 부분 성숙도** 판단 (왜 어떤 부서가 부분 L4 이지만 전체 L2 인지), 배포 방식과 강의 비율 추천 규칙.

### `AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`

L1-L5 각 단계의 Definition of Done, Deliverables, Evidence, Owner, Stage Gate, Fail Condition, Next Level Entry Criteria. 「각 레벨 '완료'가 어떻게 보이는지, 무엇을 evidence 로 증명하는지」 정의 — Stage Gate 검수의 근거.

### `FILLABLE_QUESTIONNAIRE.md`

10/25/50 문항을 작성 가능 폼으로 변환하는 렌더 스펙 — 문항 타입 (radio / 0-4 scale / 멀티 선택 / 단답), 페이지 분할, skip logic, 제출 페이지와 「다음 무슨 일이 일어날까」 페이지, Google Form / Tally / Notion Form 3 플랫폼 렌더 힌트 포함.

### `COMPANY_PROFILE_QUESTIONNAIRE.md`

35 문항 회사 속성 설문, 6 섹션 (Profile / Systems / Risk / Deployment / Course / Budget). 출력: JSON Profile Bundle, **도출 규칙** 포함: Bundle 에서 자동으로 배포 방식 추천, 강의 비율 미세 조정, PoC 시나리오 추천 도출. 성숙도 설문과 `submission_id` 로 연결.

### `AI_DIAGNOSIS_SHEETS_SCHEMA.md`

진단 전체를 자동화하는 구현 스키마. 3 플랫폼: Google Sheets (채점 수식, 조건부 서식, Apps Script), Notion (4 개 database 구조와 formula), n8n (13 노드 자동 진단 플로우, idempotency 포함). 설문 → 채점 → 보고서 생성 → 컨설턴트 알림, 전 자동.

### `*_EN.md`

위 파일들의 영어 sibling 버전.

## 6. 다른 디렉터리와의 대응

| 디렉터리 | 본 디렉터리와의 관계 | 데이터 플로우 |
| --- | --- | --- |
| `00_Overview` | 진단은 스토리의 첫 단계 | `00` 스토리 → `01` 구현 |
| `02_Course_Design` | 진단의 「L 레벨 + 강의 비율」이 강의 구성을 직접 결정 | `01` 비율 → `02` 구성 |
| `03_Consulting_Report` | 진단 결과는 8 단계 Stage 1 의 입력; 보고서가 진단 점수와 레이더 인용 | `01` 점수 → `03` 보고서 |
| `04_Scenarios` | 진단 후 L 레벨에 따라 `LLM_APPS_CASE_INDEX.md` 로 PoC 후보 선정 | `01` L 레벨 → `04` 케이스 선정 |
| `06_Delivery` | 진단은 engagement lifecycle 의 Sales 단계 대응 | `01` ↔ `06` Sales 단계 |
| `90_References` | 채점 모델의 방법론 근거 | `90` 근거 → `01` |

## 7. 일반적 사용 시나리오

- **영업 개발**: 잠재 고객이 10 문항 버전 작성 → 24 시간 내 자동 보고서 → Sales 가 L 레벨 위치를 가지고 상담.
- **강의 전 준비**: 개강 1 주 전 25 문항 버전을 고객 매니저 그룹에 발송 → 컨설턴트가 6 차원 레이더 받고 강의 비율 조정.
- **컨설턴트 면담 전**: IT/AI Champion 이 50 문항 + 회사 속성 설문 작성 → 컨설턴트가 면담 1 시간 전에 완전 Profile Bundle 을 브리프로 수령.
- **스케일링**: `AI_DIAGNOSIS_SHEETS_SCHEMA.md` 로 고객 n8n 에 자동 진단 플로우 deploy, 컨설턴트는 최종 해석만.

---

## ⭐ Cross-Topic Quick References: 5 가지 핵심 주제, 어디서 찾는가

방법론 전체에는 모든 디렉터리를 관통하는 5 가지 주동맥이 있습니다. 본 디렉터리가 각각에 어떻게 연결되는지:

| Cross-Topic | 주 위치 | 본 디렉터리가 어떻게 연결되는가 |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 3 엔진 공독** | Root [`README_KR.md`](../README_KR.md) §🌟 ｜ [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`../07_AI_Contributions/`](../07_AI_Contributions/) | 설문은 Antigravity `/diagnose` 로 인터랙티브 작성 가능; AI_DIAGNOSIS_SHEETS_SCHEMA 가 설문 자동화 (n8n + Google Sheets + Notion); 진단 결과는 Codex `/consistency-review` 로 크로스 파일 정렬에 흘려보낼 수 있음 |
| 🎓 **학술 기반 (7 대 기둥)** | [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **본 디렉터리의 [`BARS_RUBRICS.md`](BARS_RUBRICS.md) 가 inter-rater reliability 에 대응** (Smith & Kendall 1963); 6 차원 진단은 Capability Maturity (Rosemann/CMMI) + Absorptive Capacity (Cohen & Levinthal 1990) + Sociotechnical Trust 에 대응 |
| 📚 **L1-L5 강의 교육** | [`../02_Course_Design/`](../02_Course_Design/) | **진단의 L 레벨 판정 + 6 차원 레이더 + 강의 비율 추천** 이 `02` 의 강의 구성을 직접 결정 — `02` 의 「강의 전 필수」 |
| 🔁 **컨설팅 / 8 단계 + Phase A→B→C 폐쇄 루프** | [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **진단 = Phase A 의 핵심 입력** (Stage 1 현황 파악 + Stage 2 Reference Model 레이더 서명); Phase C 분기 레이더 회고는 「**진단 재실행**」 — 구조가 실제로 둥글어졌나? 진단은 입구이자 폐쇄 루프의 반증 메커니즘 |
| 📖 **참고 자료 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | 채점 모델은 BARS (Smith & Kendall 1963) + 7 대 이론 기둥 참조; Pilot Study 18-24 개월 실증 계획은 [`../90_References/PILOT_STUDY_PROTOCOL.md`](../90_References/PILOT_STUDY_PROTOCOL.md) 참조 (설문의 Cohen's κ ≥ 0.60 목표 검증) |
