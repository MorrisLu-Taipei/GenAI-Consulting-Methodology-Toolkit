# Failure Patterns & Counter-Cases: Tiger AI 방법론을 적용하지 말아야 할 때 / 실패할 때

> 🌐 언어: [繁體中文](FAILURE_PATTERNS.md) ｜ [English](FAILURE_PATTERNS_EN.md) ｜ [Deutsch](FAILURE_PATTERNS_DE.md) ｜ [Français](FAILURE_PATTERNS_FR.md) ｜ [Español](FAILURE_PATTERNS_ES.md) ｜ [日本語](FAILURE_PATTERNS_JA.md) ｜ 한국어
>
> Apache License 2.0 · 저자: Morris Lu · Tiger AI

마지막 업데이트: 2026-05-16

---

> **목적**: 성공만 논의하는 방법론은 세일즈 자료. 학술 / 규제 / 진지한 고객은 묻는다: 「**언제 실패하는가? 언제 적용하지 말아야 하는가? 레벨을 건너뛰면 무엇이 잘못되는가?**」 본 문서는 알려진 failure patterns 와 counter-cases 를 방법론의 비판 가능성과 개선 가능성의 하드 증거로 공개 기록.

---

## 1. 왜 방법론은 Failure Modes 를 발표해야 하는가

| 청중 | 왜 실패를 봐야 하는가 |
| --- | --- |
| **학술 리뷰어** | 성공만 사례 = selection bias → 출판 불가 |
| **규제 기관** | 위험 평가는 failure modes + early-warning 조건을 포함해야 함 |
| **진지한 고객** | 「**언제 실패하는지 말해줘**」가 진정한 신뢰 질문 |
| **컨설턴트** | Failure modes = 제도적 기억 = 반복 회피 |

> **성공만 논의하는** 방법론은 **실패를 인정하는** 방법론보다 신뢰성이 낮음.

---

## 2. 레벨 건너뛰기 실패

### 2.1 L1 건너뛰기 → L4 Agent 로 점프

**증상**: 전사적 L1 채택 없음. 보스가 Agent 데모를 보고 고객 서비스 Agent 를 원함. 3 엔지니어가 3 개월에 Agent 구축. 라이브 후: CS 직원이 사용을 두려워함, QC 가 서명하지 않음, IT 가 audit log 배선을 모름, Compliance 가 「누가 위험을 부담하는가」 라고 물음.

**근본 원인**: 직원이 L1 을 통한 **개인적 신뢰**를 구축하지 않음; L2 Skill Library 없음 → Agent 가 「회사가 작성한 판단 논리」가 없음; L3 Workflow 없음 → Agent 가 시스템에 작용할 합법적 파이프가 없음; L1-L3 거버넌스 기반 없음 → Agent 가 compliance 블랙박스로 라이브.

**전형적 결말**: Agent 가 6 개월에 폐기; IT 부부장이 비난받음; AI 예산 삭감.

### 2.2 L2 건너뛰기 → L3 Workflow 직접 구축

**증상**: IT 가 n8n 튜토리얼을 봄 → Gmail → CRM → Slack 체인 구축. 월 1: 작동. 직원이 「출력이 off-tone / 우리 SOP 를 인용하지 않는다」 고 불평. 엔지니어가 프롬프트를 튜닝하지만, **각 Workflow 에 10 프롬프트가 n8n 노드에 분산 — 오너 없음, 버전 없음, 문서 없음**.

**근본 원인**: 「회사가 작성한 프롬프트 + 판단 + 데이터」 로서의 L2 Skill Library 없음 → L3 가 「IT 엔지니어의 개인 프롬프트 놀이터」 가 됨.

**전형적 결말**: Workflow 품질이 시간이 지나며 드리프트; 3 개월 후 비즈니스 유닛이 revert 요청; IT 가 신뢰를 잃음.

### 2.3 HITL 없이 L3 / L4 진행

