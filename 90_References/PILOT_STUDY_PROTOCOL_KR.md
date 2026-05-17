# Pilot Study Protocol: Tiger AI 방법론에 대한 실증 검증 연구 계획

> 🌐 언어: [繁體中文](PILOT_STUDY_PROTOCOL.md) ｜ [English](PILOT_STUDY_PROTOCOL_EN.md) ｜ [Deutsch](PILOT_STUDY_PROTOCOL_DE.md) ｜ [Français](PILOT_STUDY_PROTOCOL_FR.md) ｜ [Español](PILOT_STUDY_PROTOCOL_ES.md) ｜ [日本語](PILOT_STUDY_PROTOCOL_JA.md) ｜ 한국어
>
> Apache License 2.0 · 저자: Morris Lu · Tiger AI

마지막 업데이트: 2026-05-16
버전: v1.0 Research Design Protocol (pre-registration ready)

---

> **목적**: Tiger AI 방법론을 「잘 디자인된 컨설팅 프레임워크」 에서 「연구 가능한 모델」 로 진화. 본 프로토콜은 18-24 개월, 5-10 기업의 실증 파일럿 연구를 정의, **방법론을 자가 검증만이 아닌 외부 반증에 노출**.
>
> 이는 IRB 제출 / 학술 pre-registration / 정부 연구 보조금 신청 준비 완료된 **연구 설계 문서**.

---

## 1. 배경 & 동기

### 1.1 왜 실증 연구

Tiger AI 방법론의 현재 evidence 강도:

| 요소 | Evidence Level (Tool 8.9) | 상태 |
| --- | --- | --- |
| 8 단계 흐름 설계 | L2 문서적 논증 | 완료 (Rosemann BPM + 업계 프레임워크 통합) |
| 6 construct × 0-4 스케일 | L2 전문가 컨센서스 | 완료 (**심리측정 검증 없음**) |
| 7 케이스 라이브러리 | L2 익명화 합성 | 완료 (**실제 종단 데이터 없음**) |
| Self-Qualification (Tool 2.5) | L1 self-report | 완료 (**자기 참조적, 외부 검증 안됨**) |
| Inter-rater consistency | — | **미실시** |
| 종단 KPI 의 방법론 응답 | — | **미실시** |

**결론**: 방법론은 「내부 일관성 + 논리적 폐쇄성」 에서 성숙하지만, 「외부 재현 가능성 + 예측 타당성」 에 대해 실증적으로 테스트되지 않음. 본 파일럿 연구는 둘 다 다룸.

### 1.2 연구 질문

**RQ1 — Inter-rater Reliability**: 다른 컨설턴트가 같은 방법을 사용해 같은 회사를 일관되게 스코어할 수 있는가?

- **H1**: Cohen's κ ≥ 0.60 (substantial agreement)

**RQ2 — 내부 일관성**: 6 construct 가 얼마나 내부 일관적인가?

- **H2**: Cronbach's α ≥ 0.70 construct 별

**RQ3 — Construct 타당성**: 6 construct 가 인자 분석에서 깔끔하게 출현하는가?

- **H3a**: EFA 가 5-6 인자 추출; 각 항목이 할당된 인자에 ≥ 0.5 로 로드
- **H3b**: CFA 6 인자 모델 fit: CFI ≥ 0.90, TLI ≥ 0.90, RMSEA ≤ 0.08

**RQ4 — 예측 타당성**: T0 스코어가 T+12 개월 비즈니스 KPI 향상을 예측할 수 있는가?

- **H4**: 베이스라인 KPI 와 회사 크기를 통제, Tiger AI maturity 스코어가 +12m KPI 향상을 양으로 예측 (β ≥ 0.30, p < 0.05)

**RQ5 — 종단 패턴**: Phase C 24 개월을 완료하는 기업이 「더 둥근」 레이더를 보이는가?

- **H5**: T0 vs T24 레이더 면적 (6 construct 합) 이 유의하게 증가, 각 construct 의 성장이 Tool 6.1 분해 (foundation → optimization → excellence) 를 따름

---

## 2. 연구 설계

### 2.1 설계 유형

- **혼합 방법 종단 연구**
- **Convergent parallel design**: 양적 (스케일 스코어링, KPI) + 질적 (반구조화 인터뷰, 케이스 스터디) 동시
- **Pre-registered** (공개 가설, 샘플링, 분석 계획; p-hacking 회피)

### 2.2 샘플

