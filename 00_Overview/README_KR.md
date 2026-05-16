# 00 Overview — 프로그램 개요 & 진입점

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. 본 디렉터리의 위치

본 디렉터리는 전체 **AI Consulting Methodology Toolkit** 의 **유일한 진입점** 입니다. 「도구」나 「산출물」을 두지 않고 두 가지만 둡니다: **방법론의 스토리** 와 **방법론의 상태**.

이 레포를 처음 만나는 모든 사람 — 컨설턴트가 방법론을 배우거나, 고객이 구매를 평가하거나, 신입이 온보딩하거나, 리뷰어가 감사하거나 — 모두 여기서 시작해야 합니다. 먼저 여기서 「방법론이 무엇인가, 왜 이렇게 설계됐는가, 현재 어디까지 왔는가」의 전체 그림을 구축한 후, 기능 디렉터리 `01`-`06` 으로 진입하세요. 나무를 보고 숲을 놓치지 않게.

본 디렉터리가 해결하는 문제: **명확한 입구와 상태가 없으면, 사용자는 길을 잃고, 방법론을 오용하며, 무엇이 완료되고 무엇이 진행 중인지 모릅니다.**

## 2. 방법론 내 위치

| 축 | 매핑 |
| --- | --- |
| 3 단계 서비스 플로우 | 단일 단계에 대응하지 않음; 「Diagnose → Build → Deliver」 3 단계의 **조감도** |
| 8 단계 컨설팅 구조 | 단일 단계에 대응하지 않음; 8 단계의 **전체 개요** |
| L1-L5 성숙도 | 단일 레벨에 대응하지 않음; L1-L5 의 **전체 개요** |
| Engagement Lifecycle | 단일 페이즈에 대응하지 않음; 전체 라이프사이클의 **시작점 설명** |

> 논리적 위치: `00_Overview` 는 「**무엇·왜**」 에 답함; `01`-`06` 은 「**어떻게**」 에 답함; `90_References` 는 「**근거·인용**」 에 답함.

## 3. 목표 & 효과

| 목표 | 효과 |
| --- | --- |
| 신규 독자가 5-10 분에 방법론 골격 이해 | 온보딩 단축; 오용 감소 |
| 가치 제안을 고객 언어로 말함 | Sales 가 스토리를 직접 30 분 고객 브리핑에 사용 가능 |
| 권위 있는 프로젝트 상태 파일 유지 | 누구나 「현재 진행도, 다음 단계」 확인 가능 — 구두 인수인계 불필요 |
| `01`-`06` 와 `90` 의 관계 연결 | 사용자가 각 디렉터리의 역할과 순서 파악 |

**본 디렉터리 건너뛸 경우**: 사용자가 기능 디렉터리로 직접 점프하여, 「왜 이 디렉터리가 존재하는지, 다른 디렉터리와 어떻게 연결되는지」 이해하지 못함 — 결과: 도구가 고립 사용되고, 방법론이 흩어진 파일 더미가 됨.

## 4. 워크플로 & 로직

```text
신규 독자 / 고객
   → AI_TRANSFORMATION_STORY_AND_STRUCTURE.md 읽기 (왜 + 어떻게 동작 + 무엇 산출)
   → 「L1-L5 + 8 단계 + 3 단계 플로우」 전체 멘탈 모델 구축
   → 01_Assessment 로 이동하여 실제 진단 시작

컨설턴트 / 동료 / 리뷰어
   → TODO_WBS.md 읽기 (프로젝트 진행도, 변경 로그, 다음 라운드 후보, 작업 일지)
   → 상황 파악 후 행동
```

| 단계 | 누가 | 언제 | 입력 | 출력 |
| --- | --- | --- | --- | --- |
| 스토리 읽기 | 컨설턴트 / 고객 / 신입 | 레포 첫 접촉 시 | 없음 | 방법론의 전체 이해 |
| 고객 브리핑 | Sales / 컨설턴트 | 프리엔게이지먼트 첫 미팅 | 스토리 | 고객이 진단 진입 준비 완료 |
| 프로젝트 상태 확인 | 컨설턴트 / 동료 / 리뷰어 | 인수 / 리뷰 전 | 없음 | 현재 상황 + 다음 단계 |
| 상태 업데이트 | 담당 컨설턴트 / AI | 각 배치 완료 후 | 완료 작업 | 업데이트된 `TODO_WBS.md` |

> 로직: 스토리는 「대외용」 (고객 + 신입 인지 형성); `TODO_WBS.md` 는 「대내용」 (실행자 상황 파악). 대외 + 대내가 완전한 입구를 구성.

## 5. 파일 설명

### `AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`

