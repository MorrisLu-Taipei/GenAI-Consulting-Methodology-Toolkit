# 경영 요약: 방법론 전체를 5 분에 (전체 그림은 10 분)

> 🌐 中文 / Chinese: [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) ｜ English: [EXECUTIVE_SUMMARY_EN.md](EXECUTIVE_SUMMARY_EN.md)
>
> **5 분 버전**: §1 "한 페이지로" + §2 "코어 모델" 만 읽으면 충분.
> **10 분 버전**: §3-§7 (살아있는 책, 이론, 강의, 컨설팅, 납품, 공독, 다음 단계) 추가.
> 링크된 파일은 더 깊이 알고 싶을 때만 클릭.

---

## 1. 한 페이지로: 무엇을 해결하는가

많은 기업이 AI 도입 시 "**도구로 바로 뛰어듭니다**" — ChatGPT 사고, n8n 시도하고, Agent 만들고 싶어함. 결과: 직원이 사용 못함, 프로세스 연결 안 됨, 데이터 거버넌스 안 됨, PoC 검수 불가, 결국 경영진도 회사 AI 가 실제 어떤 성숙도에 있는지 모름.

본 방법론은 "**산재된 AI 사용**"을 "**재현 가능, 거버넌스 가능, 측정 가능, 확장 가능한 조직 역량**"으로 변환 — **설문 + 강의 + 컨설팅**의 폐쇄 루프로 기업을 **AI 를 사용하는 개인**에서 **AI 팀을 보유한 기업**으로 인도합니다.

| 요소 | 한 문장으로 |
|---|---|
| **진단 도구** | 10 / 25 / 50 문항 설문 → 객관적인 L1-L5 위치 + 6 차원 갭 |
| **교육 경로** | 5 단계 강의 (OpenWebUI / Antigravity / n8n / Hermes / ClawTeam) + BARS 채점 보정 |
| **컨설팅 구조** | 8 단계 (Awareness → Acceptance Test) + 3 단계 계약 (A 진단 / B 전략 / C 도입) |
| **학술 기반** | 7 대 이론 기둥 (Rosemann / Cohen & Levinthal / Teece / Real Options / 등) |
| **운반 매체** | **AI-Native Living Book** — 진정으로 *살아있는* 방법론, AI IDE 로 직접 공독 가능 |

---

## 2. 코어 모델: L1-L5 의 두 축

L1-L5 는 "다섯 개의 도구"가 아니라 **두 축**으로 연결된 성숙도 경로:

| 축 | 범위 | 드라이버 | 계층 | 도구 |
|---|---|---|---|---|
| **규모 축** | L1 → L2 → L3 | **인간**이 AI 사용, **인간**이 AI 감독 | 개인 → 부서 → 부서 간 / 전사 | OpenWebUI / Antigravity / n8n |
| **AI 자율 축** | L4 → L5 | **AI** 가 자율 운영; 인간은 **거버너**로 후퇴 | AI 엔티티 → AI 팀 | Hermes Agent / ClawTeam |

**중요 분기점 = L3 → L4**: "인간이 일 운전"에서 "AI 가 일 운전"으로 건너감. L4-L5 에서도 **거버넌스 프레임은 여전히 인간이 구축하고, 인간이 감독 보유** — AI 가 자율하는 것은 "운영 실행"이지 "거버넌스 결정"이 아님.

➜ 전체 스토리: [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) §3.0

---

## 3. AI-Native Living Book — 왜 이 책이 *살아있는*가

본 방법론은 PDF / PPT / SOP 가 아닙니다 — **진정으로 *살아있는* 책**:

| 세대 | 형태 | 한계 |
|---|---|---|
| 1 세대 — 인쇄 책 | 종이 | **정적** — 읽기만 가능, 응답하지 않음 |
| 2 세대 — 인터랙티브 북 | 웹 / 위키 | **인터페이스는 살아도 콘텐츠는 살지 못함** — 여전히 선제적 제안 없음 |
| **3 세대 — AI-Native Book** (본 레포) | Markdown + AI IDE | **진정으로 살아있음** — 묻게 하고, 답하고, 함께 생각하고, 회사 상황에 맞춰 진단 / 보고서 초안 / 시뮬레이션 실행 |