**증상**: Workflow 가 자동으로 고객 이메일 전송, 자동으로 청구서 생성, 자동으로 주문 배치. 월 1: 70% 효율 향상. 월 2: LLM 환각 → tier-A 고객에게 잘못 가격된 견적 → NT$ 300만 계약 손실.

**근본 원인**: 모든 AI 가 ~0.5-3% 환각률을 가짐. **HITL 없음 = 조만간 zero-tolerance 시나리오에 부딪힘**.

**전형적 결말**: C-suite 가 AI 금지; AI Champion 처벌; 방법론에 「unreliable」 라벨.

### 2.4 L4 안정화 전 L5 ClawTeam 서두르기

**증상**: 보스가 멀티에이전트 데모를 보고 Sales + CS + QC 부서 간 Agent Team 을 원함. 단일 Agent 도 Stage Gate 4A-4E 를 통과하지 못했지만 3 Agent 가 체인화. Evidence trail 이 Agent 간 깨짐 → 아무도 결정을 추적할 수 없음.

**근본 원인**: 단일 Agent 거버넌스 없음 → 멀티 Agent 는 통제를 잃을 수밖에 없음 (어떤 Agent 가 어떤 문제를 일으켰는지 누구도 특정할 수 없음).

**전형적 결말**: 프로젝트가 6 개월에 해산; 단일 Agent 로 회귀; 반년 낭비.

---

## 3. Organizational Misfit 실패

### 3.1 AI Champion 없음 (임원 드라이버)

**전제 조건**: 각 Phase 는 적어도 1 명의 Champion 이 필요, 「부서 간 조정, 결정, Sponsor 에 보고」 가능한 사람.

**실패**: CEO 가 Phase A 에 서명하지만 Champion 을 지정하지 않음 → 인터뷰 중 부서장들이 책임을 미룸 → As-Is 불완전 → Phase A 품질 낮음 → 고객이 Phase B 에 서명하지 않음.

**Tiger AI 거부**: Phase B 전에 Champion 이 자리잡지 않은 경우, **컨설턴트는 서명을 거부**하거나 Champion 지정을 먼저 요구해야 함.

### 3.2 L3+ 에 IT 캐파시티 부족

**전제 조건**: L3 Workflow + L4 Agent 는 지속적 유지보수에 0.5-2 IT FTE 가 필요.

**실패**: 회사에 IT 1 명, 이미 ERP / 네트워크 / Helpdesk 로 maxed. 5 Workflow 가 라이브 → 아무도 유지보수 안 함 → 6 개월에 50% 실패 → 직원이 수동으로 되돌아감.

**Tiger AI 거부**: Tool 6.3 Organizational Absorption 「IT FTE」 < Phase 2 최소 (0.5 전담 FTE) 인 경우, **고객에게 IT 추가를 먼저 하도록 강력히 조언**.

### 3.3 Compliance/규제 불충분 (민감 산업)

**전제 조건**: Financial / Healthcare / Government / Legal 은 강한 compliance 요구사항을 가짐.

**실패**: 병원이 HIPAA / PIPA / 환자 권리 검토 없이 CS AI 배포 → 3 개월 후 보건부에 의해 감사 → AI 철수, 벌금, 뉴스에 → AI 계획만 실패하는 게 아니라 전체 IT 거버넌스가 의심받음.

**Tiger AI 거부**: 전담 Compliance Officer / 변호사 검토 없는 민감 산업 → **Phase A 종료 보고서는 「compliance 미검증 → Phase B 중단」 을 표시해야 함**.

### 3.4 임원 이직이 24 개월 로드맵을 깨뜨림

**전제 조건**: Phase C 24 개월은 안정적인 Sponsor 지원이 필요.

**실패**: Phase A 는 CEO 서명; CEO 가 Phase C 월 9 에 떠남 → 새 CEO 가 반대 → Phase C 동결 → NT$ 980만 투자, 부분 출력 (L1-L3) 보유되지만 L4-L5 포기.

**Tiger AI 완화**: Phase C 분기 Gate C exit 메커니즘 = Sponsor 가 바뀌어도, 각 분기는 독립적으로 재평가 가능, sunk-cost-all-lost 가 아님.

