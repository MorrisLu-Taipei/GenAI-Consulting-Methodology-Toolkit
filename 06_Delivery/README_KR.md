# 06 Delivery — 납품 검수 & 안건 운영

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. 본 디렉터리의 위치

본 디렉터리는 두 가지 계층을 가지며, 합쳐서 한 가지를 해결: **컨설팅 안건을 전문적이고 스케일 가능하게 「비즈니스로 만들고」 「납품하는」 방법.**

- **납품 검수 계층**: 본 방안이 고객에게 무엇을 납품하는지, 어떻게 검수하는지, 어떤 evidence 가 완료를 증명하는지 정의.
- **안건 운영 계층**: 전체 안건 라이프사이클 (Sales → Delivery → Support), 역할 SOP, 비즈니스 문서 템플릿, 운영 체크리스트, 가격 책정 및 리스크 관리 정의.

`01`-`03` 은 「컨설턴트가 무엇을 하는가」 (방법론); `05` 는 「고객이 사고 싶게 만드는 법」 (프리세일); 본 디렉터리는 「**계약 후, 전체 안건을 비즈니스로 완주, 클린, 재현 가능하게 실행**」. 문제: **방법론만 있고 운영 프레임워크 없는 컨설팅 회사는 스코프 크리프에 짓눌리고, 핸드오버 단절, 보안 사고, 스케일 불가.**

본 디렉터리를 쓰는 사람: PM, 컨설턴트, Sales (Closer), Technical Lead, 고객 측 Owner.

## 2. 방법론 내 위치

| 축 | 매핑 |
| --- | --- |
| 3 단계 서비스 플로우 | **Deliver** + 3 단계를 「비즈니스」 운영 프레임으로 감쌈 |
| 8 단계 컨설팅 구조 | 8 단계의 **납품과 검수** 에 대응; 안건 라이프사이클은 8 단계의 「상업 외피」 |
| **3 단계 계약 모델 (컨설팅 폐쇄 루프)** | **Phase A 진단 2W → Phase B 전략 4W → Phase C 도입 24M + 분기 레이더 회고** — 안건 라이프사이클의 Delivery 단이 Phase A→B→C 폐쇄 루프 |
| L1-L5 성숙도 | 납품 패키지 검수가 L1-L5 각 레벨의 납품물 커버 |
| Engagement Lifecycle | **본 디렉터리는 안건 라이프사이클 (Sales → Delivery → Support) 본체** |

