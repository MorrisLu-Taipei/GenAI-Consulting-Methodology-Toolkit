# AI Governance Alignment: Tiger AI 방법론 vs 국제 AI Governance 프레임워크

> 🌐 언어: [繁體中文](AI_GOVERNANCE_ALIGNMENT.md) ｜ [English](AI_GOVERNANCE_ALIGNMENT_EN.md) ｜ [Deutsch](AI_GOVERNANCE_ALIGNMENT_DE.md) ｜ [Français](AI_GOVERNANCE_ALIGNMENT_FR.md) ｜ [Español](AI_GOVERNANCE_ALIGNMENT_ES.md) ｜ [日本語](AI_GOVERNANCE_ALIGNMENT_JA.md) ｜ 한국어
>
> Apache License 2.0 · 저자: Morris Lu · Tiger AI

마지막 업데이트: 2026-05-16

---

> **이 문서가 답하는 것**: Tiger AI 방법론은 국제 AI Governance 프레임워크 (NIST AI RMF / EU AI Act / ISO/IEC 42001 / OECD AI Principles / Taiwan AI Basic Act / Singapore Model AI Governance) 에 어떻게 매핑되는가? 이사회 / 컴플라이언스 / 규제 기관은 각 프레임워크에서 구체적인 착륙 지점이 필요.
>
> BPM / 컨설팅 / AI-maturity alignment 는 [`../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) 에. **이 문서는 AI Governance 에 집중**, 특히 L4-L5 제도적 신뢰성.

---

## 1. 왜 L4-L5 가 공식 AI Governance Alignment 가 필요한가

L4 Autonomous Agent + L5 Multi-Agent Organization = AI 가 실시간 인간 감독 없이 비즈니스 액션을 실행.

이사회 / 규제 기관은 세 가지 의무 질문을 한다:

1. **누가 책임을 지는가**? AI 가 실패할 때 누가 법적 / 윤리적으로 책임지는가?
2. **어떤 early-warning 메커니즘**? 무엇이 고위험 결정에 대한 인간 개입을 트리거하는가?
3. **어떻게 감사되는가**? 제3자가 AI 행동을 독립적으로 검증할 수 있는가?

답변은 이사회, 컴플라이언스, 규제 기관에 수용 가능하도록 **국제적으로 인정된 거버넌스 프레임워크**에 매핑되어야 함.

---

## 2. 8 단계 × 메인스트림 AI Governance 프레임워크

| 거버넌스 프레임워크 | 출처 / 성격 | 커버되는 Tiger AI 단계 |
| --- | --- | --- |
| **NIST AI RMF** | US NIST, 2023 / 자발적이지만 광범위 채택 | Govern→Stage 8; Map→Stage 1-2; Measure→Stage 4+8; Manage→Stage 6-8 |
| **EU AI Act** | EU, 2024 / 의무 규제 | High-risk AI 는 L4-L5 에 매핑; 투명성→Stage 8 Audit; HITL→모든 단계 |
| **ISO/IEC 42001:2023 AI Management System** | ISO, 2023 / 인증 가능 | AI policy→Stage 8; risk→Stage 4+8; 지속적 개선→Phase C |
| **ISO/IEC 23894:2023 AI Risk Management** | ISO / 위험 집중 | Risk Register→Stage 8 |
| **OECD AI Principles** | OECD+회원국 / 정책 원칙 | 5 원칙 → Tool 7.2 + 8.8 |
| **Taiwan AI Basic Act (초안)** | Taiwan 입법원, 심의 중 | Taiwan 고-컴플라이언스 고객에 매핑 |
| **Singapore Model AI Governance Framework** | IMDA / 자발적 | 4 pillars → Stage 7 To-Be + Stage 8 |
| **US AI Bill of Rights** | 백악관 / 정책 성명 | 5 보호 → Tool 8.8 Ethics + 고객 데이터 보호 |

---

## 3. NIST AI RMF (가장 중요한 글로벌 레퍼런스)

NIST AI RMF 는 **가장 광범위 채택된** AI Governance 프레임워크. 4 핵심 기능:

### 3.1 Govern

**NIST 요구**: org-level AI policy, 역할, 책임, 문화.

**Tiger AI**: Stage 8 §12.1 RACI 매트릭스; Tool 8.8 AI Ethics 체크리스트 15 항목; 4 층 아키텍처 Layer 1 Governance (Policy / Ethics / Compliance / Risk Committee / Audit Owner); Tool 3.6 고객 3 자 서명 = 기업 레벨 서면 commitment.

### 3.2 Map

**NIST 요구**: AI 시스템 컨텍스트, 위험, 이해관계자의 인벤토리.

**Tiger AI**: Stage 1 As-Is (인터뷰, Systems Inventory, AI Usage Inventory, Swimlane); Tool 2.2 RM Mapping; Tool 2.6 + 2.7 Component Map + 4 층.

### 3.3 Measure

**NIST 요구**: AI 시스템 성능, 영향, 위험 정량화.

**Tiger AI**: Stage 2 레이더 0-4 스코어링; Stage 4 Impact × Effort; Stage 8 Tool 8.5 Value Tracking Matrix (5 차원); Tool 8.9 Evidence Hierarchy (L1-L5 evidence strength); 분기 Gate C 레이더 재방문.

### 3.4 Manage

**NIST 요구**: 위험 완화, 모니터링, 지속적 개선.

**Tiger AI**: Stage 6 Phased Goals + Stage Gate Criteria; Stage 7 Human-AI Collaboration + HITL 노드; Stage 8 Tool 8.6 Risk Register; Tool 8.7 Audit Log; Phase C 24 개월 분기 리뷰.

> **전체**: NIST AI RMF 4 기능은 Tiger AI 8 단계에 완전히 착륙, **NIST 컴플라이언스 문서를 직접 생성**.

---

## 4. EU AI Act (의무 규제)

EU AI Act 는 AI 를 4 위험 티어로 분류: Unacceptable / High-risk / Limited / Minimal.

### 4.1 위험 분류 매핑

| EU AI Act Tier | Tiger AI L-level | 요구되는 거버넌스 |
| --- | --- | --- |
| **Unacceptable** (social scoring, real-time biometric ID 등) | ❌ Tiger AI **지원 거부** | — |
| **High-risk** (HR, credit, medical, education, judicial, critical infrastructure) | 주로 L4-L5 시나리오 | 의무 risk assessment + 투명성 + human oversight + post-market monitoring |
| **Limited** (chatbots, deepfake) | 주로 L1-L3 시나리오 | 투명성 의무 (「AI-generated」 표시) |
| **Minimal** (spam filtering 등) | 주로 L1-L2 시나리오 | 일반 의무 |

### 4.2 High-Risk AI Article Alignment

| EU AI Act Article | Tiger AI Mapping |
| --- | --- |
| **Art. 9 Risk Management System** | Stage 8 Tool 8.6 Risk Register |
| **Art. 10 Data Governance** | Tool 8.7 Audit Log + Tool 8.4 Permission Matrix |
| **Art. 11 Technical Documentation** | 완전한 14 섹션 컨설팅 보고서 + 4 층 아키텍처 문서 |
| **Art. 12 Record-Keeping (logs)** | Tool 8.7 Audit Log 7 event types |
| **Art. 13 Transparency** | Tool 8.8 「AI-generated marking」 + 공개 Ideal Practice 서명 |
| **Art. 14 Human Oversight** | Tool 7.2 Human-AI Collaboration + HITL 노드 + Reviewer Workflow |
| **Art. 15 Accuracy, Robustness, Cybersecurity** | Stage 8 Tool 8.5 Value Tracking (품질 dim) + Audit Log + Security |
| **Art. 17 Post-Market Monitoring** | Phase C 분기 Gate C + Stage 2 레이더 재방문 + 5 차원 value tracking 종단 |
| **Art. 26 Quality Management System** | ISO/IEC 42001 alignment (§5 참조) |
| **Art. 72 Serious Incident Reporting** | Tool 8.8 Ethics §11 「AI system incident response」 |

> **EU 운영 고객**: Tiger AI 방법론 산출물 (완전한 14 섹션 보고서 + 거버넌스 문서) 은 EU AI Act 컴플라이언스 증거 패키지로 작동.

---

## 5. ISO/IEC 42001:2023 AI Management System

ISO 42001 은 첫 **제3자 인증 가능** AI management system 표준. 구조는 ISO 9001 / 27001 을 반영.

### 5.1 ISO 42001 섹션 매핑

| ISO 42001 Section | Tiger AI Mapping |
| --- | --- |
| **4. Context of the Organization** | Stage 1 As-Is + Stage 2 Reference Model |
| **5. Leadership** | Sponsor + AI Champion 역할 정의 (RACI) + AI Policy 서명 |
| **6. Planning** | Stage 5 Problem Definition + Stage 6 Phased Goals + Tool 6.3 Absorption |
| **7. Support** | Change Management Playbook + 훈련 계획 + 리소스 계획 |
| **8. Operation** | Stage 7 To-Be Operating Model + Human-AI Collaboration + HITL |
| **9. Performance Evaluation** | Tool 8.5 Value Tracking Matrix + Tool 8.7 Audit Log + 분기 Gate C 레이더 |
| **10. Improvement** | Phase C 분기 리뷰 + Cases-as-Benchmarks 축적 |
| **Annex A Controls** | Tool 8.4 Permission + Tool 8.6 Risk + Tool 8.7 Audit + Tool 8.8 Ethics |

> **목표**: ISO/IEC 42001 인증을 추구하는 기업은 Tiger AI 산출물을 management-system 문서로 사용 가능. Tiger AI 는 **모든 ISO 42001 섹션을 완전 커버**.

---

## 6. OECD AI Principles (5 원칙)

OECD AI Principles 는 G20, APEC 에 의해 광범위 채택.

| OECD 원칙 | Tiger AI Mapping |
| --- | --- |
| **1. Inclusive growth, sustainable development and well-being** | Stage 8 Tool 8.5 Value Tracking 이 「employee experience」 포함; Change Management 가 「역할 업그레이드, 교체 아님」 포함 |
| **2. Human-centered values and fairness** | Tool 8.8 Ethics §9 bias / discrimination assessment; Tool 7.2 HITL 의무 |
| **3. Transparency and explainability** | Tool 8.7 Audit Log + Tool 8.8 §7 「AI-generated marking」 + 완전 evidence trail |
| **4. Robustness, security and safety** | Stage 8 Risk Register + Tool 8.4 Permission + 배포 모드 (Hybrid / On-Prem 3 옵션) |
| **5. Accountability** | RACI 매트릭스 + 「**고객 서명된 Ideal Practice 3 자 서명**」 + Reviewer sign-off |

---

## 7. Taiwan AI Basic Act (초안)

Taiwan 입법원 AI Basic Act 심의 중 (2026/05 기준). Tiger AI 방법론은 **주요 조항과 정렬**:

| 초안 하이라이트 | Tiger AI Mapping |
| --- | --- |
| **AI 제품/서비스에 risk grading 필요** | Stage 1-2 식별 + 4 층 아키텍처 + Tool 8.6 Risk Register |
| **모델 훈련 위의 PII 보호** | Tool 8.8 §2 PII 를 LLM 에 보내지 않음 / redacted; 고민감도는 배포 기본 on-prem |
| **알고리즘 투명성과 설명 가능성** | Tool 8.7 Audit Log + 8.8 §7 AI 표시 |
| **사용자 권리 보호** | Tool 8.8 §5 직원은 일이 AI 처리됨을 알 권리 |
| **운영자 Accountability** | RACI + Tool 8.8 §8 IP 귀속 |
| **정부 규제 권한** | Tool 8.7 Audit Log retention 이 정부 감사 지원 |

⚠️ Taiwan AI Basic Act 아직 통과 안 됨. 이 alignment 는 최종 텍스트로 업데이트.

---

## 8. Singapore Model AI Governance Framework

Singapore IMDA 자발적 프레임워크, 4 pillars:

| Singapore Pillar | Tiger AI Mapping |
| --- | --- |
| **1. Internal Governance Structures** | Layer 1 Governance + RACI |
| **2. Determining Level of Human Involvement** | Tool 7.2 Human-AI Collaboration (HITL 노드) |
| **3. Operations Management** | Tool 8.4-8.7 완전 세트 (Permission / Value / Risk / Audit) |
| **4. Stakeholder Interaction & Communication** | Tool 8.2 Change Management Playbook + Stakeholder Map |

---

## 9. 규제 / 컴플라이언스 산출물 Map

고객이 규제 / 컴플라이언스 / 내부 감사에 직면할 때, 어떤 Tiger AI 산출물을 직접 제출 가능한가:

| 규제 필요 | 직접 Tiger AI 산출물 |
| --- | --- |
| AI risk assessment | Stage 4 Gap + Tool 8.6 Risk Register |
| AI policy | Tool 8.8 Ethics 체크리스트 15 항목 + AI Policy 문서 |
| Audit evidence package | Tool 8.7 Audit Log + 분기 Gate C 로그 + Stage 2 레이더 before/after |
| 제3자 감사 준비 | 완전한 14 섹션 보고서 + 4 층 아키텍처 + 4 권위 문서 |
| ROI / 이익 입증 | Tool 8.5 Value Tracking 5 차원 + 종단 KPI |
| 사고 대응 흐름 | Tool 8.8 §12 + Tool 8.6 Risk Register 트리거 |
| 직원 훈련 기록 | Change Management 훈련 기록 + Tool 8.8 §14 |

---

## 10. 인증 / Labeling 권장

방법론 성숙도에 기반하여, Tiger AI 고객은 다음 고려 가능:

| 인증 | 적용 대상 | 예상 타임라인 |
| --- | --- | --- |
| **ISO/IEC 42001 AI Management System** | L3+ 고객 (완전 거버넌스 보유) | 6-12 개월 |
| **ISO/IEC 27001 ISMS** | 모든 고객 (보안 베이스라인) | 6-12 개월 |
| **SOC 2 Type II** | US / 다국적 서비스 고객 | 6-12 개월 |
| **EU AI Act CE Marking** (High-risk) | EU 운영 + High-risk AI 시스템 | 12-24 개월 |

> Tiger AI 산출물은 **인증 문서 베이스의 90%** 로 작동. 실제 인증은 제3자 감사 필요.

---

## 11. 관련 문서

| 문서 | 관계 |
| --- | --- |
| [`../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) | 컨설팅 펌 / BPM / AI maturity 프레임워크와 정렬; 이 문서는 AI Governance 추가 |
| [`../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | 왜 방법론이 토론에 견디는지 |
| [`FAILURE_PATTERNS_EN.md`](FAILURE_PATTERNS_EN.md) | 방법론 failure modes & counter-cases |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Stage 8 | 완전한 거버넌스 툴킷 |

---

## 12. 참고문헌

- NIST (2023). *AI Risk Management Framework (AI RMF 1.0)*.
- European Commission (2024). *Regulation on Artificial Intelligence (EU AI Act)*.
- ISO/IEC (2023). *ISO/IEC 42001:2023 — AI Management System*.
- ISO/IEC (2023). *ISO/IEC 23894:2023 — AI Risk Management*.
- OECD (2019, updated 2024). *OECD AI Principles*.
- The White House (2022). *Blueprint for an AI Bill of Rights*.
- Singapore IMDA (2020). *Model AI Governance Framework, 2nd Edition*.
- 입법원 (심의 중). *Taiwan Artificial Intelligence Basic Act Draft*.

---

라이선스 & 인용

이 문서는 Apache License 2.0; [`../NOTICE`](../NOTICE) 귀속이 보존되는 한, 사용, 수정, 상용화 가능.
