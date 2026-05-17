# 방법론의 과학적 논리: 왜 이 리포트가 토론에 견디는가

> 🌐 언어: [繁體中文](METHODOLOGY_SCIENTIFIC_LOGIC.md) ｜ [English](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) ｜ [Deutsch](METHODOLOGY_SCIENTIFIC_LOGIC_DE.md) ｜ [Français](METHODOLOGY_SCIENTIFIC_LOGIC_FR.md) ｜ [Español](METHODOLOGY_SCIENTIFIC_LOGIC_ES.md) ｜ [日本語](METHODOLOGY_SCIENTIFIC_LOGIC_JA.md) ｜ 한국어
>
> Apache License 2.0 · 저자: Morris Lu · Tiger AI

최종 업데이트: 2026-05-15

---

> **이 문서가 답하는 것**: 왜 이 방법론은 이렇게 설계되었는가? 왜 8 단계, 5 도 12 도 아닌? 왜 데이터가 이렇게 흐르는가? 왜 케이스는 Benchmark-grade 여야 하는가? **궁극적으로**: 클라이언트 / 이사회 / 규제기관이 도전할 때, 이 컨설팅 리포트는 무엇에 기반하여 서는가?
>
> **핵심 주장**: 이 방법론은 컨설팅 경험의 모음이 아니라 **클로즈드 루프 과학적 관리 논리** — 모든 단계가 과학적 방법의 5 조건을 만족: 관찰 가능, 정량화 가능, 재현 가능, 반증 가능, 감사 가능.

---

## 1. 왜 컨설팅 리포트는 「과학적 논증력」이 필요한가

일반적 실패 시나리오:

| 시나리오 | 클라이언트 도전 | 전형적 컨설턴트 응답 | 왜 실패하는가 |
| --- | --- | --- | --- |
| 이사회 질문 | 「우리가 L2 라는 걸 어떻게 압니까?」 | 「인터뷰에 기반하여...」 | 주관적; 검증 불가능 |
| 내부 감사 | 「왜 고객 서비스가 영업보다 먼저?」 | 「우리 경험으로는...」 | 경험은 감사 불가능 |
| 규제 체크 | 「AI 가 실패하면 누가 책임?」 | 「정책이 있습니다...」 | 감사 체인 없는 정책은 안 침 |
| 컨설턴트 교체 | 「이전 펌은 L3 라고 했고; 당신은 L2 — 누가 옳은가?」 | 「다른 방법」 | 비재현 = 비과학적 |

**Tiger AI 의 설계 목표**: 각 이러한 질문에 **검증 가능한 숫자 + 감사 가능한 에비던스 + 재현 가능한 절차** 가 응답으로 존재.

---

## 2. 과학적 방법의 5 조건 vs. 본 방법론

| 과학적 조건 | 정의 | 방법론이 어떻게 만족하는가 |
| --- | --- | --- |
| **1. 관찰 가능** | 결론은 타인이 볼 수 있는 에비던스에 의거 | Stage 1 녹음 + 시스템 인벤토리 + As-Is Swimlanes; 각 항목에 타임스탬프와 소스 |
| **2. 정량화 가능** | 결론은 형용사가 아닌 숫자로 환원 가능 | Stage 2 레이더 0-4 스코어링; Stage 4 Impact×Effort 스코어링; Stage 5 80/20 impact-surface 숫자; Stage 8 value tracking 5 차원 |
| **3. 재현 가능** | 다른 컨설턴트가 같은 방법을 사용하여 유사한 결론에 도달 | 3 개 Reference Model (APQC / SCOR / Tiger AI L1-L5) 은 공식 표준; 40 문항 인터뷰 뱅크; MECE 규율 |
| **4. 반증 가능** | 결론에 명시적 반박 조건 | Stage 6 Stage Gate Criteria 가 명시적으로 pass/fail 나열; 체크리스트에 관찰 가능 조건; 타겟 미달 = 가설 반증 |
| **5. 감사 가능** | 프로세스가 제 3 자에 의해 독립적으로 검증 가능 | Stage 8 Audit Log (LLM 콜, 권한 변경, Skill 배포, Reviewer 사인오프 완전 체인), 보유 정의 |