고객 지향 스토리와 챕터 구조. 기술 문서가 아닌 **내러티브** — 「기업이 왜 AI 트랜스포메이션이 필요한지, 방법론이 어떻게 단계적으로 동작하는지, 각 단계가 무엇을 수용 가능하게 산출하는지」 를 고객이 이해할 수 있는 일관된 스토리로 풀어 씀. 포함: 솔루션 포지셔닝, 3 단계 경로, L1-L5 ↔ 도구 매핑, 미래 상상, 역할별 가치 제안 (CEO/COO/CIO/IT/HR/부서장), §6 완전한 8 단계 정의 + 6 주 시나리오. 첫 고객 미팅에서 직접 사용 가능.

### `EXECUTIVE_SUMMARY.md`

방법론 전체를 5 분에 1 페이지로 압축. 디테일 볼 시간 없는 경영진용.

### `CLIENT_JOURNEY_STORY.md` 🆕

**Ming 의 이야기** — CEO / 이사회 / 가족이 20 분에 방법론을 이해할 시나리오 스토리. 반도체 패키징 700 명 회사의 24 개월 트랜스포메이션 — 제로 도구표, 제로 전문 용어. 대외 커뮤니케이션, 첫 고객 접촉, 신입 면접에 사용 가능.

### `EIGHT_STAGE_FLOW_STORY.md` 🆕

**권위 있는 8 단계 플로우 스토리**: 3 단계 계약 모델 (Phase A 진단 2W + Phase B 전략 4W + Phase C 도입 24M) + 중간 평가 보고서 + 분기 레이더 회고의 완전한 폐쇄 루프. 컨설턴트 내부 교육 필독.

### `METHODOLOGY_SCIENTIFIC_LOGIC.md` 🆕

**방법론의 과학적 토론 능력**: 과학적 방법의 5 조건 (관찰 가능, 정량화 가능, 재현 가능, 반증 가능, 감사 가능) 으로 8 단계가 왜 고객 / 이사회 / 규제 기관의 질문에 견디는지 검증. 학술 투고, 정책 로비, 이사회 리뷰 필독.

### `INDUSTRY_FRAMEWORK_ALIGNMENT.md` 🆕

**업계 프레임워크와의 정렬 지도**: 8 단계 vs McKinsey / BCG / Bain / Deloitte / Accenture / PwC; 4 계층 아키텍처 vs TOGAF / Zachman / Dragon1; L1-L5 vs Gartner / MIT / Forrester AI Maturity. 「우리 기존 방법론과 충돌하나요?」 라는 고객 질문 대응.

### `AI_NATIVE_LIVING_BOOK.md` 🆕

**방법론 운반 매체 혁신 논의**: 본 방법론을 **AI-native living book** (AI IDE 로 직접 실행 가능한 지식 시스템) 으로 포지셔닝, 단순 PDF / PPT 가 아님. 포함: 학술 분류 (executable knowledge artifact, AI-mediated methodology, interactive consulting playbook), 3 계층 설계 (Repo as Book / Agent as Tutor / Methodology as Executable Artifact), 4 대 리스크 통제 원칙 (AI ≠ 컨설턴트, evidence 필요, AGENTS.md 버전 관리, AI 출력 명시). 학술 투고 / 방법론 차별화 필독.

### `ACADEMIC_THEORETICAL_FOUNDATIONS.md` 🆕

**7 대 이론 기둥 통합 논의**: Capability Maturity (Rosemann/CMMI) + Absorptive Capacity (Cohen & Levinthal 1990) + Task-Technology Fit (Goodhue & Thompson 1995) + Dynamic Capabilities (Teece 1997/2007) + Sociotechnical Systems & Trust in AI (Bostrom 1977/Dietvorst 2015/Glikson 2020) + Real Options (Dixit & Pindyck 1994/McGrath 1997) + Executable Knowledge Artifact (Knuth 1984). 각 이론별: 요약 + 창시자 + Tiger AI 에 대한 기여 + 매핑 위치 + 인용. 학술 / 규제 / 이사회가 「이론적 근거는?」 물을 때 유일한 답.

### `../01_Assessment/BARS_RUBRICS.md` 🆕 (학술 강화)

**Behaviorally Anchored Rating Scales**: 6 차원 × 0-4 점의 **행동 앵커 표** (Smith & Kendall 1963 에 따라). 각 점수에 구체적인 관찰 가능 행동이 있어, **컨설턴트의 주관적 채점 회피**, inter-rater reliability 향상. Pilot Study Cohen's κ ≥ 0.60 목표 대응. 두 컨설턴트가 같은 회사에 유사한 점수를 줄 수 있는 핵심 메커니즘.

### `TODO_WBS.md`

