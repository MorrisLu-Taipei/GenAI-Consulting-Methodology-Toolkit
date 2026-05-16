# 03 Consulting Report — 컨설팅 진단 & 보고서 (컨설팅 폐쇄 루프)

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. 본 디렉터리의 위치

본 디렉터리는 3 단계 서비스 플로우의 **세 번째 단계: Deliver**, 그리고 전체 방법론의 **컨설팅 실무의 핵심** 입니다.

진단 (`01`) 은 객관적 점수 제공, Build (`02`) 는 고객 역량 성장 — 그러나 컨설팅 안건이 최종적으로 고객에게 전달하는 것은 **구조화되고, evidence 기반, Roadmap 있고, 의사결정층이 채택 가능한 진단 보고서**. 본 디렉터리는 그 보고서 작성에 필요한 모든 것을 제공: **8 단계 컨설팅 구조의 도구표, 고전 컨설팅 프레임워크 라이브러리, 보고서 생산 워크플로, 보고서 템플릿**.

> 🔁 **본 디렉터리는 「6 주 마라톤 선형 프로세스」 가 아니라, 「컨설팅 폐쇄 루프」**. 완전한 폐쇄 루프 설계는 [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) 참조:
> **3 단계 계약** (Phase A 진단 2W + Phase B 전략 4W + Phase C 도입 24M) + **중간 평가 보고서** + **분기별 레이더 회고** (과학 관리의 반증 메커니즘).
> 루프의 핵심은 「완료하면 끝」 이 아니라 「**구조가 실제로 둥글어졌는가?**」 — Stage 2 Reference Model 레이더에 대한 지속적 자기 반증.

해결하는 문제: **방법론 없이는, 컨설턴트 진단은 경험 기반 개인 수공예 — 스케일 불가, 신입 컨설턴트 재현 불가, 품질 불안정.** 본 디렉터리는 「컨설턴트가 어떻게 진단하는가」 를 가르칠 수 있고 재현 가능하고 검수 가능한 표준 폐쇄 루프로 변환.

본 디렉터리를 쓰는 사람: 컨설턴트, 시니어 컨설턴트, 신입 컨설턴트 (온보딩), PM.

## 2. 방법론 내 위치

| 축 | 매핑 |
| --- | --- |
| 3 단계 서비스 플로우 | **Deliver** — 세 번째 단계 |
| 8 단계 컨설팅 구조 | **본 디렉터리는 8 단계 (Stage 1-8) 의 도구와 보고서 본체 자체** |
| **3 단계 계약 모델** | **Phase A 진단 2W → Phase B 전략 4W → Phase C 도입 24M + 분기별 레이더 회고** (컨설팅 폐쇄 루프) |
| L1-L5 성숙도 | 보고서에서 고객의 L 레벨과 강의 관찰 인용 |
| Engagement Lifecycle | **Delivery — Handover** (보고서는 Phase B 의 핵심 납품; Phase C 는 분기별 레이더 회고 기록 지속 산출) |

