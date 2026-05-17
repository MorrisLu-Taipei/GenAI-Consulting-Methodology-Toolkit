# 학술 이론 기반: Tiger AI 방법론의 일곱 이론적 기둥

> 🌐 언어: [繁體中文](ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [English](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) ｜ [Deutsch](ACADEMIC_THEORETICAL_FOUNDATIONS_DE.md) ｜ [Français](ACADEMIC_THEORETICAL_FOUNDATIONS_FR.md) ｜ [Español](ACADEMIC_THEORETICAL_FOUNDATIONS_ES.md) ｜ [日本語](ACADEMIC_THEORETICAL_FOUNDATIONS_JA.md) ｜ 한국어
>
> Apache License 2.0 · 저자: Morris Lu · Tiger AI

마지막 업데이트: 2026-05-16

---

> **목적**: 파일에 분산된 Tiger AI 방법론의 학술 이론적 기반을 **하나의 권위 있는 문서**로 통합. 어떤 학자 / 규제 기관 / 진지한 컨설턴트가 「이론적 기반이 무엇인가」 묻든, 본 문서가 답.
>
> **핵심 주장**: Tiger AI 방법론은 단순한 컨설팅 실천이 아닌 **일곱 이론의 엔지니어링된 통합**.

---

## 1. 이론 맵 개관

| 이론 | 창시자 / 고전 참조 | 해결된 핵심 문제 | Tiger AI 매핑 |
| --- | --- | --- | --- |
| **Capability Maturity & BPM Maturity** | Paulk et al. (1993) CMMI; Rosemann & de Bruin (2005) | 조직 능력을 구조적으로 어떻게 스코어할까? | L1-L5 + Stage 2 스코어링 |
| **Absorptive Capacity** | Cohen & Levinthal (1990) | 조직이 새 능력 **흡수**에서 왜 그렇게 다른가? | Tool 6.3 Organizational Absorption Assessment |
| **Task-Technology Fit (TTF)** | Goodhue & Thompson (1995) | 어떤 작업이 AI 에 적합 / 부적합한가? | Stage 7 To-Be Design (모든 부서가 L5 에 도달해야 하는 것은 아님) |
| **Dynamic Capabilities** | Teece et al. (1997); Teece (2007) | 조직이 **외부 변화에 빠르게 적응**하는 방법? | Stage 7 + Stage 8 (정적 자동화에서 동적 능력으로) |
| **Sociotechnical Systems & Trust in AI** | Bostrom & Heinen (1977); Dietvorst et al. (2015); Glikson & Woolley (2020) | 인간-AI 협업이 왜 어려운가? Algorithm aversion / complacency | Stage 8 Change Management + HITL |
| **Real Options Theory** | Dixit & Pindyck (1994); McGrath (1997) | 고불확실성 AI 전략 투자를 어떻게 평가? | Stage 8 §13 Value Tracking + ROI |
| **AI-Native Living Book / Executable Knowledge Artifact** | Knuth (1984); Anderson et al. (1995); 본 저자 (2026) | 방법론 자체가 AI 에 의해 실행 가능한가? | AGENTS.md + AI_NATIVE_LIVING_BOOK |

---

## 2. Capability Maturity & BPM Maturity

### 2.1 이론 요약

- **CMMI**: Paulk et al. (1993) 가 SEI 에서 5 레벨 조직 능력 정의 (Initial / Repeatable / Defined / Managed / Optimizing)
- **BPM Maturity Model**: Rosemann & de Bruin (2005, QUT) 가 maturity 를 Business Process Management 로 확장, 6 enabler 추가: Process Awareness / Alignment / Methods / IT / People / Culture

### 2.2 Tiger AI 에 대한 기여

- **L1-L5 두 축**은 BPM Maturity 의 「Process Awareness → Optimization」 로직 상속, GenAI 시대 필수 「**스케일 축 + AI Autonomy 축**」 이중 구조 추가
- **0-4 스케일 + BARS 행동 앵커**는 이 학파에서 유래
- **Stage Gate Criteria** = CMMI 의 「Process Areas」 + 단계 수락

### 2.3 매핑된 파일

- [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §3.0 두 축 이야기
- [`../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md) L1-L5 정의
- [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) 행동 앵커

---

## 3. Absorptive Capacity

### 3.1 이론 요약

- **Cohen & Levinthal (1990)** *Administrative Science Quarterly* 에서: 조직의 「**외부 지식을 식별, 동화, 적용하는 능력**」 이 그 혁신 능력을 결정
- 핵심 요소: **Prior Knowledge + Internal Knowledge Flow**
- Zahra & George (2002) 가 더 4 차원으로 분할: Acquisition / Assimilation / Transformation / Exploitation

### 3.2 Tiger AI 에 대한 기여

- **동일한 AI 기회가 회사마다 매우 다른 결과**를 가져오는 이유 설명 — 차이는 absorptive capacity
- Tool 6.3 Organizational Absorption Assessment 가 이 이론에 직접 매핑
- 「**왜 레벨을 건너뛸 수 없는지**」 강화: L1-L3 건너뛰기 → absorptive capacity 부족 → L4-L5 실패 ([`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md) §2 참조)

### 3.3 Tool 6.3 에 대한 구체적 확장

오리지널 Tool 6.3 6 차원 (Budget / Champion / IT FTE / Governance / Literacy / Change capacity) 에 **2 개 새 차원 추가**:

| 새 차원 | 평가 질문 | 스코어 |
| --- | --- | --- |
| **Prior Knowledge** | 회사가: (a) 과거 BPM / Lean / Six Sigma 경험? (b) 과거 AI / ML / RPA 시도? (c) 내부 소프트웨어 개발 능력? | 0-4 |
| **Internal Knowledge Flow** | 부서 간: (a) 일상적 부서간 리뷰? (b) 공유 문서 플랫폼? (c) 내부 멘토 / 인스트럭터 시스템? | 0-4 |

→ High Prior Knowledge + High Knowledge Flow 회사는 더 공격적인 Phase 1/2/3 처리 가능; 반대로, 타임라인 연장 필요.

### 3.4 참고문헌

- Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly*, 35(1), 128-152.
- Zahra, S. A., & George, G. (2002). Absorptive capacity: A review, reconceptualization, and extension. *Academy of Management Review*, 27(2), 185-203.

---

## 4. Task-Technology Fit (TTF)

### 4.1 이론 요약

- **Goodhue & Thompson (1995)** *MIS Quarterly* 에서: 기술이 성과를 개선하는 정도는 「**작업 수요 ↔ 기술 능력**」 fit 에 의존
- 작업 분류: **Routine (반복적, 예측 가능) vs Non-routine (judgment-heavy, 창의적)**

### 4.2 Tiger AI 에 대한 기여

**모든 부서가 L5 에 도달해야 하는 것은 아님**. 작업 특성으로 각 부서의 적절한 L-level 종점 결정:

| 작업 유형 | 적절한 종점 | 근거 |
| --- | --- | --- |
| Highly Routine (CS FAQ, 청구서 분류) | L3-L4 | 높은 AI fit; 낮은 HITL 비용 |
| Medium Routine + 부분 판단 (영업 제안, 월말 이상) | L2-L3 + HITL | AI 드래프트 + 인간 확인; 효율과 위험 균형 |
| Highly Non-routine (M&A 평가, 전략 결정) | L1-L2 (개인 어시스턴트) | AI 지원, 인간 주도; L4-L5 푸시는 판단 품질 해침 |
| Highly compliance-sensitive (법무, 의료 진단) | L2-L3 + strong HITL | 규제 위험 너무 높음; L4-L5 부적합 |

### 4.3 매핑된 파일 / Tools

- Stage 7 Tool 7.2 Human-AI Collaboration → TTF 매트릭스가 프로세스별 AI 관여 결정
- Tool 6.3 에 **TTF Assessment Worksheet 추가** → 부서별 TTF 스코어, Ideal L-level 결정

### 4.4 참고문헌

- Goodhue, D. L., & Thompson, R. L. (1995). Task-technology fit and individual performance. *MIS Quarterly*, 19(2), 213-236.
- Zigurs, I., & Buckland, B. K. (1998). A theory of task/technology fit and group support systems effectiveness. *MIS Quarterly*, 22(3), 313-334.

---

## 5. Dynamic Capabilities

### 5.1 이론 요약

- **Teece, Pisano & Shuen (1997)** *Strategic Management Journal* 에서: 경쟁 우위는 「**내부 및 외부 자원의 통합, 구축, 재구성**」 에서 비롯
- **Teece (2007)** 이 세 마이크로 기초로 분해:
  1. **Sensing**: 기회와 위협 식별
  2. **Seizing**: 결정과 자원 할당
  3. **Transforming**: 기회 활용을 위한 조직 재구성

### 5.2 Tiger AI 에 대한 기여

**정적 자동화에서 → 동적 적응 능력**. Tiger AI 는 기존 APQC 프로세스를 AI 화할 뿐만 아니라 **외부 변화에 지속적으로 적응하는 새로운 능력을 클라이언트에게 구축**:

| Dynamic Capability | Tiger AI 매핑 |
| --- | --- |
| **Sensing** | L3 Workflow + L4 Agent 가 시장 / 고객 / 프로세스 신호를 지속 모니터 |
| **Seizing** | Phase 1/2/3 분해 = sensed 신호를 구체적 투자 결정으로 변환 |
| **Transforming** | L5 Multi-Agent Organization + 분기 Gate C 레이더 = 지속적 조직 재구성 |

### 5.3 Stage 7 에 대한 구체적 확장

Stage 7 To-Be Design 에 **Dynamic Capability Worksheet 추가**:

```
Teece (2007) 세 마이크로 기초별, 각 To-Be 설계는 답해야:

1. Sensing: 이 AI 설계가 회사가 「sense」 하도록 돕는 외부 신호는 무엇?
   예: complaint Agent 가 고객 만족도 트렌드 모니터
2. Seizing: 신호가 나타날 때 회사가 얼마나 빠르게 「seize」 할 수 있나?
   예: Quick Win complaint response 5d → 1d 가 고객 손실 윈도우를 압축
3. Transforming: 이 AI 가 조직 「self-reconfiguration」 을 어떻게 가능하게 하나?
   예: L5 ClawTeam 부서간 = 조직이 특정 시니어 스태프에 더 이상 의존하지 않음
```

→ 이 3 가지에 답하지 않는 To-Be 는 단지 「현상 유지를 자동화」, 진정한 트랜스포메이션이 아님.

### 5.4 참고문헌

- Teece, D. J., Pisano, G., & Shuen, A. (1997). Dynamic capabilities and strategic management. *Strategic Management Journal*, 18(7), 509-533.
- Teece, D. J. (2007). Explicating dynamic capabilities. *Strategic Management Journal*, 28(13), 1319-1350.

---

## 6. Sociotechnical Systems & Trust in AI

### 6.1 이론 요약

- **Sociotechnical Systems Theory** (Bostrom & Heinen, 1977): 조직 성과 = **사회 시스템 + 기술 시스템**의 공동 출력; 단독으로 최적화 불가
- **Algorithm Aversion**: Dietvorst, Simmons & Massey (2015) *JEP* 에서: 사람들은 **알고리즘이 잘못되는 것을 본 후 알고리즘보다 더 나쁜 인간 판단을 선호**, 알고리즘이 더 정확한 것을 알면서도
- **Automation Complacency**: Parasuraman & Manzey (2010): 자동화에 대한 과신이 경계 상실을 야기하여 더 큰 인시던트로 이끔
- **Trust in AI**: Glikson & Woolley (2020) 이 인지적 + 감정적 신뢰 통합

### 6.2 Tiger AI 에 대한 기여

인간-AI 협업의 진정한 챌린지는 「대체 두려움」 만이 아니라, 또:

1. **Algorithm Aversion**: 첫 AI 오류 후 직원이 집단적으로 거부 → L3-L4 출시 후 흔함
2. **Automation Complacency**: 직원이 리뷰를 중단 → HITL 실패 → 더 큰 인시던트
3. **Accountability 모호성**: AI 가 잘못하면 누가 책임? 직원이 비난 두려워함 → 심리적 안전성 갭
4. **전문 정체성 재형성**: 「Doer」 에서 「Reviewer」 로 → 인지 부하와 성취감 시프트

### 6.3 Stage 8 Change Management 에 대한 확장

Tool 8.2 에 2 개 새 저항 유형 추가:

| 저항 유형 | 전형적 신호 | 처리 |
| --- | --- | --- |
| **Algorithm Aversion** | 한 번의 AI 오류 후 집단적 거부 | 오류율 투명성 (인간 vs AI) + 점진적 신뢰 구축 (저위험 시나리오로 시작) |
| **Automation Complacency** | 직원이 리뷰 없이 승인 | Reviewer Workflow 에서 의무 무작위 샘플링 + 오류 감지 후 재훈련 |

### 6.4 HITL 설계 (Tool 7.2) 에 대한 확장

**심리적 안전성과 accountability 컬럼 추가**:

| 프로세스 | HITL Node | **Accountability Statement** | **심리적 안전성** |
| --- | --- | --- | --- |
| CS reply | 전송 전 100% 인간 리뷰 | AI 드래프트 책임 = AI Champion; 최종 응답 책임 = CS 직원 | 직원은 「AI 가 잘못이면 리뷰 없이 거부」 권리를 가지며 비난 없음 |
| Process root cause | 액션 전 100% 인간 리뷰 | AI 가설 책임 = Agent 개발자; 액션 책임 = 프로세스 매니저 | 매니저는 「AI 제안 거부」 공식 SOP 보유 |

### 6.5 참고문헌

- Bostrom, R. P., & Heinen, J. S. (1977). MIS problems and failures: A socio-technical perspective. *MIS Quarterly*, 1(3), 17-32.
- Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion. *JEP: General*, 144(1), 114-126.
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation. *Human Factors*, 52(3), 381-410.
- Glikson, E., & Woolley, A. W. (2020). Human trust in artificial intelligence. *Academy of Management Annals*, 14(2), 627-660.
- Edmondson, A. (1999). Psychological safety and learning behavior in work teams. *ASQ*, 44(2), 350-383.

---

## 7. Real Options Theory

### 7.1 이론 요약

- **Dixit & Pindyck (1994)** *Investment Under Uncertainty* 에서: 고불확실성 투자 가치 = 즉시 실행 가치 + 「**미래 옵셔널리티**」 가치
- **McGrath (1997)** 이 전략에 적용: 「**오늘의 투자가 미래 확장할 권리를 보존**」
- 불확실성 하 NPV 과소평가에 반박: NPV 는 확실성을 가정하지만, 관리적 유연성은 불확실성 하 높은 가치

### 7.2 Tiger AI 에 대한 기여

L4-L5 고불확실성 AI 투자는 **전통 NPV / IRR 에 의해 필연적으로 과소평가됨** (18-24 개월 현금 흐름이 불확실하기 때문). Real Options 가 더 나은 프레이밍 제공:

| 투자 | NPV 뷰 (과소평가) | Real Options 뷰 (정당화) |
| --- | --- | --- |
| Phase 1 Foundation (NT$ 280 만) | 현금 흐름 불명확 → NPV ≈ 0 | 「**미래 더 낮은 비용으로 L4-L5 를 빠르게 확장하는 옵션**」 구매, NT$ 280 만보다 훨씬 가치 |
| L1 전사 Chat AI | 단기 ROI 불명확 | 직원 AI 리터러시 = **모든 미래 AI 응용의 기초 자산** |
| L2 Skill Library | ROI 불가시 | 지식 codification = 회사의 「**미래에 여러 AI 응용을 동시에 플러그인**」 하는 옵션 |
| L4 Hermes Agent Pilot | 하나의 Agent 가 가치있나? | Pilot = L4 학습 = L5 ClawTeam 으로의 옵션 |

### 7.3 Real Options Valuation (단순화 Black-Scholes)

L4-L5 투자에 대해, 다음을 통해 추정:

```
Option Value = max(0, future_payoff - exercise_cost)

여기서:
  future_payoff = 옵션 행사로부터 수익 (예: L5 로 확장)
  exercise_cost = 행사 시 비용 (예: Phase 3 투자)
  volatility (σ) = 시장 / 기술 불확실성
  time-to-expiration = 기회 윈도우
```

⚠️ 정확한 Black-Scholes 불필요; **내러티브 레벨 논증으로 CFO 를 설득해 「단기 ROI 불가시지만 장기 가치있는」 투자를 정당화하기 충분**.

### 7.4 Stage 8 §13 Value Tracking 에 대한 확장

오리지널 5 차원 (Time / Quality / Scale / Risk / Assets), **6 번째 차원 추가**:

| 차원 | 내용 |
| --- | --- |
| **Strategic Options** | 이 투자가 보존한 「**미래 행사권**」 은 무엇? 예: L1 foundation → 미래 L4 빠르게 확장 가능; L2 Skill Library → 임의의 미래 Agent 플러그인 가능; L3 Workflow → 임의의 새 시스템 통합 가능 |

### 7.5 참고문헌

- Dixit, A. K., & Pindyck, R. S. (1994). *Investment Under Uncertainty*. Princeton University Press.
- McGrath, R. G. (1997). A real options logic for initiating technology positioning investments. *Academy of Management Review*, 22(4), 974-996.
- Trigeorgis, L. (1996). *Real Options*. MIT Press.

---

## 8. AI-Native Living Book as Executable Knowledge Artifact

### 8.1 이론 요약

- **Literate Programming**: Knuth (1984) 가 코드와 문서가 단일 「인간 가독 + 기계 실행 가능」 문서로 통합되어야 한다고 주장
- **Intelligent Tutoring Systems (ITS)**: Anderson et al. (1995) 가 AI 를 개인화된 튜터링 시스템으로 설계
- **Open Educational Resources (OER) + AI**: 오픈 자료를 AI 와 결합하여 대화형 지식 시스템으로 만드는 현대적 트렌드

### 8.2 Tiger AI 에 대한 기여

이 방법론 자체가 이 이론의 **실천 케이스**:

- repo + AGENTS.md = **실행 가능 지식 아티팩트**
- AI 공동 읽기 튜터 = 성인 전문 교육에 적용된 **적응적 ITS**
- 방법론과 대화하는 클라이언트 = 커스터마이즈된 OER

전체 논의는 [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md) 참조.

### 8.3 참고문헌

- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.
- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society*. Harvard University Press.

---

## 9. 7 이론이 어떻게 협력하는가: Tiger AI 의 통합 모델

```
┌────────────────────────────────────────────────────────────────┐
│                                                                  │
│   [Capability Maturity]  ────►  L1-L5 구조화 스코어링            │
│         │                                                        │
│         ▼                                                        │
│   [Absorptive Capacity] ────►   기업이 흡수에서 다른 이유        │
│         │                                                        │
│         ▼                                                        │
│   [Task-Technology Fit] ────►  어떤 작업이 어떤 L 에?            │
│         │                                                        │
│         ▼                                                        │
│   [Dynamic Capabilities]────►  L3-L5 는 단순 자동화가 아닌       │
│         │                       적응 능력 구축                   │
│         ▼                                                        │
│   [Sociotechnical Trust]────►  진정한 인간-AI 협업 챌린지        │
│         │                       (trust, accountability)          │
│         ▼                                                        │
│   [Real Options]        ────►  불확실성 하 L4-L5 전략 투자       │
│         │                       정당화                           │
│         ▼                                                        │
│   [AI-Native Living Book]──►   방법론 자체가 실행 가능           │
│                                                                  │
└────────────────────────────────────────────────────────────────┘

7 이론은 격리된 층이 아닌 완전한 체인:
scoring → absorption → matching → adaptation → trust → investment → execution
```

---

## 10. 학술 제출 권장사항

이 7 이론별로, 여러 논문이 파생 가능:

| 논문 제목 (제안) | 주요 이론 | 대상 저널 |
| --- | --- | --- |
| A GenAI Adoption Maturity Model: Extending BPM Maturity for the LLM Era | Capability Maturity + AI-native | MIS Quarterly / Information Systems Research |
| Absorptive Capacity in Enterprise AI Adoption: Empirical Evidence from 7 Industries | Absorptive Capacity | Strategic Management Journal |
| Task-Technology Fit Beyond Routine Work: When Should Departments Adopt L4-L5 Agents? | TTF | Information & Management |
| From Automation to Dynamic Capability: How AI Reshapes Organizational Sensing | Dynamic Capabilities | Strategic Management Journal |
| Algorithm Aversion in Workflow Automation: A Mixed-Methods Study | Sociotechnical / Trust | Organization Science |
| Valuing AI Foundation Investments as Real Options | Real Options | SMJ / California Management Review |
| AI-Native Living Books: Methodology as Executable Knowledge Artifact | AI-Native LB | Communications of the ACM |

---

## 11. 완전 참고문헌

§3-8 에서 이론별 참고문헌과 완전 참고문헌은 중국어 버전 참조.

---

라이선스 & 인용

이 문서는 Apache License 2.0; [`../NOTICE`](../NOTICE) 귀속이 보존되는 한, 사용, 수정, 상용화 가능.