**운영 모델**: `git clone` → AI IDE (Antigravity / Claude Code / Codex) 로 열기 → AI 가 전체 책 자동 독해 → 본 방법론의 **공독 튜터**로 자기 위치 → 직접 대화, 질문, 적용.

➜ 전체 논의: [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md)

### 서로 다른 전문성을 가진 3 개의 AI 엔진

| 엔진 | 역할 | 가장 잘하는 것 | 워크플로 |
|---|---|---|---|
| 🟦 **Antigravity** | 최전선 컨설턴트 | 고객과 대화, 설문 실행, 보고서 초안 | `/diagnose`, `/generate-report` |
| 🟪 **Codex CLI** | 방법론 감사관 | 파일 간 테스트, 레드팀 검토, 버전 관리, 수리 | `/evidence-audit`, `/red-team-review`, `/bump-version` 외 7 개 |
| 🟨 **Claude Code** | 파일 간 사고 파트너 | 심층 종합, 다관점 토론, 시뮬레이션, 고객 Fork | `/simulate-engagement`, `/devil-pair-debate`, `/methodology-fork` 외 7 개 |

➜ 3 엔진 자기 기술: [`../07_AI_Contributions/`](../07_AI_Contributions/) ｜ 설치 가이드: root [`../README_KR.md`](../README_KR.md) §🚀

---

## 4. 학술 기반: 7 대 이론 기둥

본 방법론은 임시방편이 아닙니다. 모든 핵심 설계는 **고전 이론에 매핑** — 학자, 규제, 이사회가 "이론적 근거는?"이라고 물을 때의 표준 답변:

| # | 이론 | 창시자 | 본 방법론에서의 역할 |
|---|---|---|---|
| 1 | **Capability Maturity** | Rosemann (QUT) / CMMI | L1-L5 성숙도의 학파적 기반 |
| 2 | **Absorptive Capacity** | Cohen & Levinthal (1990) | 일부 기업이 L1 에 묶이는 이유 설명 — 사전 지식 부족 |
| 3 | **Task-Technology Fit (TTF)** | Goodhue & Thompson (1995) | Stage 7 To-Be 설계: 어떤 태스크가 L4 에 도달해야 하는지, 어떤 것이 L2 에 머물러야 하는지 |
| 4 | **Dynamic Capabilities** | Teece (1997, 2007) | sense / seize / transform — AI 거버넌스가 "역량"이지 "정책"이 아닌 이유 |
| 5 | **Sociotechnical Systems & Trust in AI** | Bostrom (1977) / Dietvorst (2015) / Glikson (2020) | L4-L5 에서 HITL 을 유지해야 하는 이유 — 인간은 순수 자율 AI 를 맹신하지 않음 |
| 6 | **Real Options Theory** | Dixit & Pindyck (1994) / McGrath (1997) | Phase 1 에서 NPV ≈ 0 인데도 투자 가치가 있는 이유 — 확장 옵션을 구매 중 |
| 7 | **Executable Knowledge Artifact** | Knuth (1984) Literate Programming + 현대적 확장 | 본 방법론이 PDF 가 아닌 Markdown + AI IDE 공독인 이유 |

➜ 전체 이론 논의 (인용 포함): [`ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md)
➜ 실패 패턴 (이론이 실패를 예측하는 곳): [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md)
➜ Pilot Study 설계 (18-24 개월 실증 계획): [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md)

---

## 5. 교육: L1-L5 완전 커리큘럼

각 레벨은 **자체 강의 자료 + 검증 가능 산출물 + Stage Gate 검수** 보유:

| 레벨 | 명칭 | 도구 | 강의 계획 |
|---|---|---|---|
| L1 | Controlled AI Access | OpenWebUI | [`../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md) |
| L2 | Knowledge Codification | Antigravity / Claude Code / Codex | [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) |
| L3 | Workflow Automation | n8n + Tiger AI Skill Pack | [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) |
| L4 | Autonomous Agent | Hermes Agent + Wiki | [`../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md) |
| L5 | Multi-Agent Organization | ClawTeam | (L5 는 [`L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md) 에 포함) |

**설계 원칙**: 고객이 L1-L5 를 한 번에 다 수강할 필요는 없음. 설문을 사용해 **즉시 산출 가능한 결과가 가장 빠른 계층**을 찾고, 위로 쌓아 올림. 강의 믹스는 기업 속성, 산업, 배포 방식 (클라우드 / 하이브리드 / 온프레), 리스크 요건으로 결정.