> 🔁 **안건 라이프사이클 ↔ 컨설팅 폐쇄 루프**: 본 디렉터리의 「Delivery 단」 은 **6 주 마라톤이 아니라** [`../03_Consulting_Report/README.md`](../03_Consulting_Report/README.md) §4 와 [`../00_Overview/EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) §6 가 묘사한 **폐쇄 루프**: Phase A 중간 보고서 서명 → Gate A → Phase B 완전 보고서 → Gate B → Phase C 24 개월 구현 + **분기 레이더 회고** (과학 관리의 반증 메커니즘). Support 단은 Phase C 후의 Retainer / Maintenance 에 대응.

## 3. 목표 & 효과

| 목표 | 효과 |
| --- | --- |
| 명확한 납품 패키지와 검수 기준 | 고객과 컨설턴트가 「끝났는가」 에 합의, 분쟁 없음 |
| 완전한 안건 라이프사이클 | 리드부터 종료까지 SOP, 개인 수공예 의존하지 않음 |
| 역할 SOP | 스케일 가능 (한 명이 모두 하지 않음), 핸드오버 단절 없음 |
| 비즈니스 문서 템플릿 | SOW/계약/청구서/변경 명령서 기성, 매번 재작성하지 않음 |
| 운영 체크리스트 | pre-project/security/QA/handover/offboarding 빠뜨림 없음 |
| 가격 책정 및 리스크 프레임워크 | 스코프 크리프로 마진 잠식되지 않음, 언제 「노」 할지 앎 |

**본 디렉터리 건너뛰면**: 방법론 강해도 비즈니스 안 커짐 — 스코프 크리프, 헛수고, 핸드오버 단절, 보안 사고, 키 인물 의존, 미수금.

## 4. 워크플로 & 로직

```text
안건 라이프사이클 (ENGAGEMENT_LIFECYCLE):
  Sales (Lead → Discovery → Proposal → Contract)
     → BUSINESS_DOCUMENT_TEMPLATES 사용 (제안, SOW)
     → PRICING_AND_RISK 사용 (가격 책정, 리스크 등록)
  Delivery (Kickoff → Build → Test → Security → Handover)
     → DELIVERY_CHECKLISTS 사용 (pre-project / security / QA / handover)
     → DELIVERY_PACKAGE_AND_ACCEPTANCE 사용 (패키지 검수)
     → DELIVERY_ROLE_SOPS 사용 (누가 어느 단계 책임)
  Support (Retainer → Maintenance → Offboarding)
     → DELIVERY_CHECKLISTS 사용 (offboarding)
전 과정: 7 Pillars 를 기본 원칙으로
```

| 단계 | 누가 | 언제 | 입력 | 출력 |
| --- | --- | --- | --- | --- |
| 라이프사이클 실행 | PM | 안건 전 과정 | `ENGAGEMENT_LIFECYCLE` | 각 단계 추진 |
| 비즈니스 문서 작성 | Closer / PM | Sales / 변경 시 | `BUSINESS_DOCUMENT_TEMPLATES` | 제안 / SOW / 변경 명령서 |
| 가격 책정 및 리스크 평가 | Closer / PM | Proposal / Kickoff | `PRICING_AND_RISK` | 견적 + Risk Register |
| 체크리스트 실행 | PM / Technical Lead | 각 납품 단계 | `DELIVERY_CHECKLISTS` | 각 단계 체크 통과 |
| 납품 검수 | PM + 고객 | Handover | `DELIVERY_PACKAGE_AND_ACCEPTANCE` | 고객 서명 |
| 역할 분담 | 팀 전체 | 전 과정 | `DELIVERY_ROLE_SOPS` | 명확한 책임과 핸드오버 |

> 로직: `ENGAGEMENT_LIFECYCLE` 은 본 줄기 (라이프사이클); 다른 5 개는 본 줄기 각 단계의 도구 — 문서 템플릿, 가격 리스크, 체크리스트, 역할 SOP, 납품 검수. **7 Pillars** (고객 보유, 고객 지불, 보안 최우선, 철저한 테스트, 완전한 문서화, 클린 핸드오버, 명확한 스코프) 가 전 과정 관통.

## 5. 파일 설명

### 납품 검수 계층

| 파일 | 용도 |
| --- | --- |
| `DELIVERY_PACKAGE_AND_ACCEPTANCE.md` | AI 성숙도 진단, L1-L5 강의, L4 Hermes Agent, 8 단계 컨설팅 진단 보고서의 납품 패키지 리스트와 항목별 검수 표. |

### 안건 운영 계층 (Mirza Iqbal / next8n.com 의 Workflow Automation Delivery Framework 에서 adapt, MIT, L1-L5 AI 트랜스포메이션 컨텍스트에 generalized; 인용은 `../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md` 참조)

| 파일 | 용도 |
| --- | --- |
| `ENGAGEMENT_LIFECYCLE.md` | 3 단계 라이프사이클 (Sales → Delivery → Support), 각 단계의 서브 단계와 산출, 7 Pillars, 라이프사이클 × 8 단계 크로스 레퍼런스, 프리엔게이지먼트 체크리스트. |
| `DELIVERY_ROLE_SOPS.md` | 7 개 납품 역할 SOP (Lead Gen / Sales Rep / Closer / PM / Technical Lead / Developer / Client), 각 역할: 책임, 키 납품물, 핸드오버 지점, 협업 상대, 라이프사이클 단계, 역할 × 라이프사이클 매트릭스와 핸드오버 황금 규칙 추가. |
| `BUSINESS_DOCUMENT_TEMPLATES.md` | 8 종 비즈니스 문서 템플릿: 제안, SOW, MSA 아웃라인, 변경 명령서, 청구서, 핸드오버 문서, 유지 보수 계약, 핵심 이메일. **법적 면책 첨부 — 템플릿 골격은 법률 문서 아님, 법무 검토 필요.** |
| `DELIVERY_CHECKLISTS.md` | 5 가지 운영 체크리스트: pre-project, security, QA, handover, offboarding; 방법론 Stage Gate 와의 차이 설명. |
| `PRICING_AND_RISK.md` | 가격 책정의 두 분리 원칙, 4 가지 가격 모델, 단계적 제품 라인, 안건 일반적 리스크와 완화, 언제 「노」 할지, 사고 처리 프로세스. |

### `*_EN.md`

일부 파일의 영어 sibling 버전.

## 6. 다른 디렉터리와의 대응

| 디렉터리 | 본 디렉터리와의 관계 | 데이터 플로우 |
| --- | --- | --- |
| `01_Assessment` | 진단은 라이프사이클의 Sales 단계 대응 | `01` ↔ `06` Sales |
| `02_Course_Design` | 클래스 내 산출물이 납품 패키지 검수로 | `02` 산출 → `06` 검수 |
| `03_Consulting_Report` | 컨설팅 보고서는 납품 패키지의 핵심 납품물 | `03` 보고서 → `06` 검수 |
| `05_Sales` | 덱의 견적/플랜 등급이 라이프사이클과 가격 책정 대응 | `05` 덱 ↔ `06` 가격 |
| `00_Overview` | 안건 라이프사이클은 스토리를 비즈니스로 만드는 외부 프레임 | `00` 스토리 → `06` 운영 |
| `90_References` | 안건 운영 계층의 제3자 인용 (Mirza Iqbal 프레임워크) | `90` 인용 → `06` |

## 7. 일반적 사용 시나리오

- **신규 안건 수령**: PM 이 `ENGAGEMENT_LIFECYCLE.md` 의 「시작 전 체크리스트」 로 준비 확인, `DELIVERY_ROLE_SOPS.md` 로 역할 할당.
- **계약 직전**: Closer 가 `BUSINESS_DOCUMENT_TEMPLATES.md` 의 SOW 템플릿 (스코프 내외 명기) 사용, `PRICING_AND_RISK.md` 로 가격 책정.
- **각 납품 단계**: `DELIVERY_CHECKLISTS.md` 와 대조하여 pre-project / security / QA / handover 체크리스트 실행.
- **고객에게 납품**: `DELIVERY_PACKAGE_AND_ACCEPTANCE.md` 로 항목별 검수 + `BUSINESS_DOCUMENT_TEMPLATES.md` 의 핸드오버 문서.
- **고객이 요구사항 계속 추가**: `PRICING_AND_RISK.md` 의 스코프 크리프 완화 + `BUSINESS_DOCUMENT_TEMPLATES.md` 의 변경 명령서.
- **종료**: `DELIVERY_CHECKLISTS.md` 의 offboarding 체크리스트 실행.

---

## ⭐ Cross-Topic Quick References: 5 가지 핵심 주제, 어디서 찾는가

방법론 전체에는 모든 디렉터리를 관통하는 5 가지 주동맥이 있습니다. 본 디렉터리가 각각에 어떻게 연결되는지:

| Cross-Topic | 주 위치 | 본 디렉터리가 어떻게 연결되는가 |
| --- | --- | --- |
| 🌟 **AI-Native Living Book + 3 엔진 공독** | Root [`README_KR.md`](../README_KR.md) §🌟 ｜ [`AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) ｜ [`07_AI_Contributions/`](../07_AI_Contributions/) | 안건 중에 3 엔진 분담 동원 가능: Antigravity 가 고객 회의 / Codex 가 SOW 및 보고서 초안 감사 / Claude Code 가 Phase B 시뮬레이션과 다관점 리뷰 |
| 🎓 **학술 기반 (7 대 기둥)** | [`ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md) ｜ [`FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) | 7 Pillars 의 「보안 최우선 / HITL」 은 Sociotechnical Systems & Trust (Bostrom / Dietvorst / Glikson) 에 대응; 스코프 크리프 / 레벨 점프 실패는 Real Options + Absorptive Capacity 실패 패턴 대응 |
| 📚 **L1-L5 강의 교육** | [`../02_Course_Design/`](../02_Course_Design/) ｜ [`L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md) | 납품 패키지 검수가 L1-L5 각 레벨의 검수 가능 납품물 커버; 클래스 내 산출물이 [`DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](DELIVERY_PACKAGE_AND_ACCEPTANCE.md) 에서 항목별 검수 |
| 🔁 **컨설팅 / 8 단계 + Phase A→B→C 폐쇄 루프** | [`EIGHT_STAGE_FLOW_STORY.md`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md) ｜ [`../03_Consulting_Report/`](../03_Consulting_Report/) | **본 디렉터리가 컨설팅 폐쇄 루프의 「상업 외피」** — 안건 라이프사이클 Sales→Delivery→Support 가 Phase A→B→C + 분기 레이더 회고에 대응 |
| 📖 **참고 자료 / 致敬名單** | [`../90_References/`](../90_References/) §2 致敬名單 | 안건 운영 계층이 Mirza Iqbal / next8n.com 의 Workflow Delivery Framework (MIT) 인용, 상세는 [`../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](../90_References/WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md) |