> **이 다섯 조건은 장식이 아님**. 이 다섯에 응답할 수 없는 컨설턴트 결론은 과학적 관리가 아님 — 단지 경험 공유.

---

## 3. 왜 정확히 8 단계 (5 도 12 도 아닌)

과학적 방법에서 역추론: 방어 가능한 AI 트랜스포메이션 리포트는 **5 개 추론 액션을 거쳐야 함**, 그것들 사이에 엄격한 데이터 의존성:

| 추론 액션 | Stage 에 매핑 | 건너뛰기가 야기하는 것 |
| --- | --- | --- |
| **A. 현재 상태 관찰** | Stage 1 As-Is | 객관적 베이스라인 없음 → 그 후 모든 것이 추측 |
| **B. 국제 좌표 적용** | Stage 2 Reference Model | 외부 좌표 없음 → 「우리는 충분히 좋지 않음」은 컨설턴트 의견 |
| **C. 클라이언트가 자기 Ideal Practice 확장** | Stage 3 Best Practice | 클라이언트 서명 타겟 없음 → 클라이언트가 갭을 부정 가능 |
| **D. 갭 정량화** | Stage 4 Gap Analysis | 구조화된 갭 없음 → 우선순위 불가 |
| **E. 핵심 문제 수렴** | Stage 5 Problem Definition | 80/20 없음 → 「모든 것이 중요」 = 아무것도 하지 못함 |
| **F. 흡수 가능 타겟 설정** | Stage 6 Phased Goals | 단계 분해 없음 → 원샷 완벽주의 시도 = 실패 |
| **G. 청사진 설계** | Stage 7 To-Be Design | To-Be 다이어그램 없음 → Roadmap 이 조직과 시스템에 착륙 안 함 |
| **H. 실행 & 거버넌스** | Stage 8 Implementation | Change Mgmt + Value Tracking + Audit 없음 → 청사진은 벽지 |

**왜 정확히 8**: 각 추론 액션은 분리 불가; **어느 하나라도 건너뛰면 도전이 무응답으로 남음**.

- Stage 2 건너뛰기 → 「당신의 표준은?」 무응답
- Stage 4 건너뛰기 → 「왜 이것이 먼저, 저것이 나중?」 무응답
- Stage 6 건너뛰기 → 「왜 9 개월, 3 개월이 아닌?」 무응답
- Stage 8 건너뛰기 → 「개선됐다고 어떻게 증명?」 무응답

> 5 단계는 너무 거침 (Reference Model, Phased Goals, Change Mgmt 생략); 12 단계는 너무 미세 (중복 서브 스텝). **8 은 「최소 완전 토론 가능 추론 체인」**.

---

## 4. 왜 데이터가 이렇게 흐르는가 (각 화살표의 과학적 이유)

```
Stage 1 ──────────► Stage 2 ──────────► Stage 3 ──────────► Stage 4
As-Is              Reference Model     Best Practice         Gap
관찰된 현실         국제 좌표           클라이언트 Ideal       객관적 갭
                                        Practice (서명)
                                                              │
                                                              ▼
Stage 8 ◄────────── Stage 7 ◄────────── Stage 6 ◄────────── Stage 5
Implementation      To-Be Design       Phased Goals          Problem
착륙 + change       미래 청사진          흡수 가능 단계         핵심 수렴
                                                              
        ↑                                                     ↓
        └─── 분기별: Stage 2 레이더 재방문 (클로즈드 루프 검증) ───┘
```

#### 각 화살표가 왜 인과적으로 필요한가