➜ 완전한 강의 패키지: [`../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](../02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
➜ 채점 보정 (주관 회피): [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) BARS

---

## 6. 컨설팅: 8 단계 + 3 단계 계약 모델

### 6.1 8 단계

| # | 단계 | 주요 액션 |
|---|---|---|
| 1 | **Awareness** | AI 인식 및 고객 비전 확립 |
| 2 | **Reference Model** | 고객을 Ideal Practice 레이더 서명으로 인도 |
| 3 | **Discovery** | As-Is 현황, Shadow IT, 시스템 인벤토리 수집 |
| 4 | **Gap Analysis** | Ideal Practice vs As-Is 비교; 고영향 갭 식별 |
| 5 | **Stakeholder Mapping** | Sponsor, AI Champion, HR, Compliance 식별 |
| 6 | **Diagnosis** | 계층 간 분석 (7 대 이론 기둥에의 정착 포함) |
| 7 | **To-Be Design** | TTF / Real Options 사용해 단계별 로드맵 설계 |
| 8 | **Acceptance Test** | Stage Gate sign-off + 분기별 레이더 리뷰 |

### 6.2 3 단계 계약

| Phase | 기간 | 주요 산출물 |
|---|---|---|
| **Phase A — 진단** | 2 주 | 중간 진단 보고서 + 서명된 Ideal Practice |
| **Phase B — 전략** | 4 주 | 완전한 14 장 컨설팅 보고서 + 24 개월 로드맵 + ROI + 거버넌스 제언 |
| **Phase C — 도입** | 24 개월 | 단계별 도입 + 분기별 레이더 리뷰 + 지속 진화 |

➜ 완전한 8 단계 스토리 (대화 예시 포함): [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md)
➜ 컨설팅 보고서 템플릿: [`../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)
➜ 컨설팅 툴킷 템플릿: [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md)
➜ 납품 패키지 & 검수: [`../06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](../06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)

---

## 7. 검증 가능 산출물: 각 레벨이 남기는 것

각 레벨의 "강의"는 강의가 끝나면 끝나는 게 아니라 — 감사 가능 evidence 를 남깁니다:

| 레벨 | 주요 산출물 | Evidence |
|---|---|---|
| L1 | 개인 채팅 영역, Prompt Library | 계정표, 권한표, 로그인 로그, Prompt 샘플 |
| L2 | Skill Library, Agentic artifacts | Skill 문서, 테스트 케이스, 버전 이력, 출력 샘플 |
| L3 | n8n Workflow PoC, Sub-workflow Library, Data Tables | 실행 로그, 재시도 로그, 시스템 연결 스크린샷 |
| L4 | 검증 가능 Agent, Briefing, task card | Agent log, Wiki 버전, HITL sign-off 로그 |
| L5 | Agent Team 역할 카드, 협업 플로우, 부서 간 성과 | Team run log, 인수인계 로그, 거버넌스 로그 |
| **컨설팅 레벨** | 14 장 진단 보고서, 30/60/90 일 로드맵, ROI, 거버넌스 제언 | Stage Gate sign-off 로그, 분기별 레이더 리뷰 |

➜ 완전 산출물 + evidence 매트릭스: [`../01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](../01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)

---

## 8. 이 책 사용법 (역할별 5 가지 진입 경로)

| 당신은 | 여기서 시작 (20 분 → 1 시간) |
|---|---|
| **CEO / 오너 / 방법론 이해 원하는 가족** | [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) — Ming 의 이야기 |
| **컨설턴트 / 학습자** | [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) — 완전한 8 단계 플로우 |
| **이사회 / 규제 / 학술** | [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) — 과학적 논증 |
| **엔터프라이즈 IT / 타사 컨설턴트** | [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) — McKinsey/BCG/TOGAF/Gartner 와의 정렬 |
| **방법론 연구자 / AI Pedagogy 학자** | [`AI_NATIVE_LIVING_BOOK_EN.md`](AI_NATIVE_LIVING_BOOK_EN.md) — 왜 새로운 형태의 방법론인지 |

---

## 9. 참고 자료 빠른 인덱스

