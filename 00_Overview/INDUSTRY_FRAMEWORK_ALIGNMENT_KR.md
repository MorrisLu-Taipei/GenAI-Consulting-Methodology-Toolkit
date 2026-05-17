# Tiger AI 방법론과 업계 프레임워크의 정렬

> 🌐 언어: [繁體中文](INDUSTRY_FRAMEWORK_ALIGNMENT.md) ｜ [English](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) ｜ [Deutsch](INDUSTRY_FRAMEWORK_ALIGNMENT_DE.md) ｜ [Français](INDUSTRY_FRAMEWORK_ALIGNMENT_FR.md) ｜ [Español](INDUSTRY_FRAMEWORK_ALIGNMENT_ES.md) ｜ [日本語](INDUSTRY_FRAMEWORK_ALIGNMENT_JA.md) ｜ 한국어
>
> Apache License 2.0 · 저자: Morris Lu · Tiger AI

최종 업데이트: 2026-05-15

---

> **이 문서가 답하는 것**: Tiger AI 방법론은 메인스트림 컨설팅 펌 (McKinsey / BCG / Bain / Deloitte / Accenture / PwC), 학술 학파 (Rosemann BPM / CMMI / APQC / SCOR / TOGAF / Dragon1), AI 성숙도 프레임워크 (Gartner / MIT / MMC / Forrester) 와 어떻게 관련되는가? 무엇을 중복, 보완, 혁신하는가?
>
> **핵심 입장**: Tiger AI 는 바퀴를 재발명하지 않고 **메인스트림 도구를 통합하고, 업계 클로즈드 루프를 보완하며, GenAI 시대 필수 요소를 추가**. 인용된 모든 프레임워크는 [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md) 에 상세히 기술; 본 문서는 펌 간 매핑.

---

## 1. 이 정렬이 왜 중요한가

| 오디언스 | 얻는 것 |
| --- | --- |
| 대기업 IT/CIO | 「이 방법론은 기존 TOGAF / ITIL / APQC 와 호환」 |
| 다른 펌의 컨설턴트 | 「BCG/Deloitte 출신 — 어떤 도구를 계속 사용하고 어떤 것이 Tiger AI 특유한지 보임」 |
| 학술 리뷰어 | 「Tiger AI 는 주변 과학이 아님 — Rosemann/CMMI/APQC 학파의 어깨 위에 서 있음」 |
| 규제 기관 | 「인용된 표준은 국제적으로 인정됨; AI 거버넌스는 기존 GRC 프레임워크로 매핑」 |
| 클라이언트 임원 | 「우리가 지불하는 것은 업계 베스트 + GenAI 시대 보완, 단일 펌의 독점 방법이 아님」 |

---

## 2. 8 단계 vs. 메인스트림 컨설팅 펌

### 2.1 펌 간 정렬 테이블

| 단계 | Tiger AI | McKinsey | BCG | Bain | Deloitte | Accenture | PwC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **1 As-Is Snapshot** | 40-Q 인터뷰 + Inventory + Swimlane | 7-Step Step 1: Define Problem | Diagnostic Survey | Customer / Process Diagnostics | Business Architecture Discovery | Living Business Diagnostic | Value Creation Diagnostic |
| **2 Reference Model** | APQC + Tiger AI L1-L5 + 4 층 | (드물게 수행) | Capability Maturity Map | (비코어) | TOGAF Capability Assessment | Industry Reference Architecture | Capability Framework |
| **3 Best Practice → Ideal** | Benchmark + Ideal Practice Workshop | Best Practice Research | Strategic Position vs Industry | NPS / Customer Loyalty | Industry Pulse | Industry Benchmarking | Industry Outlook |
| **4 Gap Analysis** | M/B/R + Impact×Effort | Issue Tree + MECE | Importance-Performance Map | Pareto + Lean | Capability Gap Heatmap | Maturity Gap Analysis | Gap Map |
| **5 Problem Definition** | 80/20 + 5 Whys + EPS | Day-1 + SCQ + Pyramid | Strategic Diagnosis | Bain Question Pyramid | Hypothesis-Driven | Outcome-Driven | Issue-Tree Synthesis |
| **6 Phased Goals** | Phased + Absorption | Workplan + Critical Path | Phased Transformation | Bain Way Multi-phase | Imagine-Deliver-Run | Wave Planning | Transformation Wave |
| **7 To-Be Design** | Phased To-Be + Human-AI | To-Be Operating Model | Operating Model Design | Bain Way (Org) | Target Operating Model | Future-State Blueprint | Future Operating Model |
| **8 Implementation & Change** | Roadmap + Change + Value Tracking | Influence Model + 7S | Smart Simplicity | Bain Results Delivery | Diamond Performance | Wired for Change | Project Delivery |