| 화살표 | 왜 이 방향 | 역전이 야기하는 것 |
| --- | --- | --- |
| **Stage 1 → 2** | 「표준」과 비교하기 전에 「현실」을 가져야 함 | 역전: 표준에 맞추기 위해 에비던스 체리픽 |
| **Stage 2 → 3** | 「클라이언트 Ideal」을 논의하기 전에 「구조 완전」을 확인해야 함 | 역전: Ideal 이 구조적 갭을 건너뜀 |
| **Stage 3 → 4** | 「Gap = (클라이언트 Ideal − 클라이언트 As-Is)」를 계산하기 전에 **클라이언트 서명 Ideal Practice** 를 가져야 함 | 클라이언트 서명 없음, 갭 = 컨설턴트 의견, 반박 가능 |
| **Stage 4 → 5** | 「핵심 문제」로 80/20 수렴하기 전에 「모든 갭」을 가져야 함 | 4 없이, 문제 정의 = 추측 |
| **Stage 5 → 6** | 「타겟」을 설정하기 전에 「핵심 문제」를 잠가야 함 | 5 없이, 타겟 분산 |
| **Stage 6 → 7** | 「청사진」을 설계하기 전에 「단계화된 타겟」을 가져야 함 | 6 없이, 청사진은 원샷 시도 |
| **Stage 7 → 8** | 「실행」 전에 「청사진」을 가져야 함 | 7 없이, 실행은 맹목 |
| **Stage 8 ↑ Stage 2 (분기별)** | 실행 후, 「표준 레이더 더 둥근가?」 재방문 | 루프백 없이, PoC 완료했지만 구조 미검증 |

> **이것이 「클로즈드 루프」의 과학적 의미**: 「완료 = 좋음」이 아니라 「결과가 소급적으로 검증 / 반증 가능」.

---

## 5. 왜 Reference Model 은 4 층 (3 도 5 도 아닌)

