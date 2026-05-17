# 8 단계 컨설팅 플로우: 완전 시나리오 스토리와 클로즈드 루프 설계

> 🌐 언어: [繁體中文](EIGHT_STAGE_FLOW_STORY.md) ｜ [English](EIGHT_STAGE_FLOW_STORY_EN.md) ｜ [Deutsch](EIGHT_STAGE_FLOW_STORY_DE.md) ｜ [Français](EIGHT_STAGE_FLOW_STORY_FR.md) ｜ [Español](EIGHT_STAGE_FLOW_STORY_ES.md) ｜ [日本語](EIGHT_STAGE_FLOW_STORY_JA.md) ｜ 한국어
>
> Apache License 2.0 · 저자: Morris Lu · Tiger AI

최종 업데이트: 2026-05-15

---

> **이것은 무엇인가**: 8 단계 컨설팅 방법론을 완전, 재현 가능, 논의 가능한 클로즈드 루프 스토리로 작성한 것. 설문 수신부터 구현 계획까지, 각 단계에 명확한 트리거, 산출물, 서명, 다음 단계와의 락인 관계가 있음.
>
> **이것이 아닌 것**: 6 주 선형 마라톤 내러티브가 아님. 오히려 **3 단계 계약 모델 + 중간 인게이지먼트 고객 서명 + 분기별 루프 백** 의 완전한 과학적 관리 프로세스.

---

## 0. 선형 워크스루에 대한 개선 (3 가지 더 나은 설계 선택)

전형적인 사용자 직관:
> 설문 + AI As-Is 평가 → RM 과 비교 → 성숙도 + 케이스 벤치마킹 → 점수 → 클라이언트 리포트 제시 → 클라이언트가 Ideal Practice 선택 → 필요한 것 분석 → TO-BE 권장 → 컨설팅 리포트 → 구현 계획

**방향은 옳다**. Tiger AI 는 여기에 3 가지 개선을 구축:

| # | 개선 | 왜 더 강한가 |
| --- | --- | --- |
| **1** | **3 가지 계약 단계** (Phase A Diagnostic / Phase B Strategy / Phase C Implementation), 6 주 마라톤이 아님 | 클라이언트가 먼저 저위험으로 Phase A 에 커밋, 결과에 따라 B / C 결정; 컨설턴트는 과잉 커밋 회피 |
| **2** | **Phase A 종료: 중간 인게이지먼트 평가 리포트가 산출물로 서명됨** Phase B Ideal Practice 워크숍 시작 전 | 클라이언트는 먼저 레이더 빈 칸에 충격받음, 그 후 Ideal 선택 — 판타지 회피; 중간 리포트도 독립 산출물 |
| **3** | **분기마다 Reference Model 레이더 재방문** (Phase C Implementation 진입 후에도 지속) | 「완료했으니까 좋다」가 아니라 **「구조가 실제로 더 둥글어졌는가?」** — 이것이 과학적 클로즈드 루프 반증 메커니즘 |

> **왜 6 주 선형 마라톤보다 강한가**: 선형은 클라이언트에게 6 주 + 24 개월을 한 번에 커밋시킴 — 심리적 장벽이 너무 높음; 3 단계는 결정을 분할, 위험 감소, 수용 증가.

---

## 1. 3 단계 계약 모델 개관

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  Phase A: Diagnostic           Phase B: Strategy           Phase C:        ║
║                                                            Implementation  ║
║  ─────────────                ─────────────              ─────────────     ║
║  2 주 · NT$ 80 만             4 주 · NT$ 200 만          24 개월 · NT$ 700 만║
║                                                                             ║
║  Stage 1 + 2 + 3 자료        Stage 3 Ideal Practice      Stage 7 + 8        ║
║                                + Stage 4 + 5                                ║
║                                                            (분기별           ║
║                                                            레이더 재방문)   ║
║                                                                             ║
║  산출물:                     산출물:                     산출물:           ║
║  중간 인게이지먼트           완전 진단 리포트            Transformation     ║
║  평가 리포트                 + Ideal Practice            Roadmap +          ║
║  (클라이언트 수령)           정의 (3 자 서명)            Change Mgmt +      ║
║                                                          Value Tracking +   ║
║                                                          분기 로그          ║
╚═══════════════════════════════════════════════════════════════════════════╝
                ↑                       ↑                       ↑
            Gate A                  Gate B                   Gate C
        클라이언트가 B 로        클라이언트가 C 로          클라이언트가 각
        진행 결정                진행 결정                  분기 지속 결정