| 항목 | 명세 |
| --- | --- |
| **대상 샘플 N** | 5-10 기업 (파일럿 단계; 메인 스터디 N=200+ CFA 용) |
| **산업 다양성** | ≥ 3 산업 (제조, 서비스, 공공 부문 ≥ 1 씩) |
| **회사 크기** | 100-5000 직원 |
| **AI 시작점** | L0-L2 (이미 L3+ 는 제한된 개입 공간으로 제외) |
| **commitment 기간** | 18 개월 (연구 협력 협정) |
| **인센티브** | 무료 / 할인 컨설팅 + 공동 출판 기회 + 케이스 익명화 통제 |

### 2.3 모집 전략

1. n8n Taipei Ambassador 커뮤니티, NTUST Intelligent Manufacturing, QUT 동문 통해
2. 공개 권유 + Apache 2.0 오픈 repo 를 신뢰 신호로
3. 서명된 연구 협력 협정 (데이터 사용, 익명화, exit 메커니즘)

### 2.4 윤리 / IRB

- NTUST 또는 QUT IRB 승인 신청
- 정보 동의: 모든 참가자 서면으로
- 민감 데이터 처리: PII / 비즈니스 비밀 그레이딩; 더블 블라인드 데이터 격리
- 철회 권리: 어떤 기업이든 언제든 나갈 수 있음; 수집된 데이터 반환 또는 파기

---

## 3. 더블 블라인드 스코어링 설계

### 3.1 목적

Tiger AI 스코어링 모델의 **inter-rater reliability** 검증.

### 3.2 설계

```
T0 스코어링 단계 (기업별):
  ↓
  컨설턴트 A 가 독립적으로 완료:
    • 인터뷰 (Tool 1.1 40-Q 뱅크)
    • Inventory + Swimlane (Tools 1.2-1.4)
    • Reference Model Mapping (Tool 2.2)
    • 6-construct 0-4 스코어링 (Tool 2.3)
    • 주요 maturity 판단 (L1-L5)
  ↓
  컨설턴트 B 가 독립적으로 완료 (같은 기업, A 에 대해 블라인드):
    • 위 모든 액션 반복
  ↓
  연구 분석가 (중립) 가 A vs B 비교:
    • 6-construct 스코어 격차 (weighted kappa)
    • 주요 maturity 판단 일치 (unweighted kappa)
    • 갭 식별 오버랩 (M/B/R 테이블 오버랩)
```

### 3.3 일관성 통계

| 메트릭 | 도구 | 해석 |
| --- | --- | --- |
| **Cohen's κ (unweighted)** | κ = (Po - Pe) / (1 - Pe) | < 0.20 slight; 0.21-0.40 fair; 0.41-0.60 moderate; 0.61-0.80 substantial; > 0.80 almost perfect |
| **Weighted κ (linear / quadratic)** | 순서 스케일 (0-4) 용 | 위와 같지만, 「1 포인트 off」 vs 「4 포인트 off」 에 더 엄격 |
| **ICC (Intraclass Correlation)** | Two-way mixed model | < 0.5 poor; 0.5-0.75 moderate; 0.75-0.9 good; > 0.9 excellent |
| **Bland-Altman 플롯** | 스코어 격차 시각화 | 시스템적 바이어스 감지 |

---

## 4. 종단 KPI 추적

### 4.1 KPI 측정 시점

| 시점 | 이름 | 측정 |
| --- | --- | --- |
| **T0** | Baseline | Phase A 후, Phase B 전 |
| **T+6m** | Phase 1 종료 | L1 Gate Acceptance |
| **T+12m** | Mid Phase 2 | L2/L3 Gate |
| **T+18m** | Phase 2 종료 | L3 완료 |
| **T+24m** | Phase 3 종료 | L4/L5 Gate |

### 4.2 5 KPI 차원 (Tool 8.5 Value Tracking 별)

| 차원 | 예시 KPI |
| --- | --- |
| **Time** | Complaint response, proposal turnaround, month-end close, decision cycle |
| **Quality** | 결함률, 오류율, complaint count, rework rate |
| **Scale** | Throughput, beneficiaries, automated task count |
| **Risk** | Missed case rate, compliance violations, sensitive-data leakage |
| **Assets** | Skill count, Wiki entries, Agent task count, training completion |

### 4.3 KPI 데이터 품질 (Tool 8.9 Evidence Hierarchy 별)

- **L3 의무**: 모든 Time / Scale KPI 를 system logs (n8n / Audit Log / ERP) 에서
- **L4 권장**: Internal audit / external accountants 에 의한 샘플 검증
- **L1-L2 보충**: Employee NPS / 인터뷰 요약