성숙도의 「**추상 × 휘발성**」 축에서 유도 ([`CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 2.7 참조):

| 추상 | 휘발성 | 층 | 왜 병합 또는 생략 불가능 |
| --- | --- | --- | --- |
| 가장 추상 | 년 단위 | **L1 Governance** | 전략과 정책은 프로세스와 혼합할 수 없음 (휘발성 10× 차이) |
| 추상 | 분기-년 | **L2 Business** | 비즈니스 기능은 데이터 서비스와 혼합할 수 없음 |
| 중간 | 월-분기 | **L3 Information** | 데이터 서비스는 하드웨어/네트워크와 혼합할 수 없음 |
| 가장 구체 | 주-월 | **L4 Technical** | 하드웨어가 Business 층에 혼입되면 테크 선택이 잠김 |

**3 층 불충분**: 보통 L3 Information 을 떨어뜨림 → 데이터 서비스가 L2 또는 L4 에 압착 → 포커스 상실.
**5 층 과도**: 추가 층은 보통 L2 또는 L3 의 서브 층 → MECE 위반.

> **Dragon1 학파가 4 층을 고수하는 것은 이 과학적 이유 때문**. Tiger AI Enterprise AI Reference Model 은 엄격히 따름.

---

## 6. 왜 케이스는 Benchmark-grade 여야 하는가 (서술이 아닌)

과학은 「**재현 가능성**」을 요구 — 다른 컨설턴트 / 클라이언트가 읽는 같은 케이스는 유사한 「갭 추정」을 산출해야 함.

- **서술 케이스**: 「X 회사가 AI 품질 검사를 했고 성공했다」 → 재현 불가능 (각 독자가 다르게 해석)
- **Benchmark-grade 케이스**: 9 필수 필드 (업계 + 규모 + 시작 L + 종료 L + 기간 + 투자 + Wins + Failures + 적용성) → **재현 가능** (어떤 독자의 갭/시간/예산 추정도 유사 범위에 들어감)

Tool 3.5 Cases-as-Benchmarks 참조.

> **그래서 모든 7 Tiger AI 케이스가 같은 9 필드 템플릿에 따름** — 시각적 일관성을 위해서가 아니라 **재현 가능성**의 과학적 조건을 위해.

---

## 7. 리포트의 「과학적 논증력」 체크리스트

클라이언트 / 이사회 / 규제기관이 다음 질문을 할 때, 본 방법론은 특정 응답 위치를 가짐:

| 도전 | 응답 위치 | 에비던스 |
| --- | --- | --- |
| 「우리가 L2 라는 걸 어떻게 압니까?」 | §3 As-Is + §4 RM Mapping | 인터뷰 녹음, 시스템 인벤토리, RM 레이더 0-4 |
| 「왜 APQC / Tiger AI L1-L5?」 | §4.1 + Tool 2.5 | 10 조건 자격 스코어카드 |
| 「우리는 이상에서 얼마나 멀리 있는가?」 | §5 + §6.1 | **클라이언트 서명 Ideal Practice 정의 테이블** + 케이스 Benchmark; Gap = (당신의 서명 Ideal − 당신의 As-Is), 양 끝 모두 당신의 진술 |
| 「왜 고객 서비스가 영업보다 먼저?」 | §6.2 + §6.3 | Impact × Effort 매트릭스 + Prioritization Score |
| 「왜 핵심 문제가 ‹지식 자산화›?」 | §7 | 80/20 impact-surface 숫자 + 5 Whys 체인 |
| 「왜 9 개월, 3 개월이 아닌?」 | §8 + Tool 6.3 | 단계 분해 + Organizational Absorption (6 차원) + 벤치마크 케이스 기간 |
| 「PoC 가 실패하면?」 | §13.2 | Risk Register + Triggers + Mitigation Owners |
| 「개선됐다고 어떻게 증명?」 | §13.1 + 분기 레이더 리뷰 | Value Tracking 5 차원 + Stage 2 레이더 before/after |
| 「AI 가 실패하면 누가 책임?」 | §12.1 + Tool 8.8 | RACI + AI Ethics Checklist + Audit Log 완전 체인 |
| 「당신의 방법론은 재현 가능한가?」 | 방법론 전체 | Apache 2.0 + GitHub + Tool 2.5 자기 자격 9/10 |
| 「이전 컨설턴트는 L3 라 했고, 당신은 L2 — 누가 맞나?」 | §3 스코어링 에비던스 | 공식 0-4 스케일 + 각 스코어에 관찰 가능 에비던스 → **제 3 자 검증 가능** |
| 「왜 정확히 8 단계?」 | 본 문서 §3 | 「최소 완전 토론 가능 추론 체인」 논증 |

> **리포트가 토론 가능 문서가 됨**: 클라이언트는 「컨설턴트 권위를 신뢰」하는 것이 아니라 「에비던스 체인을 따라 같은 결론에 스스로 도달」. 그것이 과학적 관리.

---

## 8. 메인스트림 컨설팅 방법론과의 비교

| 방법론 | 강점 | 부족 (과학적 완전성 렌즈에서) |
| --- | --- | --- |
| **McKinsey Issue Tree + Pyramid** | 엄밀한 논리 추론, 강한 내러티브 | Reference Model 없음 (좌표 없음); Phased Goals 없음 (단계 분해 없음) |
| **BCG Digital Maturity** | 명확한 5 단계 성숙도 | 정량화된 Best Practice 없음 (우수성을 컨설턴트가 기술); 조직 흡수 평가 없음 |
| **Gartner AI Maturity** | 업계 인정 | As-Is 인터뷰 규율 없음; 재현 가능 케이스 Benchmark 없음 |
| **MIT AI Capability** | 학술적으로 엄밀 | Implementation & Change 착륙 도구 부족 |
| **Tiger AI (본 방법론)** | **8 단계 완전 추론 체인 + 4 층 Reference Model + Cases-as-Benchmarks 클로즈드 루프** | 신규 (2025 출시, 케이스 축적 중) |

> **다른 방법론이 나쁘다고 말하는 것이 아님** — 각자 강점이 있지만 **클로즈드 루프가 불완전** 하다는 것. Tiger AI 의 설계 목표는 그 루프를 완성하여 리포트가 **표지에서 마지막 페이지까지 각 문장에 에비던스** 를 갖게 하는 것.

---

## 9. 학술 및 규제 인용 가치

왜 본 방법론이 학술 커뮤니티에 의해 검증, 인용, 개선 가능한가:

1. **공식**: Apache 2.0, GitHub repo, zh/en 이중 언어
2. **자체 자격 가능**: Tool 2.5 자체 평가, 10 조건 중 9 충족
3. **이론적 뿌리 투명**: Rosemann BPM Maturity 학파 (QUT) + CMMI + APQC + Dragon1 EA 각각 인용
4. **업계 횡단 검증**: 제조 / 병원 / 마케팅 / B2B / Financial / Government / Education — 7 업계 케이스 (이식성 검증)
5. **반증 가능**: 각 Stage Gate Criteria 에 반박 조건
6. **비판 가능**: 본 문서와 Tool 2.5 모두 명시적으로 「신규, 인정 축적 중」 명시

> **학술 인용의 골드 스탠다드는 「다른 사람이 이 방법을 다른 문제에 적용하여 유사한 결론을 얻을 수 있는가?」** — Tiger AI 방법론은 Yes 라고 응답, 모든 단계, 도구, 스코어링 기준이 공식이므로.

---

## 10. 컨설턴트를 위한 운영 규율

이 리포트를 쓸 때, 각 단락은 응답해야 함:

```
이 진술의 에비던스는 무엇인가?                       ← 관찰 가능
이 숫자는 어떻게 계산됐는가?                          ← 정량화 가능
다른 컨설턴트가 같은 결과를 얻을 것인가?              ← 재현 가능
이것이 틀렸다면 무엇이 보일 것인가?                   ← 반증 가능
이 프로세스에 누가 서명했는가?                        ← 감사 가능
```

**5 가지 모두 응답 → 그 단락은 과학적 관리**.
**어느 것도 응답 불가 → 그 단락은 개인적 의견; 에비던스를 보충하거나 삭제**.

---

## 11. 클라이언트에 대한 약속

본 방법론은 약속함:

1. **모든 결론에 번호 매겨진 에비던스** — Appendices A-G 완전 추적 가능
2. **모든 숫자에 계산 공식** — 「컨설턴트 판단에 기반하여」 없음
3. **모든 권장 사항에 Stage Gate Criteria** — 당신이 검증 가능
4. **모든 리스크에 Trigger + Owner + Mitigation** — 당신이 관리 가능
5. **모든 케이스가 Benchmark-grade** — 당신이 갭을 자체 계산 가능
6. **각 단계 종료에서 Reference Model 레이더 재방문** — 당신이 구조가 실제로 더 둥글어지는 것을 봄

**어떤 단락이 「컨설턴트 권위가 결정」 으로 느껴지면 지적하세요. 우리는 에비던스를 추가, 공식을 수정, 또는 삭제할 것입니다**.

---

## 12. 클로징: 본 방법론 자체가 Reference Model

최종 자체 참조적 관찰:

- 본 방법론은 Tool 2.5 의 10 조건을 적용하여 **자체 평가**: 10 중 9 충족 (조건 6 「광범위한 업계 인정」 여전히 축적 중)
- 본 방법론은 Tool 2.6 의 5 가지 유도 질문을 적용하여 **컴포넌트를 자체 인벤토리**: 8 단계 + 4 층 + 5 트래킹 차원 모두 존재
- 본 방법론은 Tool 2.7 의 4 층 아키텍처를 적용하여 **자체 조직**: Governance (본 문서) + Business (Stages 1-8) + Information (toolkit + cases) + Technical (GitHub repo + AGENTS.md + CLAUDE.md)
- 본 방법론은 Tool 3.5 의 Cases-as-Benchmarks 를 적용하여 **재현 가능성을 자체 증명**: 7 업계 케이스 모두 9 필드 템플릿을 따름

> **이것이 과학적 관리의 클로즈드 루프**: 방법론은 다른 사람들을 분석할 뿐만 아니라 **자신의 도구로 자기 자신을 분석 가능** — 학계에서 「자기 참조적 일관성」이라 불리며, 엄밀한 이론의 특징.

---

## References

- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT.
- APQC (2024). *Process Classification Framework Version 7.3*.
- CMMI Institute (2018). *CMMI for Development V2.0*.
- Dragon1 (n.d.). *Enterprise Architecture Reference Model*. <https://www.dragon1.com/reference-models/enterprise-architecture-reference-model>
- Pyramid Principle: Minto, B. (2009). *The Pyramid Principle*.
- 80/20: Koch, R. (1997). *The 80/20 Principle*.
- 5 Whys: Ohno, T. (1988). *Toyota Production System*.
- Change Management: Kotter, J. (1996). *Leading Change*. Prosci ADKAR.

---

라이선스 & 인용

본 문서는 Apache License 2.0; [`../NOTICE`](../NOTICE) 귀속이 보존되는 조건으로 사용, 수정, 상업화 가능.