```

**과학적 의의**: 각 Gate 는 「클라이언트가 내릴 수 있는 출구점」 — 컨설턴트는 직전 단계 산출물이 **클라이언트가 지속하고 싶을 만큼 충분히 좋다는** **자신감이 있어야만** 이를 설계.

---

## 2. 주인공: Client M

> ⚠️ **「Client M / MingChang Packaging」 은 AI 생성 가공 기업**, 실제 고객 아님. 모든 규모, KPI, 예산, 타임라인 숫자는 **설명용 전용**, 방법론 교육 목적. 완전한 학술 진실성 면책 조항은 [`../04_Scenarios/README_EN.md`](../04_Scenarios/README_EN.md) 참조.

- **업계**: 반도체 패키징 & 테스팅 (FATP)
- **규모**: 700 명 직원, NT$ 12 억 연 매출
- **트리거**: 3 곳의 직접 경쟁사가 AI 품질 검사와 Complaint Agent 배치; 고객 A 의 분기 수주 18% 감소
- **페인 포인트**: Complaint response 5 일 (업계 1 일); Proposal turnaround 4 일 (업계 1.5 일); 불량률 3.2% (업계 1.8%)
- **제약**: 예산 상한 NT$ 800 만; 프로세스 데이터 온프레; IT 2 FTE, 성장 없음
- **역할**: CEO (Sponsor), COO, IT Director (잠재적 AI Champion), QC Head, Sales Head, CS Head, HR, Compliance

---

## 3. Phase A: Diagnostic (2 주, NT$ 80 만)

### 트리거

M Company 의 CEO 가 Tiger AI 아웃리치 메일 수신 + GitHub 에서 오픈소스 방법론 repo 를 봄; 비서가 30 분 인트로 미팅 스케줄.

### Pre-Engagement: 10 문항 퀵 서베이 (다음 주 발송)

CEO 가 [`01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md) 의 10 문항 버전을 자가 기입 (5 분).

**자동 채점 결과**:

```
6 차원 레이더:
  도구 사용                1 / 4 (일부 exec 가 ChatGPT 사적 사용)
  지식 침전                0 / 4 (Wiki 없음, SOP 없음)
  프로세스 자동화          1 / 4 (Finance 1 Power Automate 플로우)
  시스템 통합              2 / 4 (ERP/CRM 사일로화)
  Agent 적용               0 / 4 (없음)
  Governance & ROI         1 / 4 (AI 정책 없음)
합계: 5 / 24 → 예비 L1
```

CEO 가 레이더를 봄 → **첫 번째 충격** → Phase A 계약 서명 동의.

### Phase A 플로우 (주 1-2)

#### 주 1 ── Stage 1 As-Is Snapshot: 듣고, 보고, 코멘트 없음

| 일 | 액션 | Tool | 출력 |
| --- | --- | --- | --- |
| 일 1-2 | Exec 인터뷰 (CEO/COO/CIO × 60 분) + Dept Head 인터뷰 (QC/Sales/CS/IT/HR × 90 분) | Tool 1.1 (40 문 뱅크) | 녹음 + 서머리 |
| 일 3 | 오퍼레이터 인터뷰 (Line/Sales/CS × 각 3 × 30 분) | Tool 1.1 Section C | 서머리 |
| 일 4 | AI Usage Inventory + Systems Inventory | Tool 1.2 + 1.3 | Shadow IT 리스크 맵 + 시스템 맵 |
| 일 5 | 3 개 핵심 프로세스 워크스루 + Swimlanes 작성 | Tool 1.4 | 3 As-Is 프로세스 맵 |