---

## 5. 질적: 반구조화 인터뷰

### 5.1 인터뷰 시점

기업별: T0, T+6m, T+12m, T+18m, T+24m — 각 1 라운드 (인터뷰 대상자별).

### 5.2 인터뷰 대상자

- CEO / Sponsor
- AI Champion
- IT Lead
- ≥ 2 Department Heads
- ≥ 3 Front-line Users

### 5.3 인터뷰 질문 (발췌)

1. 지난 6 개월에서 가장 영향력 있는 AI 변화는?
2. 기대된 AI 변화 중 일어나지 않은 것은? 왜?
3. 직원 / 부서의 AI 에 대한 태도가 변했는가?
4. 동료에게 이 방법론을 추천 / 비추천하겠는가?
5. 가장 유용한 Stage / Tool 은? 가장 덜 유용한 것은?
6. Cross-time: 12 개월 전 서명한 Ideal Practice 를 돌아보면, 후회가 있는가?

### 5.4 질적 분석

- 그대로 전사 + 코딩 (NVivo / Atlas.ti)
- Dual-coder reliability ≥ 80%
- 패턴 / counter-examples 추출하기 위한 주제 분석

---

## 6. 통계 분석 계획

### 6.1 기술 통계

- Construct 별 스코어 분포 (mean, SD, median, IQR)
- 레이더 차트 T0 vs T24 시각화
- 6-construct 상관 매트릭스 (다중공선성 체크)

### 6.2 Reliability & Validity

| 분석 | 도구 | 가설에 매핑 |
| --- | --- | --- |
| Cronbach's α | SPSS / R `psych::alpha()` | H2 |
| EFA + Bartlett's + KMO | SPSS / R `psych::fa()` | H3a |
| CFA + fit indices | Mplus / R `lavaan::cfa()` | H3b (**N ≥ 200 필요**) |
| Cohen's κ | R `irr::kappa2()` | H1 |
| ICC | R `irr::icc()` | H1 |

### 6.3 추론 통계

| 분석 | 가설 | 도구 |
| --- | --- | --- |
| Paired t-test (T0 vs T24) | H5 레이더 면적 증가 | R `t.test(paired=TRUE)` |
| Mixed-effects model | H4 예측 타당성 | R `lme4::lmer()` |
| ANCOVA | 베이스라인 KPI + 크기 통제 | R `aov()` |
| 민감도 분석 | 결측 데이터 + 드롭아웃 대비 | R `mice` multiple imputation |

### 6.4 유의성 & 조정

- α = 0.05 주 테스트
- Bonferroni correction 을 multiple comparisons 용으로
- Effect size 보고: Cohen's d, η², partial η²

---

## 7. 타임라인 & 마일스톤

```
월 0:     설계 완성 + IRB 제출
월 1-3:   5-10 기업 모집 + 연구 협정 서명
월 4:     컨설턴트 A/B 훈련 (더블 블라인드 SOP)
월 5-6:   T0 더블 블라인드 스코어링 + Baseline KPI 측정
월 6-12:  Phase 1 개입 + T+6m 스코어링 + 인터뷰
월 12-18: Phase 2 개입 + T+12m + T+18m
월 18-24: Phase 3 개입 + T+24m 최종 스코어링 + 인터뷰
월 24-27: 분석 + 연구 보고서 + 저널 제출
월 27-30: 개정 + 제출
```

---

## 8. 예산 추정

| 항목 | 추정 (NT$) |
| --- | --- |
| 컨설턴트 시간 (A + B 80-120 시간씩 기업별) | 6-9M |
| 연구 직원 (중립 스코어링 비교 + 질적 분석) | 1.5-2.5M |
| KPI system-log 도구 + 인터뷰 전사 | 0.5-1M |
| IRB / 법무 / 통계 컨설턴트 | 0.5-1M |
| 오픈소스 도구 + 클라우드 데이터 스토어 | 0.3-0.5M |
| 비상 (15%) | 1.3-2M |
| **합계** | **NT$ 10.1-16M** |

⚠️ 무료 컨설팅 대가로, 5-10 기업이 18 개월 데이터 수집에 commitment → 컨설턴트 노동력은 「equivalent consulting service」 로 offset 가능, **실제 현금 지출은 NT$ 4-7M 로 축소 가능**.

---

## 9. 출판 전략

### 9.1 예상 출력