> 두 직교 축: **L1-L5 는 「역량 세로축」 (`02` 담당); 8 단계는 「진단 가로축」 (본 디렉터리 담당).** 두 축이 교차하여 검증 가능 납품물 산출.
>
> **L1-L5 자체가 2 축** (규모 축 L1-L3 + AI 자율 축 L4-L5); [`../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](../00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0 참조.

## 3. 목표 & 효과

| 목표 | 효과 |
| --- | --- |
| 8 단계 각 스텝에 직접 사용 가능 도구표 | 컨설턴트 도구 설계 재작업 불필요; 신입 컨설턴트 즉시 가능 |
| 고전 프레임워크 라이브러리가 8 단계에 매핑 | 각 스텝에서 「어떤 분석 프레임워크 쓸지」 알 수 있음 |
| 보고서 생산 워크플로 | 「문제 → 납품 가능 보고서/덱」 에 SOP, 수공예가 아님 |
| 보고서 구조 고정 | 납품 품질 안정; 의사결정층이 이해 가능 |
| 컨설팅 방법론 교육·재현 가능 | 컨설팅 팀 스케일 가능 |

**본 디렉터리 건너뛰면**: 각 컨설턴트가 자기 방식으로 진단, 보고서 품질 일관성 없음, 신입 재현 불가, 진단이 「시니어의 개인 수공예」 로 전락.

## 4. 워크플로 & 로직 (3 단계 계약 + 분기 폐쇄 루프)

```text
01 진단 결과 + 02 강의 관찰
   ↓
┌─ Phase A 진단 (2 주) ──────────────────────────────────┐
│  Stage 1-4 8 단계 전반: Awareness / Reference Model /  │
│  Discovery / Gap Analysis                              │
│  → CONSULTING_TOOLKIT_TEMPLATES.md 도구 사용           │
│  → 중간 평가 보고서 → 고객 서명                         │
└────────────────────────────────────────────────────────┘
   ↓ Gate A 고객이 Phase B 갱신 결정
┌─ Phase B 전략 (4 주) ──────────────────────────────────┐
│  Stage 5-8 8 단계 후반: Stakeholder / Diagnosis /      │
│  To-Be Design / Acceptance Test                        │
│  → REPORT_PRODUCTION_WORKFLOW.md 8 스텝 생산           │
│  → 완전한 14 장 진단 보고서 + 24M Roadmap + ROI +      │
│     거버넌스 제언                                       │
│  → CONSULTING_REPORT_TEMPLATE.md 고정 구조에 기입       │
└────────────────────────────────────────────────────────┘
   ↓ Gate B 고객이 Phase C SOW 서명
┌─ Phase C 도입 (24 개월) ─ 폐쇄 루프 피드백 단계 ───────┐
│  단계별 구현 + **분기별 Gate C: Stage 2 레이더 재점검** │
│  → 구조가 실제로 둥글어졌는가? 아니면 → 해당 Stage 로  │
│     돌아가 Roadmap 수정                                 │
│  → 분기별 산출: 레이더 회고 기록 + Roadmap 교정 기록   │
└────────────────────────────────────────────────────────┘
```

| Phase | 기간 | 대응 8 단계 | 주요 도구 | 주 납품 |
| --- | --- | --- | --- | --- |
| **Phase A 진단** | 2 주 | Stage 1-4 | TOOLKIT 전반 + FRAMEWORKS 셀렉터 | **중간 평가 보고서** + Reference Model 레이더 서명 |
| **Phase B 전략** | 4 주 | Stage 5-8 | TOOLKIT 후반 + REPORT_PRODUCTION_WORKFLOW + REPORT_TEMPLATE | **완전한 14 장 진단 보고서** + Roadmap + ROI + 거버넌스 |
| **Phase C 도입** | 24 개월 | Stage 2 분기 리뷰 | TOOLKIT 분기 레이더 회고 도구 + Risk Register | **분기별 레이더 회고 기록** + Roadmap 교정 |

> 로직: `CONSULTING_TOOLKIT_TEMPLATES` 는 「진단의 도구 + 분기 회고 도구」; `CONSULTING_FRAMEWORKS_LIBRARY` 는 「각 스텝에서 어떤 분석 프레임워크」; `REPORT_PRODUCTION_WORKFLOW` 는 「어떻게 진단을 효율적으로 납품물로 변환」; `CONSULTING_REPORT_TEMPLATE` 은 「최종 보고서는 어떤 모습」. 넷 합치면 = **완전한 컨설팅 폐쇄 루프 방법론** (선형 마라톤 아님).

> 📖 완전한 8 단계 대화 스크립트 + 폐쇄 루프 스토리: [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) (「왜 폐쇄 루프가 과학인가」 결어 포함).

## 5. 파일 설명

### `CONSULTING_REPORT_TEMPLATE.md`

AI 트랜스포메이션 진단 보고서의 Markdown 템플릿 (v2.0 8 단계 정렬판). 14 장 고정 구조: 커버, Executive Summary (표준 갭 개요 포함), 진단 방법, As-Is Snapshot, Reference Model Alignment (APQC + Tiger AI 이중 좌표), Best Practice Integration (탁월 역량 프로파일), Gap Analysis, Executive Problem Statement, Phased Goals, To-Be Design, Implementation Roadmap, Change Management Plan, Governance Design, Value Tracking & Risk Register, SOW 제언.

### `CONSULTING_TOOLKIT_TEMPLATES.md`

8 단계 컨설팅 진단의 **직접 사용 가능 도구표** (v2.0 이미지 정렬판). 각 단계가 1-5 도구에 매핑: 40 문항 인터뷰 뱅크, AI/시스템 정리, As-Is 스윔레인, **Reference Model 선정 (APQC/SCOR/eTOM/ITIL/CMMI) + Mapping Worksheet + Standard Gap Checklist + 이중 레이더**, Best-Practice Profile + 탁월 역량 프로파일, Missing/Broken/Redundant (**리스크 평가 아님**), Impact×Effort, **80/20 수렴 + 5 Whys**, Problem Statement, **궁극 벤치마크 → Phased Goals + 조직 흡수력 평가**, **단계별 To-Be Operating Model + Human-AI Collaboration (HITL)**, Skill/Workflow/Agent Map, Transformation Roadmap, **Change Management Playbook (저항 대응 포함)**, RACI, 권한, **Value Tracking Matrix (시간/품질/규모/리스크/자산 5 차원)**, Risk Register, Audit, Ethics, **Phase A 2W + Phase B 4W 표준 스케줄 + Phase C 분기 레이더 회고 도구** (컨설팅 폐쇄 루프). 복붙으로 사용 가능.

### `CONSULTING_FRAMEWORKS_LIBRARY.md`

고전 컨설팅 프레임워크 라이브러리. 50+ 업계 프레임워크 (MECE, Pyramid Principle, Issue Tree, Porter's 5 Forces, SWOT, BCG Matrix, 5 Whys, Fishbone, Business Model Canvas, WBS/RACI, NPV/IRR, Lean/Six Sigma 등) 7 카테고리. 「프레임워크 셀렉터」 (자연어 → 프레임워크 조합), 「프레임워크 조합 체인」, 각 프레임워크의 8 단계 매핑, §4.8 MECE / Issue Tree / 가설 형성 심화 포함. yoichiojima-2/consultant (MIT) 에서 adapt.

### `REPORT_PRODUCTION_WORKFLOW.md`

「문제 → 납품 가능 보고서/덱」 의 8 스텝 생산 워크플로. Dummy Page (먼저 골격, 나중에 채움), 의존성 관리, 7 종 페이지 레이아웃, Excel 에비던스 트레이스, progressive disclosure, §9 troubleshooting playbook (7 가지 일반적 문제 + 수정법) 포함. Kafurtan/mckinsey-consultant-skills (MIT) 에서 adapt.

### `*_EN.md`

위 파일들의 영어 sibling 버전.

## 6. 다른 디렉터리와의 대응

| 디렉터리 | 본 디렉터리와의 관계 | 데이터 플로우 |
| --- | --- | --- |
| `01_Assessment` | 진단 점수와 레이더는 8 단계 Stage 1 의 핵심 입력 | `01` 점수 → `03` 보고서 |
| `02_Course_Design` | 클래스 내 산출과 관찰은 「강의 관찰」 챕터의 소재 | `02` 강의 관찰 → `03` 보고서 |
| `00_Overview` | 보고서는 스토리의 「Deliver」 단계 | `00` 스토리 → `03` 구현 |
| `04_Scenarios` | 8 단계 Stage 3 업계 Best Practice 벤치마킹에서 케이스 인용 | `04` 케이스 → `03` Stage 3 |
| `06_Delivery` | 보고서는 납품 패키지의 핵심 납품; Handover 에 대응 | `03` 보고서 → `06` 납품 검수 |
| `90_References` | 프레임워크 라이브러리와 보고서 워크플로의 제3자 인용 (consultant / mckinsey-skills) | `90` 인용 → `03` |

## 7. 일반적 사용 시나리오 (폐쇄 루프 단계별)

- **신입 컨설턴트 온보딩**: 먼저 `CONSULTING_TOOLKIT_TEMPLATES.md` 의 모든 sample 한번 돌고, [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) 대화 스크립트 읽고, 마지막에 실제 인터뷰 shadow.
- **Phase A 진단 (2 주)**: TOOLKIT 의 Stage 1-4 도구 (40 문항 인터뷰, AI/시스템 정리, Reference Model 레이더) 사용, 주말에 **중간 평가 보고서** 를 Sponsor 서명용으로 산출.
- **Phase B 전략 (4 주)**: TOOLKIT 의 Stage 5-8 도구 + `REPORT_PRODUCTION_WORKFLOW.md` 8 스텝 생산으로 진단을 덱으로 변환, `CONSULTING_REPORT_TEMPLATE.md` 에 기입, **완전한 14 장 보고서 + 24M Roadmap + ROI** 산출.
- **Phase C 도입 (24 개월, 루프 피드백 단계)**: 분기별로 TOOLKIT 의 레이더 회고 도구로 **Stage 2 Reference Model 레이더 재실행** — Phase A 서명판과 비교, 「구조가 실제로 둥글어졌는지」 확인; 둥글지 않으면 → 해당 Stage 로 돌아가 Roadmap 수정.
- **고객이 「왜 이 프레임워크?」 라고 물으면**: `CONSULTING_FRAMEWORKS_LIBRARY.md` 의 프레임워크 셀렉터로 설명.
- **고객이 「6 주 후에는?」 이라고 물으면**: [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) §6 완전한 폐쇄 루프 다이어그램 보여줌 — 핵심은 6 주가 아니라 Phase C 24 개월 + 분기 레이더 회고의 반증 메커니즘.