---

## 4. 알려진 방법론 한계

### 4.1 스코어링 모델이 심리측정 검증 부족

**상태**: 6 construct × 0-4 스케일과 L1-L5 경계는 **전문가 컨센서스**, Cronbach's α / EFA / CFA / inter-rater reliability 로 **아직 검증되지 않음**.

**잠재적 문제**:

- 동일 회사를 두 컨설턴트가 스코어링하면 L2 vs L3 가 나올 수 있음
- 「50-60 = L2 경계 vs 41-60 = L2」 가 실증적 기반 부족
- Construct 들이 공선성을 가질 수 있음; 실제 요인 수가 다를 수 있음

**Tiger AI 응답**: 보고서는 「expert-consensus 버전, 심리측정 검증 보류」 를 명시 표시; `PILOT_STUDY_PROTOCOL.md` 는 실증 연구 계획; 학술 제출은 claim 강도를 「a proposed framework」 로 낮춰야 함.

### 4.2 케이스 라이브러리 Evidence Level

**상태**: 7 케이스는 Evidence Level 2 의 **익명화된 합성** (Tool 8.9 별).

**잠재적 문제**: 고객이 「이 숫자들은 실제인가 조작인가」 물을 수 있음. ROI ~358%, 결함률 3.2 → 2.0% 는 **어떤 단일 고객의 계약 commitment 로도 사용할 수 없음**.

**Tiger AI 응답**: 각 케이스 헤더는 Evidence Level 과 Composite 성격 표시; SOW 는 고객 자신의 베이스라인 사용, 케이스 숫자 아님; 실제 L3-L5 종단 케이스로 점진적 교체.

### 4.3 Tiger AI L1-L5 인지도 아직 새로움

**상태**: Tool 2.5 self-qualification 9/10; Condition 6 (광범위한 업계 인식) 은 △ 부분.

**잠재적 문제**: 초기 접촉자가 「APQC, SCOR 는 국제적으로 인정 — Tiger AI L1-L5 는 어떤 권위?」 라고 물음. 학술 인용이 임계 질량에 도달하지 못함.

**Tiger AI 응답**: 오픈소스 (Apache 2.0 + GitHub); ISO/IEC 워킹 그룹 / IEEE AI Maturity 표준 논의와 적극적으로 engage; 학술 파트너 기관과 공동 연구 구축 (구체적 파트너는 MOU 체결 후 공개).

---

## 5. 컨설턴트 레벨 Anti-Patterns (내부 실패)

### 5.1 Phase A 건너뛰기 → Phase B-C 직접 서명

**증상**: 세일즈 압박 → Phase A 건너뛰기 → 6 개월 engagement 직접 서명.
**결과**: 고객 서명된 As-Is / RM / Ideal 없음 → Stage 4+ 에서 고객이 「이것은 우리가 원한 게 아니다」 부인 가능 → 컨설턴트 수세.
**규율**: **Phase A 는 절대 건너뛰지 않음**. 그것은 이후 모든 것의 앵커.

### 5.2 고객의 Ideal Practice 를 고객을 위해 작성

**증상**: 시간 절약을 위해, 컨설턴트가 고객이 서명할 Ideal Practice 를 작성.
**결과**: 고객이 ownership 을 느끼지 못함 → 나중에 각 항목에 도전 → 추론 체인 붕괴.
**규율**: **Tool 3.6 Co-Creation Workshop 6 단계를 실행해야 함**. 독립 투표, 집단 컨센서스, reality check, definition table, 3 자 서명 — 어떤 단계도 건너뛸 수 없음.

### 5.3 L1 Self-Report 만 기반 보고서

**증상**: 작성 서두름 → 모든 결론이 고객 자체 설문에서.
**결과**: 고객 내부 감사 / 모회사에 의해 감사 → 「insufficient evidence」 → 전체 프로젝트 반환.
**규율**: Tool 8.9 Evidence Hierarchy 별, **모든 주요 결론은 L3+ (system log) 지원이 필요**. 각 단락이 `[E:L#]` 표시.