| 출력 | 저널 / 플랫폼 | 예상 시점 |
| --- | --- | --- |
| **Pre-registration** | OSF | 월 0 |
| **Protocol paper** | BMJ Open / Pilot and Feasibility Studies | 월 3 |
| **Methodology paper** | MIS Quarterly / Information Systems Research / Journal of Business Research | 월 27 |
| **Industry white paper** | 이중언어, 공개 Apache 2.0 | 월 27 |
| **Case studies (익명화)** | HBR-style 케이스 | 월 30 |
| **Practitioner guide** | 툴킷 업데이트 + 실증 evidence 추가 | 월 30 |

### 9.2 Open Science Commitment

- 모든 연구 데이터 (de-identified) 가 OSF 에 공개
- 통계 R / Python 스크립트가 GitHub 에
- 인터뷰 대상자 정체성 비공개; 집계 결과 완전 투명

---

## 10. 위험 & 완화

| 위험 | 확률 | 영향 | 완화 |
| --- | --- | --- | --- |
| 기업 중도 철회 (드롭아웃) | Med | High | 12 까지 과도 모집; intention-to-treat 분석 |
| 컨설턴트 A/B 바이어스 / 누출 | Low | High | SOP 훈련 + 감사 + 엄격 더블 블라인드 + 다른 사무실 |
| KPI system log 접근 불가 | Med | Med | T0 IT 가 로그 가용성 확인; 그렇지 않으면 대체 지표 |
| IRB 검토 지연 | Med | Med | 월 0 IRB 제출을 모집과 병행 |
| CFA 에 N 불충분 | High | Med | 파일럿에서 EFA; CFA 는 메인 스터디 N=200+ 기다림 |
| 예산 부족 | Med | High | NSTC / MOE / QUT 보조금 신청; 다중 기업 비용 분담 |

---

## 11. Stopping Rules

전체 공개와 함께 조기 종료:

- ≥ 50% 기업 철회
- Inter-rater κ < 0.40 (방법론 불일치 → 스케일 재설계 필요)
- IRB 철회
- 심각한 윤리 문제 (데이터 누출, 참가자 손해)

**조기 종료된 연구도 수집된 모든 데이터를 출판해야 함** (출판 바이어스 회피).

---

## 12. 예상 기여

| 기여 | 청중 | 형식 |
| --- | --- | --- |
| **이론**: 첫 실증 검증된 GenAI 채택 maturity 모델 | 학계 (IS / BPM / Strategy) | 동료 검토 논문 |
| **방법**: Cases-as-Benchmarks + Client Ideal Practice 워크숍 프로토콜 | 컨설팅 업계 | 오픈소스 툴킷 (Apache 2.0) |
| **정책**: AI Governance Alignment 를 위한 실증 evidence | 규제 기관 (Taiwan AI Basic Act / NIST / EU) | 백서 + 입법 청문회 |
| **업계**: 5-10 기업 실제 종단 케이스 | 동료 고객 | 실제 케이스 (합성 대체) |
| **교육**: NTUST / QUT 커리큘럼에 통합 | 학생 | 코스 자료 |

---

## 13. 관련 문서

| 문서 | 관계 |
| --- | --- |
| [`../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md) §3.1-3.3 | 스케일 construct 정의; 본 연구가 검증 |
| [`../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | 왜 방법론이 실증 검증을 필요로 하는지 |
| [`FAILURE_PATTERNS_EN.md`](FAILURE_PATTERNS_EN.md) | 알려진 failure modes → 완화가 본 연구에 구축됨 |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9 | KPI evidence grading 을 위한 Evidence Hierarchy 기반 |

---

## 14. 참고문헌

- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46.
- Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16(3), 297-334.
- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT.
- Streiner, D. L., Norman, G. R., & Cairney, J. (2015). *Health measurement scales: A practical guide to their development and use* (5th ed.). Oxford University Press.
- Hair, J. F., et al. (2019). *Multivariate Data Analysis* (8th ed.). Cengage.
- Creswell, J. W. (2018). *Research design: Qualitative, quantitative, and mixed methods approaches* (5th ed.). SAGE.
- Open Science Framework: <https://osf.io/>

---

라이선스 & 인용

이 문서는 Apache License 2.0; [`../NOTICE`](../NOTICE) 귀속이 보존되는 한, 사용, 수정, 상용화 가능. 다른 연구 팀은 동일한 pre-registration 과 open-science commitment 를 따르는 한, 본 설계를 **자유롭게 채택, 수정, 복제** 가능.