### 9.1 학술 이론 & 실패 모드

- [`ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) — 7 대 이론 기둥 전체 논의
- [`../90_References/FAILURE_PATTERNS.md`](../90_References/FAILURE_PATTERNS.md) — 14 개 실패 모드 (이론 예측)
- [`../90_References/AI_GOVERNANCE_ALIGNMENT.md`](../90_References/AI_GOVERNANCE_ALIGNMENT.md) — NIST AI RMF / EU AI Act / ISO 42001 정렬
- [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) — 18-24 개월 실증 연구 설계

### 9.2 교육 & 평가

- [`../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) — 10/25/50 문항 설문 (평이한 언어)
- [`../01_Assessment/AI_MATURITY_SCORING_MODEL.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL.md) — 채점 모델
- [`../01_Assessment/BARS_RUBRICS_EN.md`](../01_Assessment/BARS_RUBRICS_EN.md) — BARS 채점 보정 (주관 회피)
- [`../02_Course_Design/`](../02_Course_Design/) — 완전한 L1-L5 강의 계획

### 9.3 컨설팅 납품

- [`../03_Consulting_Report/`](../03_Consulting_Report/) — 컨설팅 보고서 + 툴킷 템플릿
- [`../04_Scenarios/`](../04_Scenarios/) — 7 산업 시나리오 (제조 / 병원 / 마케팅 / B2B / 금융 / 정부 / 교육)
- [`../05_Sales/`](../05_Sales/) — 영업 토킹 포인트 + FAQ
- [`../06_Delivery/`](../06_Delivery/) — 납품 패키지 + 검수 기준 + Engagement Lifecycle

### 9.4 3 엔진 자기 공개

- [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) — 3 엔진 공저 README + §3 공저 기율
- [`../07_AI_Contributions/ANTIGRAVITY.md`](../07_AI_Contributions/ANTIGRAVITY.md) ｜ [`CODEX.md`](../07_AI_Contributions/CODEX.md) ｜ [`CLAUDE_CODE.md`](../07_AI_Contributions/CLAUDE_CODE.md)
- [`../CHANGELOG.md`](../CHANGELOG.md) — 3 엔진 공저 changelog

### 9.5 소스 자료

- [`../90_References/@AI-MD-PUBIC.pdf`](../90_References/@AI-MD-PUBIC.pdf) — 원본 PDF 방법론
- [`../90_References/MD-Map.png`](../90_References/MD-Map.png) — AI Maturity Map
- [`../90_References/Metholodgy.png`](../90_References/Metholodgy.png) — 8 단계 트랜스포메이션 가이드 다이어그램
- [`../90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](../90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md) — 비디오 학습 노트
- [`../90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](../90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

---

## 10. 다음 단계: 3 가지 권장 경로

| 당신의 필요 | 권장 다음 단계 |
|---|---|
| **전체 멘탈 모델 구축** | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE.md) (§3.0 두 축 전체 스토리 포함) |
| **자기 회사가 어느 레벨인지** | [`../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE.md) 의 10 문항 빠른 진단 |
| **AI 와 직접 공독** | AI IDE 로 이 레포 열기 → 먼저 root [`../README_KR.md`](../README_KR.md) §🚀 3 AI 엔진 설치 가이드 읽고 엔진 하나 시작 |

---

> ⚠️ **학술 무결성 선언**: 본 레포의 모든 명명된 케이스 (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education — 7 개 SAMPLE_CLIENT_CASE 파일) 및 모든 주인공 (예: "Ming" 과 "MingChang Packaging") 은 **AI 생성 가상 사례**이며, 실제 고객 데이터가 아닙니다. 모든 숫자 (시간, ROI, 인월, 예산, KPI) 는 **예시일 뿐**이며 **대외 홍보, 계약상 약속, 학술적 실증 증거로 사용해서는 안 됩니다**. 실제 longitudinal 케이스는 [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) 에 기재된 18-24 개월 실증 연구 완료 후에만 교체됩니다.
>
> **아키텍처 귀속**: 본 레포의 방법론 아키텍처는 인간 저자 **Morris Lu (Tiger AI)** 가 설계. 3 개 AI 엔진 (Antigravity / Codex / Claude Code) 은 **실행·보완·확장·감사** 도구입니다. [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) §0 참조.