### 5.4 Risk 를 Gap Analysis 에 섞음

**증상**: Stage 4 챕터가 「이 위험은 높음, 권장하지 않음」 주관적 판단을 섞음.
**결과**: Stage 4 가 주관적이 됨 → 고객이 「왜 위험하다고 생각하는가」 도전 → 챕터 재작성.
**규율**: **Stage 4 = 객관적 gap 인벤토리, 위험 평가 아님**. 위험은 Stage 8 Risk Register 에 속함.

### 5.5 Gate C 에서 분기 Stage 2 레이더 재방문 건너뛰기

**증상**: 구현 중, PoC 에 집중, 매 분기 진행만 보고, 레이더 재방문 없음.
**결과**: PoC 완료되지만 구조적 완전성 변화 없음 → 24 개월 후 「실제로 개선했나?」 답변 불가.
**규율**: **분기 Gate C 는 레이더를 재방문해야 함**. 하지 않음 = 컨설턴트 과실.

---

## 6. Hard Refusal Conditions

Tiger AI 는 다음 조건 하에서 Phase C 서명을 **거부해야 함** (고객이 원해도):

- [ ] **Phase A + B 미완료** → 서명된 Ideal Practice 없음 → Phase C 거부
- [ ] **AI Champion 자리잡음 확인 없음** → Phase C 거부
- [ ] **타겟 Phase 에 IT FTE 불충분** → 지연 + IT 먼저 추가를 강력 권고
- [ ] **민감 산업에 Compliance Officer / 변호사 검토 없음** → Phase C 거부
- [ ] **Sponsor 자리잡음 없음 (명확한 CEO 지원 없음)** → Phase C 거부
- [ ] **고객이 레벨 건너뛰기를 원함 (예: L1-L3 → L4-L5 건너뛰기)** → 거부, Phase 1 기반 요구
- [ ] **현재 phase 에 예산 불충분** → 거부, 스코프 축소 조언

---

## 7. Customer Exit Protocol

Phase A / B / C 중 어느 것이 실패하면, Tiger AI 는 약속:

1. **Phase A 실패**: 고객은 mid-engagement 보고서 + 인터뷰 요약 + 레이더 보유 → **자체 실행 또는 다음 컨설턴트 고용 가능**
2. **Phase B 실패**: 완전 보고서 + 서명된 Ideal Practice 테이블 보존 → **다른 컨설턴트로 이전 가능**
3. **Phase C 중간 실패 (분기 Gate C 중단 결정)**: 완료된 Phase 보존 + 거버넌스 문서 보존 + 코드 / Skills / Workflow 완전히 고객에게 이전 (컨설턴트는 **고객 자산을 보유하지 않음**)
4. **고객 자산 인질 잡지 않음**: [`../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md`](../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md) 7 Pillars #1 「Client Hosts」 별

---

## 8. 본 문서 사용법

| 역할 | 사용 |
| --- | --- |
| **컨설턴트 내부 훈련** | 필수 온보딩 읽기; 분기 팀 리뷰 「지난 분기 어떤 failure pattern 에 부딪혔는지」 |
| **고객과 서명 전** | 컨설턴트가 본 doc 을 적극 공유 → 고객은 「이 컨설턴트는 성공만 팔지 않고, 실패를 정직히 논의한다」 신뢰 |
| **학술 제출** | 방법론 비판성 / 반증 가능성의 증거로 인용 |
| **규제 / 입찰 문서** | 위험 평가 + 완화 증거로 첨부 |

> **정직하게 실패 논의 = 세일즈 스킬의 최고 형태**. 고객은 「보장된 성공」 이 아니라 「실패할 때 무엇을 할지 우리는 안다」 를 삼.

---

라이선스 & 인용

이 문서는 Apache License 2.0; [`../NOTICE`](../NOTICE) 귀속이 보존되는 한, 사용, 수정, 상용화 가능.