### 2.2 각 펌이 무엇을 기여하는가

- **McKinsey** MECE / Pyramid / Issue Tree 는 **Tiger AI Stage 4-5 도구의 소스** (Frameworks Library 에 수록)
- **BCG** Capability Maturity 사고는 **Tiger AI Stage 2 RM 스코어링을 영감**
- **Bain** Customer / Process Diagnostics 는 **Tiger AI Stage 1 인터뷰 뱅크를 보완**
- **Deloitte** Imagine-Deliver-Run 은 **Tiger AI Stage 6 3 단계와 강하게 일치**
- **Accenture** Wave Planning 은 **Tiger AI Phase 1/2/3 와 일치**
- **PwC** Value Creation Diagnostic 은 **Tiger AI Stage 8 value tracking 에 매핑**

> **결론**: 8 단계 중 어느 것도 Tiger AI 의 「발명」이 아님. **혁신은 이러한 분산된 도구들을 데이터 의존성, 클라이언트 서명, 클로즈드 루프 반증을 갖는 완전한 추론 체인으로 통합하는 데 있음**.

---

## 3. Reference Model 학파 정렬

### 3.1 Tiger AI 4 층 vs. 주요 EA 프레임워크

| 층 | Tiger AI | Dragon1 EA | TOGAF ADM | Zachman | ArchiMate |
| --- | --- | --- | --- | --- | --- |
| **L1 Governance** | AI Governance | Enterprise Governance | (Architecture Vision) | Scope | Motivation + Strategy |
| **L2 Business** | AI Business (L1-L5 여기) | Business(es) | Business Architecture (B) | Business | Business Layer |
| **L3 Information** | AI Information | Information Facilities & Systems | Data + Application (C+D) | System | Application + Information |
| **L4 Technical** | AI Technical | IT Infrastructure(s) | Technology (E) | Technology | Technology + Implementation |