본 레포의 **권위 있는 상태 파일**, 「현재 진행도」 의 유일한 신뢰 가능 출처. 포함: WBS 전체 (항목 × 우선순위 × 상태), 완료 파일 목록, 완료 항목 상세, 미완료 TODO, 다음 라운드 추천, **변경 로그 (배치별 + commit hash)**, 현재 상태 전체, **일일 작업 일지**. 컨설턴트 인수, 리뷰어 감사, AI 계속 작업 전에 반드시 읽기. 각 배치 완료 후 업데이트.

### `*_EN.md`

위 파일들의 영어 sibling 버전, 중국어 버전과 내용 대응.

## 6. 다른 디렉터리와의 대응

| 디렉터리 | 본 디렉터리와의 관계 | 데이터 플로우 |
| --- | --- | --- |
| `01_Assessment` | 스토리의 「진단」 단계가 여기서 구현 | `00` 스토리 → `01` 진단 도구 |
| `02_Course_Design` | 스토리의 「Build」 단계가 여기서 구현 | `00` 스토리 → `02` 강의 |
| `03_Consulting_Report` | 스토리의 「Deliver」 단계가 여기서 구현 | `00` 스토리 → `03` 컨설팅 보고서 |
| `04_Scenarios` | 스토리의 고객 시나리오 · 케이스 소재 제공 | `04` 케이스 ↔ `00` 스토리 |
| `05_Sales` | 스토리를 판매 가능 소재로 변환 | `00` 스토리 → `05` 판매 소재 |
| `06_Delivery` | 방법론을 납품 · 운영 가능 비즈니스로 변환 | `00` 스토리 → `06` 납품 & 운영 |
| `90_References` | 방법론 원본 + 제3자 인용 라이선스 | `90` 근거 → `00`-`06` 지원 |

## 7. 일반적 사용 시나리오

- **Sales 가 고객 초대**: `AI_TRANSFORMATION_STORY_AND_STRUCTURE.md` 의 3 단계 경로와 가치 제안으로 30 분 방법론 브리핑.
- **신규 컨설턴트 온보딩**: 먼저 스토리 읽고 인지 구축 → `TODO_WBS.md` 로 현황 파악 → §6 데이터 플로우 순서로 각 디렉터리 학습.
- **리뷰어 감사**: `TODO_WBS.md` 의 변경 로그와 작업 일지 직접 읽고 git log 와 비교.
- **AI 계속 작업**: `TODO_WBS.md` 의 「다음 라운드 후보」 와 「작업 일지」 읽고 어디부터 재개할지 파악.

---

## ⭐ Cross-Topic Quick References: 5 가지 핵심 주제, 어디서 찾는가

방법론 전체에는 모든 디렉터리를 관통하는 5 가지 주동맥이 있습니다. 본 디렉터리가 각각에 어떻게 연결되는지:

| Cross-Topic | 주 위치 | 본 디렉터리가 어떻게 연결되는가 |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 3 엔진 공독** | Root [`README_KR.md`](../README_KR.md) §🌟 ｜ [`07_AI_Contributions/`](../07_AI_Contributions/) | **본 디렉터리는 AI-Native Living Book 의 「스토리 입구」 자체** — [`AI_NATIVE_LIVING_BOOK.md`](AI_NATIVE_LIVING_BOOK.md) 가 완전한 논의; 4 개의 권위 개념 파일 (CLIENT_JOURNEY / EIGHT_STAGE_FLOW / METHODOLOGY_SCIENTIFIC_LOGIC / INDUSTRY_FRAMEWORK_ALIGNMENT) 이 모두 여기 있음 |
| 🎓 **학술 기반 (7 대 기둥)** | [`ACADEMIC_THEORETICAL_FOUNDATIONS.md`](ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | **7 대 이론 기둥 통합 논의가 본 디렉터리에 있음**: Rosemann / Cohen & Levinthal / TTF / Teece / Sociotechnical Trust / Real Options / Knuth |
| 📚 **L1-L5 강의 교육** | [`../02_Course_Design/`](../02_Course_Design/) | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0 이 **L1-L5 2 축** (규모 축 + AI 자율 축) 의 권위 있는 내러티브 입구 |
| 🔁 **컨설팅 / 8 단계 + Phase A→B→C 폐쇄 루프** | [`EIGHT_STAGE_FLOW_STORY.md`](EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **컨설팅 폐쇄 루프 스토리가 본 디렉터리에 있음** — `EIGHT_STAGE_FLOW_STORY` §6 에 완전한 폐쇄 루프 다이어그램 (Phase A 2W + Phase B 4W + Phase C 24M + 분기 레이더 회고) |
| 📖 **참고 자료 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | 본 디렉터리의 스토리는 `90_References` 의 모든 소재를 근거로 사용 (PDF / 다이어그램 / 비디오 노트 / 학술 이론 인용) |