**주 1 종료**: 컨설턴트가 클라이언트에게 「지금, 귀사가 무엇을 하고 있는지 압니다」 라고 전달. **코멘트 없음, 권장 없음.**

#### 주 2 ── Stage 2 Reference Model Alignment + Stage 3 자료 준비

| 일 | 액션 | Tool | 출력 |
| --- | --- | --- | --- |
| 일 6 | Reference Model 선택: SCOR + APQC + Tiger AI L1-L5 | Tool 2.1 | RM 선택 이유 |
| 일 7-8 | 매핑 워크시트: RM 셀에 As-Is 배치 | Tool 2.2 | 매핑 테이블 |
| 일 9 | Standard Capability Gap 체크리스트 + 듀얼 레이더 | Tool 2.3 + 2.4 | 2 개 레이더 (APQC + Tiger AI) |
| 일 10 | 벤치마크 케이스 준비 (5 stubs 에서 반도체 + 2 동업계 케이스 선택) | Tool 3.1 + 3.3 | 3 개 Best-Practice Profile |

> **Phase A 규율**: 일 10 컨설턴트는 **아직 Ideal Practice 워크숍을 실행하지 않음**. 자료만 — 다음 단계에서 사용.

### Phase A 산출물: 중간 인게이지먼트 평가 리포트 (클라이언트 수령)

**일 11-12 리포트 작성 → 일 13-14 클라이언트 리뷰 → 일 14 closeout meeting**

중간 인게이지먼트 리포트 (10-15 페이지):

1. **Executive Summary**: 「국제 표준 기준, 귀사는 SCOR Make/Deliver, APQC 11.x Knowledge, Tiger AI L1-L3 에 구조적 갭을 보임」
2. **As-Is Snapshot**: 인터뷰 서머리 + 시스템 맵 + 3 Swimlane
3. **Reference Model Mapping**: Standard Capability Gap 체크리스트
4. **듀얼 레이더**: APQC + Tiger AI L1-L5 (점선 = 벤치마크, 실선 = 회사)
5. **업계 Best Practice 자료**: 3 개 동업계 Benchmark Profile (자료만 — **아직 결론 없음**)
6. **다음 단계 권장**: Phase B Ideal Practice Workshop (반나절) + Stage 4-5 분석

### Gate A: 클라이언트가 Phase B 로 진행 결정

**closeout meeting 에서 일어나는 일**:

- CEO 가 레이더를 봄: 「잘하고 있다고 생각했는데 — 표준 아래 이 셀들이 0?」 → **두 번째 충격**
- COO 가 Swimlanes 를 넘김: 「우리 Complaint 프로세스는 정말 이런 구멍이 있구나...」 → 페인 포인트 구체화
- IT Director 가 shadow IT 월간 지출을 봄: 「사적 ChatGPT 가 NT$ 24,000 을 태우고 데이터가 새고 있다...」 → 리스크 구체화

**고객의 90% 가 Phase B 에 서명**. 왜냐하면:

- 레이더 갭은 컨설턴트의 말이 아님 — 국제 표준의 말 → **객관적**
- 페인은 직원 인터뷰 녹음에 있음 → **검증 가능**
- 동업계 기업이 이미 했음 → **달성 가능**

> **Phase A 의 설계 목표는 이 충격 그 자체**: 클라이언트가 **스스로 갭을 봄**, 컨설턴트에게 듣는 것이 아니라.

---

## 4. Phase B: Strategy (4 주, NT$ 200 만)

### 주 3 ── Stage 3 Ideal Practice 공동 창조 워크숍 (반나절)

**일 15 아침** ─ Tool 3.6 공동 창조 워크숍