**왜 이 정렬**: 모든 메인스트림 EA 프레임워크는 「**4 추상 층**」으로 수렴 — 우연이 아니라 「추상 × 휘발성」 과학적 축의 필연적 결과 ([`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) §5 참조).

### 3.2 Process Reference Model 정렬

| 유즈 케이스 | Tiger AI 권장 | APQC PCF | SCOR | eTOM | ITIL | CMMI |
| --- | --- | --- | --- | --- | --- | --- |
| **업계 횡단 프로세스** | APQC PCF (기본) | ✓ 13 Cat | — | — | — | — |
| **공급망 / 제조** | SCOR | — | ✓ 6 섹션 | — | — | — |
| **텔레콤 / 구독** | eTOM | — | — | ✓ 3 레벨 | — | — |
| **IT 서비스 관리** | ITIL | — | — | — | ✓ 5 단계 | — |
| **소프트웨어 성숙도** | CMMI | — | — | — | — | ✓ 5 레벨 |
| **AI 채택 성숙도** | **Tiger AI L1-L5 (DIY, 업계 격차 채움)** | — | — | — | — | — |

> **기존 업계 RM 은 AI 채택을 다루지 않음** — 따라서 Tiger AI L1-L5 의 필요성, Tool 2.5 점수 9/10 으로 자체 인증.

### 3.3 BPM Maturity 학파 뿌리

| 개념 | 소스 | Tiger AI 매핑 |
| --- | --- | --- |
| Capability Maturity Levels (5 단계 스케일) | **Rosemann BPM Maturity** (QUT) + CMMI | Stage 2 0-4 스코어링, Tiger AI L1-L5 |
| Process Excellence Characteristics | Rosemann + APQC | Stage 3 Excellence Capability Profile |
| Stage Gates | CMMI + Rosemann | Stage 6 acceptance gates |
| Organizational Absorption | Rosemann (신생 연구) | Tool 6.3 Absorption Assessment |

> **감사**: Prof. Michael Rosemann (QUT) 은 저자의 석사 어드바이저; 본 방법론의 BPM 학파 뿌리는 그의 장기 멘토링에서 직접 옴.

---

## 4. AI 성숙도 프레임워크 정렬

### 4.1 주요 AI 성숙도 프레임워크 매핑

| 프레임워크 | 레벨 | Tiger AI L1-L5 매핑 |
| --- | --- | --- |
| **Gartner AI Maturity Model** | Awareness / Active / Operational / Systemic / Transformational | L1 / L1+L2 / L3 / L4 / L5 |
| **MIT Sloan AI Capability** | Experimenters / Investigators / Pioneers / Empowerment | L1-L2 / L2-L3 / L3-L4 / L5 |
| **McKinsey AI Quotient (AIQ)** | (연속 스케일, 4 드라이버) | Tiger AI 6 차원 레이더로 매핑 |
| **Capgemini DELTA Maturity** | Data / Enterprise / Leadership / Targets / Analysts | 거버넌스 + 배포 축으로 매핑 |
| **Forrester AI Pulse Index** | (3 링: People / Process / Tech) | Tiger AI 4 층 아키텍처로 매핑 |
| **Tiger AI L1-L5** | L1 Chat / L2 Skill / L3 Workflow / L4 Auto Agent / L5 Agent Team | (**스케일 축 L1-L3 + AI 자율 축 L4-L5**) |

### 4.2 Tiger AI L1-L5 의 메인스트림에 대한 추가

| 추가 | 왜 업계에 부족한가 | Tiger AI 가 채움 |
| --- | --- | --- |
| **명시적 도구 매핑** | Gartner/MIT 는 레벨을 추상적으로 기술, 도구 랜딩 없음 | L1=OpenWebUI, L2=Antigravity, L3=n8n, L4=Hermes, L5=ClawTeam |
| **스케일 축과 자율 축 분리** | 업계는 그것들을 혼합, L4-L5 를 흐리게 함 | 스케일 (인간 주도) vs 자율 (AI 주도), 중요 경계 L3→L4 |
| **GenAI 특화 (전통 ML 이 아님)** | 대부분의 프레임워크가 전통 ML / 예측 모델에 머무름 | LLM / Agent / Workflow 패러다임에 완전 집중 |
| **검증 가능한 단계 어셉턴스** | 업계 프레임워크는 주로 자기 평가 스케일 | 각 레벨에 Stage Gate Criteria, 독립 검증 가능 |
| **크로스 RM 듀얼 좌표** | 업계 프레임워크는 단축 | Tiger AI 는 업계 RM (APQC/SCOR) 에 직교, 듀얼 레이더 |

---

## 5. 클래식 분석 도구 정렬

[`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md) 에 상세. 요약:

### 5.1 전략 도구

Porter's 5 Forces (Stage 3), PESTEL (Stage 3), BCG Growth-Share (Stage 3), SWOT (Stage 3/4), Blue Ocean (Stage 7), Wardley Map (Stage 6/7).

### 5.2 문제 분석 도구

MECE (Stage 2/4), Issue Tree (Stage 4/5), Pyramid Principle (Stage 5), SCQ (Stage 5), 5 Whys (Stage 5), Fishbone (Stage 4/5), Hypothesis-Driven (Stage 1-5), 80/20 (Stage 5).

### 5.3 Change Management 도구

Kotter 8 Steps (Stage 8), ADKAR (Stage 8), Stakeholder Map (Stage 8), RACI (Stage 8), Influence Model (Stage 8), 7S (Stage 2/8).

### 5.4 재무 / ROI 도구

NPV/IRR (Stage 8), Payback (Stage 8), Break-Even (Stage 8), Sensitivity Analysis (Stage 8), Balanced Scorecard (Stage 8), OKR (Stage 6/8).

---

## 6. Tiger AI 고유 / 혁신 요소

대부분의 도구는 업계에서 오지만, Tiger AI 는 다음과 같은 **고유한 통합 또는 혁신** 을 가짐:

| 혁신 | 왜 업계에 부족한가 | Tiger AI 디자인 |
| --- | --- | --- |
| **Tiger AI L1-L5 GenAI Adoption RM** | 업계 RM 은 여전히 IT / 전통 ML | LLM/Agent/Workflow 를 위해 특별히 설계된 첫 번째 RM, Tool 2.5 10 조건 중 9/10 충족 |
| **Client Ideal Practice Co-Creation Workshop** | 업계는 Best Practice 벤치마킹을 하지만 드물게 클라이언트 서명 Ideal | Tool 3.6: 클라이언트가 **스스로 서명**, 후속 추론을 부정할 수 없음 |
| **Cases-as-Benchmarks 9 필드 포맷** | 업계 케이스는 대부분 서술적, 갭 계산 없음 | Tool 3.5: 케이스는 의무적으로 9 필드, 클라이언트가 30 분에 자기 계산 |
| **분기별 Stage 2 Radar 루프 백** | 업계 Roadmap 은 대부분 선형, 자기 반증 메커니즘 없음 | Phase C 매 분기 Gate C 는 반드시 레이더 재방문, 구조가 실제로 더 둥근지 검증 |
| **3 단계 계약 모델 + Gate A/B/C 출구** | 업계는 대부분 fixed-scope 대형 계약 | Phase A diagnostic / Phase B strategy / Phase C implementation, 클라이언트가 결정을 단계화 |
| **스케일 축 vs AI 자율 축 직교** | 업계는 단일 축에서 혼합 | L1-L3 스케일 + L4-L5 자율, 중요 L3→L4 경계 |
| **4 층 RM × L1-L5 듀얼 좌표** | 업계는 단축 (RM 이거나 성숙도) | Tiger AI 는 듀얼 축 크로스 매핑 의무화 |
| **프로세스별 명시적 HITL 노드** | 업계는 거버넌스를 말하지만, 드물게 HITL 위치를 명시 | Tool 7.2 각 프로세스가 HITL 노드 + acceptance criteria 로 명시적 표시 |

---

## 7. 일반 클라이언트 질문: 우리 방법론과 충돌하는가?

### 7.1 클라이언트가 TOGAF / Zachman 사용

**충돌 없음**. Tiger AI 4 층은 **TOGAF BDAT** (Business/Data/Application/Technology) 와 직접 일치. 「귀사의 기존 TOGAF 아키텍처 위에 구축하고, GenAI 채택 차원 (L1-L5) 과 분기 레이더 클로즈드 루프를 추가합니다.」 라고 말함.

### 7.2 클라이언트가 ITIL 사용

**충돌 없음**. Tiger AI Stage 8 Audit Log / Permission Matrix / Risk Register 는 ITIL Service Operation 에 직접 연결. 「GenAI 특화 LLM 콜 로그, Reviewer 시뮬레이션, Skill 버전 거버넌스를 보완합니다.」 라고 말함.

### 7.3 클라이언트가 CMMI 사용

**충돌 없음**. Tiger AI L1-L5 와 CMMI 5 레벨은 **친족** — 둘 다 maturity capability 학파 확장. 「CMMI for AI 는 신흥 방향; Tiger AI L1-L5 는 하나의 랜딩 버전입니다.」 라고 말함.

### 7.4 클라이언트가 BCG / McKinsey / Bain 내부 프레임워크 사용

**충돌 없음, 상호 강화**. Tiger AI 는 이러한 펌의 코어 도구 (Issue Tree, MECE, Pyramid, Bain Way) 를 인용. 「귀사의 전략 컨설팅 방법론을 대체하지 않고, GenAI 채택 클로즈드 루프와 4 층 Reference Model 을 추가합니다.」 라고 말함.

### 7.5 클라이언트가 Gartner / Forrester AI Maturity 사용

**충돌 없음, 더 구체적**. Tiger AI L1-L5 는 Gartner 의 5 레벨보다 **더 구체적인 랜딩 도구** (L1=OpenWebUI 등) 를 가짐. 「Gartner 는 ‹Operational AI› 라고 하지만, 우리는 ‹n8n Workflow 3 라이브 + Reviewer 사인오프 비율 95%› 라고 합니다.」 라고 말함.

---

## 8. 학술 인용 정렬

각 파일 References 에 인용. 선정:

### 8.1 BPM / Maturity 학파

- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT. **(코어 이론 뿌리)**
- Paulk, M. et al. (1993). *Capability Maturity Model for Software*. CMU/SEI.
- Curtis, B. et al. (2009). *People CMM*.

### 8.2 Reference Model / Enterprise Architecture

- APQC (2024). *Process Classification Framework Version 7.3*.
- APICS / ASCM. *SCOR Reference Model*.
- TM Forum. *eTOM Business Process Framework*.
- ISACA. *COBIT / ITIL Framework*.
- The Open Group. *TOGAF Standard 9.2*.
- Zachman, J. *Zachman Framework*.
- Dragon1. *Enterprise Architecture Reference Model*.

### 8.3 컨설팅 방법론

- Minto, B. (2009). *The Pyramid Principle*.
- Rasiel, E. (1999). *The McKinsey Way*.
- Bain & Company. *Bain Way / Results Delivery*.
- Iansiti, M., Lakhani, K. (2020). *Competing in the Age of AI*.

### 8.4 Change Management

- Kotter, J. (1996). *Leading Change*.
- Hiatt, J. (2006). *ADKAR*. Prosci.
- Mendelow, A. (1991). *Stakeholder Mapping*.

### 8.5 GenAI 전략

- Gartner. *AI Maturity Model*.
- Davenport, T., Mittal, N. (2022). *All-in on AI*.
- Brynjolfsson, E., McAfee, A. (2014). *The Second Machine Age*.

---

## 9. 클로징: 거인의 어깨 위에 서기 + 업계 클로즈드 루프 보완

Tiger AI 방법론 디자인 철학:

1. **바퀴를 재발명하지 않음**: 전략 분석 (McKinsey), change mgmt (Kotter), 재무 도구 (NPV/IRR), EA 프레임워크 (TOGAF/Dragon1) — 업계의 최고를 사용
2. **통합 + 클로즈드 루프**: 분산된 도구를 데이터 의존성, 클라이언트 서명, 반증 메커니즘을 갖는 완전한 추론 체인으로 묶음
3. **GenAI 격차 채움**: 업계 프레임워크가 LLM/Agent/Workflow 시대를 따라잡지 못함 → Tiger AI L1-L5 + 4 층 + Cases-as-Benchmarks + HITL 디자인이 채움
4. **타인이 재현 가능**: Apache 2.0 + GitHub + 명확한 학술 인용 → 어느 펌의 사적 자산도 아님

> **이것이 「거인의 어깨 위에 서기 + 업계 클로즈드 루프 보완」의 의미** — 클라이언트가 사는 것은 업계 최고 통합 + GenAI 시대 보완, 단일 펌의 독점 방법이 아님.

---

## 10. 관련 문서

| 문서 | 관계 |
| --- | --- |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) §8 | 본 문서 §2 의 컴팩트 버전 (vs McKinsey/BCG/Gartner/MIT) |
| [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) | 8 단계가 실제 인게이지먼트에서 어떻게 진행되는가 |
| [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY_EN.md) | 50+ 프레임워크 상세 (본 문서 = 정렬 맵; 그 파일 = 프레임워크 사전) |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) | 단계별 도구 테이블 |

---

라이선스 & 인용

본 문서는 Apache License 2.0; [`../NOTICE`](../NOTICE) 귀속이 보존되는 조건으로 사용, 수정, 상업화 가능.
