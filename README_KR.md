# GenAI Consulting Methodology Toolkit

언어: [繁體中文](README.md) | [English](README_EN.md) | [ภาษาไทย](README_TH.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [日本語](README_JA.md) | 한국어

기업 AI 트랜스포메이션 성숙도 진단 및 도입 방법론 툴킷 (Enterprise AI Transformation Maturity Assessment & Implementation Methodology Toolkit).

원작자: **Tiger AI Morris Lu 盧業興**  
소속: **n8n Taipei Ambassador / 국립대만과학기술대학교 지능제조연구소 박사과정 / QUT 퀸즐랜드 공과대학교 (호주) 컴퓨터과학 석사**

라이선스 요약: 본 프로젝트는 **[Apache License 2.0](LICENSE)** 을 채택합니다. 자유롭게 사용·복제·수정·재배포·상업화할 수 있습니다. 재배포 시 Apache 2.0 라이선스 텍스트와 [`NOTICE`](NOTICE) 의 저자 표기를 유지해 주세요.

> **5 분밖에 없으신가요?** 먼저 [`00_Overview/EXECUTIVE_SUMMARY_EN.md`](00_Overview/EXECUTIVE_SUMMARY_EN.md) 을 읽으세요 — 한 페이지로 전체 방법론을 이해합니다.

---

## 🌟 이것은 단지 책이 아니라 AI-Native Living Book — 진정으로 "살아있는" 책

책은 세대마다 진화해 왔습니다. 각 세대가 하나의 문제를 해결했지만 하나의 공백을 남겼습니다 — **어느 책도 진정으로 "살아있는" 책이 아니었습니다**:

- **1세대 — 인쇄 책**: 지식을 보존하여 다음 독자에게 전달합니다. 하지만 **읽을 수만 있을 뿐 답하지 않으며**, 당신의 질문에 답할 수 없고 당신의 회사가 어떤 모습인지 모릅니다 — **정적인 종이**일 뿐입니다.
- **2세대 — 인터랙티브 북**: 웹과 위키로 옮겨진 후 검색·링크·코멘트가 가능해졌습니다. 인쇄 책에 "**인터랙션**"이 더해졌지만, 여전히 **능동적으로 제안하지 않으며** 분석이나 새로운 산출도 하지 않습니다 — 여전히 수동적이며, 인터페이스만 살았고 콘텐츠는 살지 않았습니다.
- **3세대 — AI-Native Books (본 레포) — 진정으로 "살아있는" 책**: 방법론 본체를 Markdown 으로 작성하고 AI IDE 로 엽니다 — AI 가 전체 책을 자동으로 읽고 **당신이 묻게 하고, 당신을 위해 답하고, 당신과 함께 생각합니다**. 또한 **당신 회사의 실제 상황에 맞춰 맞춤형 권고를 제공하고, 진단을 실행하고, 보고서 초안을 작성하고, 시나리오를 시뮬레이션합니다**. 책 자체가 반응하고 확장하며 당신의 질문과 함께 새로운 챕터가 자라납니다.

다시 말해: 인쇄 책은 지식을 전달하고, 인터랙티브 북은 검색 가능하게 합니다. **AI-Native Book 은 "책"을 진정으로 살아있게 하는 최초의 책으로, 당신과 함께 생각하는 파트너가 됩니다**. 최종 결정은 여전히 인간이 내리지만, 더 이상 혼자서 정적인 방법론을 마주하지 않습니다.

> *Three generations of books: printed (read-only, dead) → interactive (search & link, still passive) → **AI-native (truly alive — advises, analyzes, simulates, and grows with your questions)**. Open with an AI IDE; AI becomes your reading partner, consulting assistant, and auditor.*

### 🔱 서로 다른 전문성을 가진 3 개의 AI 엔진

같은 콘텐츠라도 선택한 AI IDE 에 따라 **완전히 다른 인격**을 보여줍니다:

| 엔진 | 역할 | 가장 잘하는 것 |
| --- | --- | --- |
| 🟦 **Antigravity** | 최전선 컨설턴트 | 고객과 대화, 설문지 실행, 보고서 초안 작성 |
| 🟪 **Codex CLI** | 방법론 감사관 | 파일 간 테스트, 레드팀 연습, 버전 관리, 끊어진 링크 수리 |
| 🟨 **Claude Code** | 파일 간 사고 파트너 | 심층 종합, 다관점 토론, 시뮬레이션, 고객별 Fork |

3 개 엔진은 서로를 대체하지 않고 **분업 협력**합니다: 오전엔 Antigravity 로 고객 미팅, 오후엔 Codex 로 보고서 감사, 저녁엔 Claude Code 로 시나리오 시뮬레이션. 각 워크스페이스는 독립 (`.agent/` / `.codex/` / `.claude/`) 되어 서로 간섭하지 않습니다.

각 엔진의 상세한 자기 기술은 [`07_AI_Contributions/`](07_AI_Contributions/) 참조. 설치 단계는 아래의 [3 AI 엔진 설치 및 시작 가이드](#-3-ai-엔진-설치-및-시작-가이드--three-ai-engines-setup-guide) 참조.

### 다양한 역할의 독자에게 의미하는 것

- **CEO / 임원**: 이 레포를 ChatGPT / Claude / Gemini 에 던져넣고 10 분의 질의응답으로 "우리 회사는 어느 레벨에 있는가? 무엇부터 시작해야 하는가?"에 대한 초기 판단을 얻습니다.
- **컨설턴트 / 학습자**: AI IDE 로 열어 진단·보고서·24 개월 도입 로드맵까지 완전한 대화형 컨설팅 경험을 실행합니다.
- **학자 / 연구자**: `/devil-pair-debate`, `/thought-experiment` 를 직접 실행해 방법론의 가치관 전제를 토론합니다. 7 대 이론 기둥과 28 편의 인용 가능한 고전이 뒷받침합니다.
- **규제 / 컴플라이언스**: `/evidence-audit`, `/generate-traceability` 를 실행하여 감사 가능한 증거 체인을 확보하고 NIST AI RMF / EU AI Act / ISO 42001 과 정렬합니다.

> ⚠️ **정직한 공개**: 방법론의 전체 아키텍처는 **Morris Lu (인간)** 가 설계했습니다. 3 개 AI 엔진은 실행·보완·감사 도구에 불과합니다. 자세한 내용은 [`07_AI_Contributions/README.md`](07_AI_Contributions/README.md) §0. 책의 모든 케이스는 AI 시뮬레이션 교육 자료이며, **실제 고객 데이터가 아닙니다**.

---

## 이 방법론이 해결하는 과제

많은 기업이 AI 도입 시 도구로 바로 뛰어듭니다 — 오늘 ChatGPT 사고, 내일 n8n 시도하고, 다음 주 Agent 만들고 싶어합니다. 일반적인 문제: 직원이 사용하지 못함, 프로세스가 연결되지 않음, 데이터가 거버넌스되지 않음, PoC 검수 불가, 최종적으로 경영진도 AI 가 어느 성숙도에 있는지 모름.

본 툴킷의 전략: 먼저 간단한 설문으로 기업의 현재 AI 성숙도를 진단하고, L1-L5 에 따라 강의 비율과 도입 경로를 설계합니다. 강의는 수강 후 끝나는 것이 아니라 각 레벨마다 검증 가능한 산출물을 남기고, 마지막으로 AI 트랜스포메이션 진단의 8 단계 프로세스로 완전한 진단 보고서·로드맵·ROI·거버넌스 제언을 산출합니다.

## 강의 시작 전의 미래 상상

고객이 L1-L5 강의를 들을지 결정하기 전에 가장 필요한 것은 미래 그림을 먼저 보는 것: "다섯 가지 도구를 배운다"가 아니라 "**강의 후 회사의 일상 업무가 어떻게 바뀌는가?**"

스토리라인: **규모가 한 층씩 확장되고, 마침내 '인간이 AI 사용'에서 '`AI 가 스스로 일하는'으로 성장**: **개인 → 부서 → 부서 간/전사 → AI 슈퍼 어시스턴트 (엔티티) → AI 팀**. 3 개월 후 월요일 아침을 상상해 보세요:

- **L1 Controlled AI Access ─ 규모 축·개인**: **직원 한 명 한 명**이 자기 계정으로 OpenWebUI 에 로그인하고, 자기 채팅 영역, 이력, 부서 권한을 가집니다. 영업이 고객 메일 작성, HR 가 교육 요약, 매니저가 회의 요점 작성 — 모두 동일한 제어된 AI 진입점에서 시작. **단위는 "개인"**, AI 가 각 사람 곁에 있음.
- **L2 Knowledge Codification ─ 규모 축·부서**: **단위가 "부서"로 격상**. 시니어는 개인적으로만 잘하는 것이 아니라, **부서 책임을 경계**로 카피, 보고서, 고객 응대, SOP 해석, 개발 방법을 재사용 가능한 Skill 로 포장. 신입과 부서 내 다른 멤버가 같은 방법을 사용하여 **부서 전체** 산출 품질이 일관됨.
- **L3 Workflow Automation ─ 규모 축·부서 간 / 전사**: **단위가 "부서 간, 전사"로 다시 격상**. n8n 이 각 부서의 Skill 과 시스템 (Gmail, Sheets, Notion, CRM, API, ERP) 을 연결. 들어온 클레임 메일 한 통이 **영업, 고객 응대, CRM, 매니저 등 여러 부서를 가로질러** 자동 처리 — 시스템이 CRM 조회, 폼 업데이트, 태스크 생성, 매니저 요약 생성. 인간은 판단과 승인만. AI 가 이제 **전사 프로세스**에 진입.
- **L4 Autonomous Agent ─ AI 자율 축·슈퍼 어시스턴트 (AI 엔티티)**: **"인간 부대" 외에 추가로 AI 엔티티가 자랄**. Hermes Agent 가 매일 태스크, 문서, Workflow 결과, Wiki 기억을 읽고 briefing, 추적 리스트, HITL (Human-in-the-Loop, 인간이 루프 안에서 검토) 가 필요한 결정점을 생성. 기업이 이제 **검증 가능한 지식형 AI 엔티티**를 보유, 완전 자동 슈퍼 어시스턴트를 한 명 더 채용한 셈.
- **L5 Multi-Agent Organization ─ AI 자율 축·AI 팀**: **여러 L4 엔티티가 다시 "AI 팀"으로 편성**. ClawTeam 이 마케팅, 제품, 고객 응대, 재무, 운영의 전문 Agent 를 기능 분업으로 편성, 신제품 출시, 품질 개선, 환자 서비스 개선, 고객 운영 태스크를 협업 수행. 기업이 **"인간 팀 + AI 팀" 두 팀**을 동시에 보유.

이 스토리는 강의 시작 전에 들려줘야 합니다. 고객이 "**규모가 어떻게 한 층씩 확장되는지, AI 가 어떻게 도구에서 디지털 인력으로 성장하는지**"를 이해한 후, 왜 설문 진단이 필요한지, 왜 강의를 L1-L5 로 나누는지, 왜 각 레벨에 deliverables, evidence, Stage Gate 가 필요한지를 되짚어 이해할 수 있습니다.

> ⚠️ 두 축에 대한 더 자세한 설명 (왜 L3 → L4 가 중요 분기점인지, 왜 거버넌스는 항상 인간이 보유하는지) 은 아래의 [§L1-L5 의 두 축](#l1-l5-의-두-축) 을 참조.

## AI 성숙도 맵

![AI Maturity Map](90_References/MD-Map.png)

## 방법론 개요

![Enterprise Consulting Methodology: Eight-Stage Transformation Guide](90_References/Metholodgy.png)

## 메인 스토리라인

```text
AI 성숙도 설문
→ 기업 속성·산업 상황·배포 방식 조사
→ L1-L5 강의 비율 설계
→ L1 OpenWebUI 기업 계정 및 개인 채팅 영역 활성화
→ L2 Antigravity / Claude Code / Codex 로 Skill 화 훈련
→ L3 n8n 으로 Gmail, Sheets, Notion, CRM, API, ERP 등 시스템 연결
→ L4 Hermes Agent 로 검증 가능한 자동 Agent 업무 형성
→ L5 ClawTeam 으로 Agentic Team 협업
→ 시나리오 케이스, Evidence, Stage Gate
→ 8 단계 AI 트랜스포메이션 컨설팅 진단
→ AI 트랜스포메이션 진단 보고서, 로드맵, ROI, 거버넌스 제언
```

## L1-L5 성숙도 모델

| 레벨 | 명칭 | 도구 / 플랫폼 | 축 | 기업 포지셔닝 |
| --- | --- | --- | --- | --- |
| L1 | Controlled AI Access | OpenWebUI | 규모 축·개인 | 기업 내부 AI 대화 진입점을 구축하여 모든 직원에게 전용 계정, AI 채팅 영역, 권한 경계 제공 |
| L2 | Knowledge Codification | Antigravity / Claude Code / Codex | 규모 축·부서 | 부서 책임을 단위로 개인 지식·프롬프트·문서·업무 방법을 재사용 가능 Skill 로 정리 |
| L3 | Workflow Automation | n8n | 규모 축·부서 간 / 전사 | 부서 간 Skill 을 연결하고 email, Sheets, Notes, CRM, API, ERP 등 시스템과 결합, AI 를 전사 자동화 프로세스에 진입 |
| L4 | Autonomous Agent | Hermes Agent | AI 자율 축·슈퍼 어시스턴트 | Wiki 역량 맵, AI 도구, Workflow, 자동 스케줄링, 자율 학습을 결합한 검증 가능한 완전 자동 AI Agent 슈퍼 어시스턴트 |
| L5 | Multi-Agent Organization | ClawTeam | AI 자율 축·AI 팀 | 여러 전문 Agent 가 기능 분업을 형성하여 부서·프로세스를 가로지르는 기업 태스크를 AI 팀으로 협업 완료 |

### L1-L5 의 두 축

L1-L5 는 "다섯 개의 도구"가 아니라 **두 개의 축**으로 연결된 성숙도 경로:

- **L1 → L2 → L3: 규모 축 (인간이 AI 사용 / 감독)**. 이 세 층은 "인간이 루프 안, 인간이 AI 사용, 인간이 AI 감독"의 단계로, 조직 규모를 따라 단계적 확장 — **L1 개인** (각 직원이 개별 AI 사용) → **L2 부서** (부서 책임 단위로 개인 지식을 재사용 가능 Skill 로 캡슐화) → **L3 부서 간 / 전사** (부서 간 Skill 연결, 시스템과 결합, AI 가 전사 자동화에 진입).
- **L4 → L5: AI 자율 축 (AI 가 완전 자율, 인간의 실시간 감독 불필요)**. 이 두 층은 기업이 인간 부대 외에 "**추가로 자라게 한**" AI 엔티티 — **L4 AI 슈퍼 어시스턴트** (완전 자동 AI Agent 엔티티) → **L5 AI 팀** (여러 전문 Agent 기능 분업 협업).

> 중요 분기점: **L1-L3 는 "인간이 AI 보조 / 감독", AI 는 도구; L4-L5 는 "AI 가 자율 운영", AI 는 기업의 추가 디지털 인력.** 도입 순서로는 L1-L3 가 먼저 사람과 조직을 끌어올리고, L4-L5 가 견고한 기반 위에 자율 AI 로 성장.
>
> L4-L5 에 이르러도 **거버넌스 프레임은 여전히 인간이 구축, 인간이 감독권 보유** — AI 가 자율하는 것은 "운영 실행"이며 "거버넌스 결정"이 아님. 각 층은 HITL (Human-in-the-Loop) 과 Stage Gate 를 유지, AI 가 자율할수록 인간의 역할은 "거버너"로 격상 — 대체되지 않음.

## 각 레벨의 검수 방법

| 레벨 | Input | Process | Output | Evidence | Stage Gate |
| --- | --- | --- | --- | --- | --- |
| L1 | 직원 역할, 빈번한 태스크, AI 페인 포인트, 권한 요구 | OpenWebUI 구축, 계정 / 그룹 / 권한, 개인 채팅 영역, Prompt 기초 훈련 | 기업 AI 대화 진입점, Prompt 목록, 유스 케이스 목록 | 계정표, 권한표, 로그인 로그, 채팅 영역 스크린샷, Prompt 샘플 | 안전 로그인, 권한 분리, 추적 가능한 사용 기록을 남길 수 있는가 |
| L2 | L1 빈번한 Prompt, 문서, SOP, 개인 업무 방법 | Antigravity / Claude Code / Codex 로 지식을 Skill 과 재사용 가능 artifact 로 캡슐화 | Skill Library, Agentic artifacts, Workflow Blueprint | Skill 문서, 테스트 케이스, 버전 이력, 출력 샘플 | Skill 이 타인에 의해 재사용되고 안정적 출력을 낼 수 있는가 |
| L3 | L2 Skill, 프로세스 블루프린트, 시스템 목록, API / CRM / ERP / Sheet 권한 | n8n 으로 자동화 플로우, Data Table, Execution Log, 오류 처리 구축 | Workflow PoC, Sub-workflow Library, Data Tables, L4 Workflow Contract | n8n workflow, execution log, 재시도 로그, 시스템 연결 스크린샷 | Workflow 가 실제 데이터·실제 시스템에서 안정 가동되는가 |
| L4 | L3 Workflow, L2 Skill, 기업 Wiki, 태스크 규칙, HITL 인간 검토 지점 | Hermes Agent 로 task card, Wiki ingest/query/update, 스케줄링, 도구 호출, Gate 4A-4E 구축 | 검증 가능 Agent, Briefing, 태스크 처리 로그, Gate sign-off | Agent log, Wiki 버전, task card, briefing, 인간 승인 기록 | Agent 가 제어 경계 내에서 자율적으로 태스크 완수하고 evidence 남길 수 있는가 |
| L5 | 여러 L4 Agent, 부서 간 태스크, 역할 책임, 거버넌스 규칙 | ClawTeam 으로 Agentic Team 편성, 역할·협업 규칙·인수인계·감독 정의 | Agent Team, 역할 카드, 협업 플로우, 부서 간 성과 | Team run log, 역할 카드, 인수인계 로그, 성과 문서, 거버넌스 로그 | Agent Team 이 안정 협업하고 추적 가능한 성과를 낼 수 있는가 |

## 강의 설계 원칙

강의 비율은 고객의 성숙도, 산업, 배포 방식, 목표 시나리오로 결정. 모든 기업이 L1-L5 를 한 번에 다 수강할 필요는 없음 — 먼저 즉시 산출 가능한 결과를 낼 수 있는 층을 찾고, 위로 이어 나감.

| 조사 차원 | 용도 |
| --- | --- |
| 기업 속성 | 연구개발 제조, 마케팅 서비스, 의료기관, 내부 운영, 기타 중 판단 |
| 배포 방식 | 클라우드 AI, 하이브리드, 풀 온프레미스 중 |
| 시스템 현황 | Gmail, Sheets, Notion, CRM, API, ERP, 데이터베이스, 내부 시스템 파악 |
| 프로세스 성숙도 | SOP, process owner, 데이터 필드, 예외 처리 존재 여부 판단 |
| 리스크 요구 | 보안, 프라이버시, 의료 / 제조 / 금융 컴플라이언스, 인간 sign-off 필요 평가 |

## 디렉터리 구조

| 디렉터리 | 용도 |
| --- | --- |
| [`00_Overview`](00_Overview/) | 솔루션 개요, 메인 스토리, WBS |
| [`01_Assessment`](01_Assessment/) | AI 성숙도 설문, 채점 모델, 산출물과 evidence 매트릭스 |
| [`02_Course_Design`](02_Course_Design/) | L1-L5 강의 설계, 기업 속성, 배포 방식, 강의 모듈 매트릭스 |
| [`03_Consulting_Report`](03_Consulting_Report/) | AI 트랜스포메이션 진단 보고서 템플릿 |
| [`04_Scenarios`](04_Scenarios/) | 고객 시나리오, 컨트롤 테이블, 제조업 케이스, 병원 케이스 |
| [`05_Sales`](05_Sales/) | 가치 제안, 영업 토킹 포인트, FAQ |
| [`06_Delivery`](06_Delivery/) | 납품 패키지와 검수 기준 |
| [`90_References`](90_References/) | 원본 PDF, 방법론 다이어그램, 비디오 학습 노트, 인용 |

## 5 가지 독자 유형, 이 5 개로 시작

| 당신은 | 여기서 시작 |
| --- | --- |
| **CEO / 오너 / 가족** — 20 분에 방법론 이해 | [`00_Overview/CLIENT_JOURNEY_STORY_EN.md`](00_Overview/CLIENT_JOURNEY_STORY_EN.md) — Ming 의 이야기 |
| **컨설턴트 / 학습자** — 8 단계 운영 방식, 계약 분할 방식 | [`00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md`](00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md) — 완전 플로우 |
| **이사회 / 규제 / 학술** — 왜 이 방법론이 토론을 견디는가 | [`00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) — 과학적 논증 |
| **대기업 IT / 타사에서 이직한 컨설턴트** — McKinsey/BCG/TOGAF/Gartner 와의 정렬 | [`00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) — 정렬 맵 |
| **바쁜 임원** — 5 분만 | [`00_Overview/EXECUTIVE_SUMMARY_EN.md`](00_Overview/EXECUTIVE_SUMMARY_EN.md) — Executive Summary |
| **방법론 연구자 / AI Pedagogy 학자** — 왜 새로운 방법론인가 | [`00_Overview/AI_NATIVE_LIVING_BOOK_EN.md`](00_Overview/AI_NATIVE_LIVING_BOOK_EN.md) — AI-Native Living Book 설계 |
| **학자 / 규제 / 이사회** — 7 대 이론 기둥 (Rosemann / Cohen & Levinthal / Teece / Real Options 등) | [`00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) — 학술 이론 기초 |
| **컨설턴트 / 채점 캘리브레이션** — 0-4 점 객관적 채점 방법 | [`01_Assessment/BARS_RUBRICS_EN.md`](01_Assessment/BARS_RUBRICS_EN.md) — BARS Behavioral Anchors |

## 권장 독서 순서

1. [`00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md)
2. [`01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](01_Assessment/AI_MATURITY_QUESTIONNAIRE.md)
3. [`01_Assessment/AI_MATURITY_SCORING_MODEL.md`](01_Assessment/AI_MATURITY_SCORING_MODEL.md)
4. [`01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)
5. [`02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
6. [`02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md)
7. [`02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md)
8. [`02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md)
9. [`02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md)
10. [`04_Scenarios/CASE_CONTROL_TABLES.md`](04_Scenarios/CASE_CONTROL_TABLES.md)
11. [`06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)
12. [`03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)

## 검증 가능한 산출물

- AI 성숙도 설문과 채점 결과
- 기업 속성과 배포 방식 조사
- L1-L5 강의 수료 evidence
- OpenWebUI 계정 / 그룹 / 권한표와 개인 채팅 영역 활성화 로그
- Skill Library 와 Antigravity / Claude Code / Codex artifacts
- n8n Workflow PoC, Execution Log, Data Tables, Sub-workflow Library
- Hermes Agent task card, Wiki, ingest/query/update 로그, briefing, Gate 4A-4E
- ClawTeam Agent Team 역할 카드, 협업 로그, 성과 문서
- Stage Gate 검수 기록
- AI 트랜스포메이션 진단 보고서
- 30 / 60 / 90 일 로드맵

## 참고 자료

- [`90_References/@AI-MD-PUBIC.pdf`](90_References/@AI-MD-PUBIC.pdf)
- [`90_References/MD-Map.png`](90_References/MD-Map.png)
- [`90_References/Metholodgy.png`](90_References/Metholodgy.png)
- [`90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md)
- [`90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

## 감사의 글

특별히 **Prof. Michael Rosemann** (Queensland University of Technology (QUT), Brisbane, 호주) 에게 감사드립니다.  
프로필: <https://www.qut.edu.au/about/our-people/academic-profiles/m.rosemann>

본 레포의 컨설팅 방법론 전체의 이론적 기반은 저자가 QUT 에서 수학한 기간과 Prof. Michael Rosemann 의 **Business Process Management (BPM)**, **Capability Maturity Models**, **기업 혁신 방법론** 에서의 장기적 영감과 지도에서 비롯되었습니다.

특히 영향을 받은 두 가지 핵심 설계:

- **8 단계 컨설팅 구조**: 기업 프로세스 진단, 능력 평가, 트랜스포메이션 경로 설계, 거버넌스 구현에 대응.
- **L1-L5 AI 성숙도 모델**: Capability Maturity Model 의 계층 논리를 참조하여 기업 AI 도입을 위한 5 계층 프레임워크로 현지화.

면책 조항: 본 방법론의 모든 오류, 누락, 현지화 조정, AI 영역으로의 확장 응용은 모두 저자 Tiger AI Morris Lu 盧業興 의 개인 책임이며 Prof. Michael Rosemann 또는 QUT 의 견해나 입장을 대표하지 않습니다.

## 라이선스와 표기

본 프로젝트는 **[Apache License 2.0](LICENSE)** 으로 배포됩니다. 자유롭게 사용·복제·수정·각색·재생산·배포·교육·컨설팅 납품·상업화할 수 있습니다.

재배포, 각색, 상업 패키징, 강의 자료, 컨설팅 납품 문서, 제품 문서에 사용할 때는 Apache 2.0 라이선스 텍스트와 [`NOTICE`](NOTICE) 의 다음 표기를 유지해 주세요:

```text
Original Author: Tiger AI Morris Lu 盧業興
Role: n8n Taipei Ambassador / PhD Student, Graduate Institute of Intelligent Manufacturing, National Taiwan University of Science and Technology / M.IT, Queensland University of Technology (QUT), Australia
Source: https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit
```

타사 플랫폼 명칭, 상표, 비디오, 외부 프로젝트, 인용 콘텐츠는 각 권리자에게 속합니다. 본 레포는 타사 자료를 학습 노트, 인용, 정리, 강의 설계 참조로만 사용합니다.

---

## 이 책을 살아있게 만들기: AI 와 함께 읽기

아래 설치 가이드는 레포를 AI IDE 와 연결하는 절차를 안내합니다. 시작 전에 운영 모델과 한 줄의 레드라인을 이해해 두세요.

**운영 모델 한 줄로**: `git clone` 또는 zip 다운로드 → AI IDE (Antigravity / Claude Code / Codex 등) 로 열기 → AI 가 [`AGENTS.md`](AGENTS.md) (와 각 엔진 고유의 `<ENGINE>.md`) 를 자동으로 읽고 **본 방법론의 공동 독해 튜터**로 자신을 위치시킴. 이후 (1) 방법론에 대해 무엇이든 질문, (2) 방법론을 회사 상황에 적용 요청, (3) L1-L5 자가 진단을 함께 진행하여 다음 단계 찾기 가능.

완전한 논의는 [`00_Overview/AI_NATIVE_LIVING_BOOK_EN.md`](00_Overview/AI_NATIVE_LIVING_BOOK_EN.md) 참조.

> ⚠️ **학술 무결성 선언 / Academic Integrity Disclaimer**
>
> **본 레포 내 명명된 모든 케이스 (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education — 7 개 SAMPLE_CLIENT_CASE) 및 주인공 (예: "Ming" / "MingChang Packaging") 은 AI 생성 가상 사례**이며 실제 고객 데이터가 아닙니다.
> 모든 숫자 (시간, ROI, 인월, 예산, KPI) 는 **예시일 뿐**이며 **대외 홍보, 계약상 약속, 학술적 실증 증거로 사용할 수 없습니다**.
> 실제 longitudinal 케이스는 [`90_References/PILOT_STUDY_PROTOCOL_EN.md`](90_References/PILOT_STUDY_PROTOCOL_EN.md) 의 18-24 개월 실증 연구 완료 후에야 교체됩니다.
>
> **All named cases and story protagonists in this repo are AI-generated fictional examples**, NOT real client data.

## 🚀 3 AI 엔진 설치 및 시작 가이드 / Three AI Engines Setup Guide

3 개 엔진의 **역할과 분업**은 위 "🔱 서로 다른 전문성을 가진 3 개의 AI 엔진"에서 소개 완료. 이 섹션은 **설치 방법, 시작 방법, 워크플로 호출 방법**에 집중. 3 개 서브섹션은 독립 — 사용할 엔진을 골라 그 부분만 읽으세요.

> ⚠️ **[`07_AI_Contributions/README.md`](07_AI_Contributions/README.md) §0 에 따라**: 방법론 아키텍처, L1-L5, 8 단계, 3 엔진 분업 등 전략 설계는 모두 **Morris Lu (인간)** 가 제안. 3 개 AI 엔진은 Morris 의 지도 아래 **실행·보완·확장·감사**, 방법론 아키텍처의 소유권을 주장하지 않음. 각 엔진의 상세 자기 기술은 [`07_AI_Contributions/`](07_AI_Contributions/) 의 해당 파일 참조.

---

### 🟦 1. Antigravity 사용자 — 최전선 인터랙티브 컨설턴트

> 이 "정적인 살아있는 책"을 직접 당신의 "**Conversational Consulting App**" 으로 업그레이드.

**설치 및 사용 단계:**

1. **프로젝트 로드**: `git clone` 또는 zip 다운로드하여 로컬로
2. **IDE 시작**: Antigravity 로 프로젝트 폴더 열기
3. **자동 초기화**: Antigravity 가 [`ANTIGRAVITY.md`](ANTIGRAVITY.md) 와 [`SKILL.md`](SKILL.md) 자동 독해, "**공동 독해 튜터**"로 자기 위치
4. **워크플로 (Slash Commands) 실행**: 대화 박스에 명령 입력하여 인터랙션 시작

**자주 쓰이는 Antigravity 명령:**

- `/diagnose` ── 사실적 대화 시작, 당신 (또는 고객) 을 L1-L5 기업 AI 성숙도 진단으로 안내
- `/generate-report` ── 이전 진단과 논의 결과를 표준 컨설팅 보고서 템플릿에 기록하고 초안 생성

자세히는 [`.agent/workflows/`](.agent/workflows/) 와 [`07_AI_Contributions/ANTIGRAVITY.md`](07_AI_Contributions/ANTIGRAVITY.md) 참조.

> Antigravity 의 핵심 가치: 방법론을 **고객이 알아듣고 즉시 인터랙션 가능한** 컨설팅 경험으로 변환.

---

### 🟪 2. Codex 사용자 — 방법론 엔지니어링 엔진

> 본 레포를 "**방법론 엔지니어링 워크스페이스**" 로 간주 — 이 AI-native living book 을 **테스트 가능·감사 가능·추적 가능·수리 가능·릴리스 가능**한 방법론 제품으로 유지.

**설치 및 사용 단계:**

1. **프로젝트 로드**: `git clone` 또는 zip 다운로드하여 로컬로
2. **Codex 시작**: Codex 에서 프로젝트 폴더 열기
3. **Codex 진입 파일 독해**: Codex 에게 [`CODEX.md`](CODEX.md) 와 [`.codex/README.md`](.codex/README.md) 를 먼저 읽도록
4. **Codex 워크플로 실행**: 대화에서 워크플로 이름 입력, 또는 Codex 에게 대응 파일 따르도록 명시

**자주 쓰이는 Codex 명령 (10 개):**

| 카테고리 | 명령 | 용도 |
| --- | --- | --- |
| Production | `/diagnose` | 인터랙티브 AI 성숙도 초기 판정 |
| Production | `/generate-report` | 컨설팅 진단 보고서 초안 |
| Quality | `/evidence-audit` | 보고서의 evidence chain 점검 |
| Quality | `/consistency-review` | 문서 간 L1-L5, Stage Gate, HITL, Evidence 일관성 점검 |
| Evolution | `/academic-upgrade` | 학술 권고를 방법론 수리 안으로 변환 |
| Evolution | `/harvest-insights` | 여러 납품 보고서에서 공통 insight 수확 |
| Defense | `/test-methodology` | 방법론을 극단 시나리오에서 stress test |
| Defense | `/red-team-review` | 컨설팅 보고서 초안의 red-team review |
| Audit | `/generate-traceability` | questionnaire → maturity → evidence → report 추적 매트릭스 생성 |
| DevOps | `/bump-version` | 시맨틱 버전 bump 와 CHANGELOG 제안 |

**권장 호출 방법:**

```text
.codex/workflows/evidence-audit.md 에 따라 이 컨설팅 보고서 초안을 점검해 주세요.
```

자세히는 [`.codex/workflows/`](.codex/workflows/) 와 [`07_AI_Contributions/CODEX.md`](07_AI_Contributions/CODEX.md) 참조.

> Codex 의 핵심 가치: 본 방법론에 "**테스트 가능·감사 가능·추적 가능·수리 가능·릴리스 가능**" 한 엔지니어링 라이프사이클을 부여.

---

### 🟨 3. Claude Code 사용자 — 파일 간 전략 사고 및 실험 엔진

> 방법론을 **연기 / 시도 / 해체 / 충돌** 시키기. Claude Code 의 1M context + 멀티 페르소나 병렬 + 도메인 간 추상 추론을 활용, **시뮬레이션, 실험, 토론, Fork**.

**설치 및 사용 단계:**

1. **프로젝트 로드**: `git clone` 또는 zip 다운로드하여 로컬로
2. **Claude Code 시작**: Claude Code CLI / IDE 에서 프로젝트 폴더 열기
3. **Claude Code 진입 파일 독해**: Claude Code 에게 [`CLAUDE.md`](CLAUDE.md) 와 [`.claude/README.md`](.claude/README.md) 를 먼저 읽도록
4. **Claude Code 워크플로 실행**: 대화에서 워크플로 이름 입력

**자주 쓰이는 Claude Code 명령 (10 개):**

| 카테고리 | 명령 | 용도 |
| --- | --- | --- |
| Tier 1 Tactical | `/deep-synthesize` | 다중 파일 심층 종합 (1M context) |
| Tier 1 Tactical | `/theory-bridge` | 고객 상황 ↔ 7 대 이론 기둥 대응 |
| Tier 1 Tactical | `/scenario-planning` | 제약 조건에서 3 개의 대비 로드맵 + tradeoff 생성 |
| Tier 1 Tactical | `/socratic-challenge` | 소크라테스식 질문으로 사용자 사고 연마 |
| Tier 1 Tactical | `/cross-stage-trace` | 단일 변경의 downstream 영향 추적 |
| Tier 2 Original | `/simulate-engagement` | 30 분 내 완전한 6 주 컨설팅 안건 실행 (12+ deliverable) |
| Tier 2 Original | `/parallel-perspectives` | 6 명의 이해관계자가 **동시에** 동일 결정에 의견 + 갈등 맵 |
| Tier 2 Original | `/thought-experiment` | 방법론의 counterfactual stress test ("EU AI Act 가 L4 를 불법화한다면?") |
| Tier 2 Original | `/devil-pair-debate` | Two-Claude 의 진정한 토론 + 판사의 종합 |
| Tier 2 Original | `/methodology-fork` | 표준 방법론을 고객 특화 버전으로 Fork (Methodology-as-Code) |

**권장 호출 방법:**

```text
.claude/workflows/simulate-engagement.md 에 따라 500 명 규모 제조업 고객의
6 주 컨설팅 안건을 시뮬레이션해 주세요.
```

자세히는 [`.claude/workflows/`](.claude/workflows/) 와 [`07_AI_Contributions/CLAUDE_CODE.md`](07_AI_Contributions/CLAUDE_CODE.md) 참조.

> Claude Code 의 핵심 가치: 방법론을 "**표준**" 에서 "**표준 + N 개 파생 + 완전 시뮬레이션 + 다관점 토론**" 으로 진화시킨 실험 가능한 살아있는 책.

---

### 3 엔진 협업 제안 / Three-Engine Workflow Suggestions

실무에서 자주 보이는 협업 리듬:

```text
Phase A 고객 진단
  → Antigravity 가 /diagnose 로 현황 수집
  → Claude Code 가 /theory-bridge 로 이론 진단 대응
  → Antigravity 가 /generate-report 로 중간 보고서 초안 산출
  → Codex 가 /evidence-audit 로 evidence chain 감사
  → Codex 가 /consistency-review 로 파일 간 정렬

Phase B 전략 설계
  → Claude Code 가 /scenario-planning 으로 3 개 로드맵
  → Claude Code 가 /parallel-perspectives 로 6 이해관계자 관점
  → Codex 가 /red-team-review 로 과도 낙관 공격
  → Claude Code 가 /devil-pair-debate 로 가치관 전제 토론

Phase C 도입과 진화
  → Codex 가 /generate-traceability 로 분기별 감사
  → Claude Code 가 /thought-experiment 로 counterfactual stress test
  → Codex 가 /bump-version 으로 방법론 버전 관리
  → Claude Code 가 /methodology-fork 로 대형 고객용 파생판 작성
```

> 3 엔진의 워크플로는 배타적이 아님 — **요점은 각 엔진이 가장 잘하는 일을 하는 것**, 인간 (컨설턴트 / Client Owner / Sponsor) 이 엔진 전환 타이밍을 결정합니다.