| 단계 | 액션 | 시간 | 출력 |
| --- | --- | --- | --- |
| 1. 자료 표시 | 컨설턴트는 Tool 3.1/3.3/3.4/2.7 4 층 아키텍처를 **표시만, 권장하지 않음** | 30 분 | 공유 자료 |
| 2. 독립 투표 | 각자가 **독립적으로** 포스트잇에 「12 개월 후 우리가 무엇이 되고 싶은가」 작성 | 45 분 | N 장의 포스트잇 |
| 3. 집단 합의 | 4 층 아키텍처에 붙임, 합의 / 차이 찾음 | 60 분 | v1 Ideal Practice 초안 |
| 4. Reality check | 컨설턴트가 처음 개입, Tool 6.3 으로 실현 가능성 도전 | 45 분 | v2 Ideal Practice |
| 5. 정의 테이블 | v2 를 「Ideal Practice Definition Table」 로 작성 | 30 분 | 서명 버전 정의 테이블 |
| 6. **3 자 서명** | CEO + Sponsor + AI Champion | 15 분 | 공식, 감사 가능 문서 |

**M Company 의 서명된 Ideal Practice Definition Table (발췌)**:

| # | Capability | RM Category | 12 개월 타겟 | 에비던스 기준 |
| --- | --- | --- | --- | --- |
| 1 | Complaint response | APQC 4.4 + Tiger AI L3 | 90% 가 1 시간 내 + 24 시간 사람 응답 | n8n + Reviewer 서명 비율 ≥ 95% |
| 2 | 지식 침전 | APQC 11.x + Tiger AI L2 | ≥ 20 Skills 월간 추가 | Skill Library Git + Owner + IPOE |
| 3 | Process root cause | SCOR Make + Tiger AI L4 | 이상 → 가설 ≤ 1 시간 | Hermes Agent + 5 태스크 Reviewer pass |

> **이 테이블은 전 인게이지먼트의 앵커**. 모든 후속 Stage 4-8 계산은 이를 기반; 클라이언트는 자기 서명 타겟을 부정할 수 없음.

### 주 3-4 ── Stage 4 Gap Analysis + Stage 5 Problem Definition

#### Stage 4: Gap = (Client Ideal − Client As-Is)

| 일 | 액션 | Tool | 출력 |
| --- | --- | --- | --- |
| 일 16-17 | M/B/R 분류 + Impact × Effort | Tool 4.1 + 4.2 | Gap matrix |
| 일 18 | Prioritization Worksheet | Tool 4.3 | 우선순위 랭킹 |

#### Stage 5: 80/20 수렴으로 Root Cause 로

| 일 | 액션 | Tool | 출력 |
| --- | --- | --- | --- |
| 일 19 | 80/20 수렴 + 5 Whys | Tool 5.1 + 5.2 | Core lesion 리스트 |
| 일 20-21 | Executive Problem Statement | Tool 5.3 + 5.4 | 한 문장 정의 |

**M Company 의 Executive Problem Statement**:

> M Company 는 「지식 자산화」의 역할, 도구, 인센티브가 결여됨. 80% 의 갭 (느린 Complaint / 느린 Quote / 지식 침전 없음 / 느린 Root Cause) 은 「같은 것을 반복하고, 아무도 침전시키지 않고, 아무도 재사용하지 않음」 에서 옴.

### 주 4 ── Stage 6 Phased Goals + Stage 7 To-Be Design

#### Stage 6: Ideal 을 흡수 가능한 단계로 분해

| 일 | 액션 | Tool | 출력 |
| --- | --- | --- | --- |
| 일 22 | Ultimate Ideal → Phase 1/2/3 분해 | Tool 6.1 | 분해 테이블 |
| 일 23 | 조직 흡수 평가 (6 차원) | Tool 6.3 | 흡수 점수 |
| 일 24 | Stage Gate Criteria | Tool 6.2 | L1-L5 Gate 체크리스트 |

> **M Company 의 흡수 평가에서 IT 가 2 FTE 만 있음을 발견; Phase 2 는 +0.5 필요**. 결정: Phase 2 를 6 → 9 개월로 연장. **이 조정은 클라이언트가 스스로 데이터를 보고 한 것, 컨설턴트 권장이 아님**.

#### Stage 7: Phase 마다 1 개 To-Be Operating Model

| 일 | 액션 | Tool | 출력 |
| --- | --- | --- | --- |
| 일 25-26 | Phased To-Be Operating Models (3 도) | Tool 7.1 | 3 도 |
| 일 27 | Human-AI Collaboration + HITL 노드 | Tool 7.2 | 프로세스별 분할 |
| 일 28 | Skill/Workflow/Agent Map + Integration Architecture | Tool 7.3-7.6 | 3 맵 + Variant B Hybrid |

### Phase B 산출물: 완전 진단 리포트 + Ideal Practice Definition Table

**일 29-30 리포트 작성 → 일 31-32 클라이언트 리뷰 → 일 32 closeout meeting**

완전 진단 리포트 (30-50 페이지), [`CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) 14 섹션 구조 기반.

### Gate B: 클라이언트가 Phase C 로 진행 결정

**고객의 95% 가 Phase C 에 서명**. 왜냐하면:

- Ideal Practice 는 **자기들이 서명** → 부정 불가능
- Gap 은 뺄셈으로 계산 → **검증 가능**
- Phase 1/2/3 는 조직 흡수에 핏 → **달성 가능**

---

## 5. Phase C: Implementation (24 개월, NT$ 700 만)

### Stage 8 Implementation & Change

**첫 달 (월 1)**

| 일 | 액션 | Tool | 출력 |
| --- | --- | --- | --- |
| 일 33 | Transformation Roadmap (24 개월 / 6 분기) | Tool 8.1 | Roadmap |
| 일 34 | Change Management Plan + resistance Playbook | Tool 8.2 | Change plan |
| 일 35 | RACI + Permission Matrix + Audit Log | Tool 8.3 + 8.4 + 8.7 | 거버넌스 문서 |
| 일 36 | Value Tracking Matrix (5 차원) | Tool 8.5 | Dashboard spec |
| 일 37 | Risk Register (case Failures 통합) | Tool 8.6 | Risk log |
| 일 38 | AI Ethics 체크리스트 | Tool 8.8 | 서명된 ethics |
| 일 39 | SOW + Phase 1 kickoff | — | Phase 1 시작 |

### Phase 1 (월 1-6): Foundation

- L1 전사 OpenWebUI 라이브
- 5 개 core Skills 공개
- AI 정책 > 90% 서명
- Prompt Library ≥ 30 엔트리

**월 6 종료 → L1 Gate acceptance + Stage 2 레이더 재방문**:

```
APQC 11.x Knowledge:  0 → 2 (Skill library 시작)
Tiger AI L1:          0 → 4 (완전 OpenWebUI + 92% policy 서명)
Tiger AI L2:          0 → 2 (5 Skills)
```

> 레이더가 **정말 더 둥글다**. 클라이언트가 눈물을 글썽임: 「그래서 이게 과학적 관리구나.」

### Phase 2 (월 6-15): Optimization

- L2 Skill Library ≥ 15 엔트리
- L3 n8n Workflow ≥ 3 라이브
- HITL 노드 완전 배치

**월 15 종료 → L2/L3 Gate + 레이더 재방문**:

```
APQC 4.0 Deliver: 1 → 3 (complaint response 5 일 → 1 일) ✓ Ideal 달성
APQC 11.x:        2 → 3 (지식 침전 안정) ✓ Ideal 달성
Tiger AI L3:      0 → 2 (n8n PoC 라이브)
```

### Phase 3 (월 15-24): Excellence

- L4 Hermes Agent 가 4A-4E 통과
- L5 ClawTeam cross-dept 1 개 성공 리허설

**월 24 종료 → L4/L5 Gate + 최종 레이더**:

```
SCOR Make + Tiger AI L4: 0 → 3 (Hermes Agent 통과) ✓ Ideal 달성
Tiger AI L5:             0 → 2 (ClawTeam cross-dept 리허설)
```

### Gate C 분기: 클라이언트는 각 분기 결정 가능

각 분기는 필수:

1. Quarter Gate acceptance (Tool 6.2 체크리스트 기준)
2. Stage 2 레이더 재방문 (개선을 정량화)
3. Value tracking matrix 5 차원 리뷰
4. 클라이언트가 다음 분기 진행, 조정, 일시 정지 결정

> 24 개월 후: M Company complaint response 1 일, 불량률 2.0%, 고객 churn 제로, Stage 2 레이더가 **들쭉날쭉한 선에서 거의 둥근 모양으로 변화**.

---

## 6. 완전 클로즈드 루프 도식

```
                          ┌──────────────────┐
                    ┌────►│ Phase A Diag 2W   │
                    │     │ Stage 1 + 2 + 3   │
                    │     │   자료 준비       │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ 중간 Report      │ ← Phase A 산출물
                    │     │ (클라이언트 수령) │
                    │     └────────┬─────────┘
                    │              │
                    │           Gate A
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase B Strat 4W  │
                    │     │ Stage 3 Ideal     │
                    │     │ + Stage 4 + 5     │
                    │     │ + Stage 6 + 7     │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ 완전 Report      │ ← Phase B 산출물
                    │     │ + Ideal Practice  │
                    │     │ (3 자 서명)       │
                    │     └────────┬─────────┘
                    │              │
                    │           Gate B
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase C Impl 24M  │
                    │     │ Stage 8           │
                    │     │ Transformation +  │
                    │     │ Change + Value    │
                    │     └────────┬─────────┘
                    │              │
                    │     ┌────────▼─────────┐
                    │     │ Phase 1/2/3       │
                    │     │ Stage Gate accept │
                    │     └────────┬─────────┘
                    │              │
                    │     분기 Gate C
                    │              │
                    │     ┌────────▼─────────┐
                    └─────┤ Stage 2 Radar    │
                          │ 재방문 (더 둥글?) │
                          └──────────────────┘
                                  
                          이 피드백 라인이
                          과학적 클로즈드 루프의
                          핵심 반증 메커니즘
```

---

## 7. 왜 이 플로우가 클라이언트 토론을 견디는가

가능한 모든 challenge 에 대해, 응답 장소:

| Challenge | 장소 | 에비던스 |
| --- | --- | --- |
| 「L1 인지 어떻게 아는가?」 | Phase A mid-report §2 레이더 | 10-Q 서베이 + 녹음 + system inventory |
| 「왜 이 셀들이 0?」 | Phase A §3 RM Mapping | APQC / Tiger AI 공식 표준 |
| 「누가 타겟 설정?」 | Phase B §5 Ideal Practice 테이블 | **클라이언트 자신이 서명, 3 자 서명** |
| 「왜 갭이 큰가?」 | Phase B §6 Gap Analysis | Gap = (당신의 서명 Ideal − 당신의 As-Is) 공식 |
| 「왜 고객 서비스가 영업보다 먼저?」 | Phase B §6.2 | Impact × Effort matrix |
| 「왜 24 개월?」 | Phase B §8 + Tool 6.3 | Case Benchmark + Organizational Absorption |
| 「잘 안되면?」 | Phase C §13 Risk Register | Trigger + Owner + Mitigation |
| 「개선됐다고 어떻게 증명?」 | 분기 Gate C | Stage 2 레이더 + Value Tracking 5 차원 |
| 「이전 컨설턴트는 L3, 당신은 L2 — 누가 맞나?」 | 공식 0-4 스케일 + 에비던스 | 제 3 자가 독립 검증 가능 |

---

## 8. 사용자 오리지널 플로우와의 매핑

| 사용자 단계 | Phase | Stage | 개선 |
| --- | --- | --- | --- |
| 1. 설문 + AI As-Is | Phase A W1 | Stage 1 | + 10-Q 퀵 스크린을 pre-engagement 로 |
| 2. RM 과 비교 | Phase A W2 | Stage 2 | 4 층 아키텍처 + 듀얼 레이더 |
| 3. 성숙도 + 케이스 벤치마킹 → 점수 | Phase A 끝 W2 | Stage 3 자료 | 케이스는 Benchmark-grade (9 필드) 여야 함 |
| 4. **클라이언트가 평가 리포트를 봄** | **Phase A 산출물** | — | **신규: 중간 리포트를 독립 산출물 + 클라이언트 수령으로** |
| 5. 클라이언트가 Ideal Practice 선택 | Phase B W3 | Stage 3 Tool 3.6 | **클라이언트 서명, 컨설턴트 처방이 아님** |
| 6. 필요한 것 분석 | Phase B W3-W4 | Stage 4 + 5 | Gap = Ideal − As-Is, 80/20 수렴 |
| 7. TO-BE 권장 | Phase B W4 | Stage 6 + 7 | Phased + 조직 흡수 평가 |
| 8. 컨설팅 리포트 | Phase B 산출물 | — | 14 섹션 완전 리포트 + 서명된 Ideal Practice |
| 9. 구현 계획 | Phase C kickoff | Stage 8 | Change Mgmt + Value Tracking + Audit |
| **(누락)** | **분기 재방문** | — | **신규: 각 분기 Stage 2 레이더 재방문 (과학적 클로즈드 루프)** |

---

## 9. 다른 문서와의 관계

| 문서 | 본 문서와의 관계 |
| --- | --- |
| [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §6 | 8 단계 정의와 데이터 플로우 제공; 본 doc 은 완전 프로세스 내러티브 |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | 「왜 그렇게 설계」 과학적 논증 제공; 본 doc 은 「실제로 어떻게 진행」 |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) | Per-Stage 도구 테이블 제공 |
| [`../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) | Phase B 산출물 14 섹션 구조 제공 |
| [`../04_Scenarios/`](../04_Scenarios/) | Phase A 용 Benchmark-grade 케이스 제공 |
| [`../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md`](../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md) | 인게이지먼트 / 가격 / 딜리버리 SOP 제공 |

---

## 10. 클로징: 왜 클로즈드 루프는 과학인가

이 플로우는 **선형 마라톤이 아닌**, **피드백 있는 클로즈드 루프**:

- **각 Gate 는 출구점** → 컨설턴트는 이렇게 설계할 **자신감이 있음** (직전 산출물이 클라이언트 지속 의향을 끌어낼 만큼 충분히 좋아야 함)
- **각 산출물에 클라이언트 서명** → 후속 추론을 부정할 수 없음
- **각 분기 Stage 2 레이더 재방문** → 구조가 실제로 더 둥글어짐 = 성공, 「PoC 완료 = 성공」 이 아님

**그것이 과학적 관리**:

- 객관적인 출발점 (국제 표준 + 클라이언트 서명)
- 검증 가능한 프로세스 (모든 Stage Gate Criteria)
- 반증 가능한 종점 (듀얼 레이더 before/after + Value Tracking 5 차원)

만약 누군가 「Tiger AI 방법론은 작동하지 않는다」 라고 한다면, 그들은 **도전** 해야 함:

- APQC PCF 가 틀렸는가?
- Rosemann BPM 학파가 틀렸는가?
- 클라이언트 자신이 서명한 Ideal Practice 가 카운트되지 않는가?
- 우리의 분기 레이더 루프 백이 카운트되지 않는가?

**어렵다.** 그래서 클로즈드 루프 설계에 투자했다.

---

라이선스 & 인용

본 문서는 Apache License 2.0; [`../NOTICE`](../NOTICE) 귀속이 보존되는 조건으로 사용, 수정, 상업화 가능.
