# 90 References — 참고 자료, 출처와 감사

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)

## 1. 본 디렉토리의 목적

본 디렉토리는 방법론 전체의 **「참고문헌 라이브러리, 인용 거버넌스 센터, 감사 리스트」**. `00`-`07` 은 「방법과 도구」를 다룸；본 디렉토리는 3 가지를 답함：

1. **이 방법들은 무엇에 기반하는가?**（원본 PDF, 방법론 다이어그램, 영상 학습 노트）
2. **어떤 내용이 제3자를 인용하는가? 라이선스는 컴플라이언스한가?**（인용된 각 프로젝트는 자체 `*_REFERENCE.md` 보유）
3. **우리는 누구의 어깨 위에 서 있는가?**（감사 리스트）

대상: 컨설턴트, 리뷰어, 법무, 재배포자, **상류 프로젝트를 찾는 학습자와 애호가**.

---

## 2. 감사: 우리가 서는 어깨

사용 레벨로 4 카테고리로 정리: **Core 플랫폼 / 컨설팅 프레임워크 / Agent & Skill / Case-Index**. 각 「Appreciation Card」 는 **상류 URL + 어디서 인용하는가 + 완전한 `_REFERENCE.md` 링크** 포함.

### 2.1 Core 플랫폼 (L1-L5 의 런타임 기반)

이들은 「인용 자료」가 아니라 — **L1-L5 코스가 돌아가는 플랫폼**. 이들 없이는 본 방법론이 착지할 수 없음.

#### 🎯 [`open-webui/open-webui`](https://github.com/open-webui/open-webui)（오픈소스, 라이선스는 상류 LICENSE 참조）

- **무엇인가**: 오픈소스, 셀프호스트 가능한 엔터프라이즈 AI 채팅 인터페이스. 다중 LLM 프로바이더（OpenAI / Anthropic / Ollama / OpenRouter / Azure 등）, 계정 / 그룹 / 역할 / 권한, 개인 채팅 워크스페이스, 모델 컨트롤, Pipelines, Function Calling, 지식 베이스, RAG, 이미지/오디오/파일 업로드 지원.
- **왜 평가하는가**: 「**기업 내 AI 채팅 진입점**」을 「**원클릭 설치, 완전 온프렘, 권한 계층, 감사 가능**」으로 만드는 몇 안 되는 오픈소스 솔루션 중 하나. 데이터를 SaaS 로 보내지 않고 LLM 시도 가능 — 제조 / 헬스케어 / 정부의 온프렘 배포에 critical. 활발한 커뮤니티, 빠른 버전 진화.
- **어디서 쓰는가**: **L1 Controlled AI Access 의 Core 플랫폼** — [`../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](../02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md) 완전 코스 계획; 영상 학습 노트는 [`OPENWEBUI_VIDEO_LEARNING_NOTES.md`](OPENWEBUI_VIDEO_LEARNING_NOTES.md).

#### 🎯 [`n8n-io/n8n`](https://github.com/n8n-io/n8n)（Sustainable Use License, 상류 LICENSE.md 참조）

- **무엇인가**: 오픈소스 워크플로 자동화 플랫폼. 비주얼 에디터, 1000+ 통합（Gmail, Sheets, Notion, Slack, CRM, API, ERP, 데이터베이스, Webhook, 커스텀 노드）, 서브워크플로 라이브러리, Data Tables, Execution Logs, 에러 핸들링, 스케줄 트리거, AI / LangChain 노드. Self-Host 와 Cloud 지원.
- **왜 평가하는가**: 크로스시스템 자동화의 「**레고 블록**」 — 컨설턴트는 1-2 일 안에 고객 데모용 PoC 조립 가능. 활발한 커뮤니티, 풍부한 템플릿, 건강한 비즈니스 모델. **Self-Hosting 은 엔터프라이즈 채택에 critical**（데이터는 내부 유지）. 방법론 저자는 n8n Taipei Ambassador 이기도.
- **어디서 쓰는가**: **L3 Workflow Automation 의 Core 엔진** — [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) 완전 코스 계획; 35 개 구현 가능 PoC 스펙 [`../02_Course_Design/POC_SCENARIO_SPECS.md`](../02_Course_Design/POC_SCENARIO_SPECS.md); 30 개 워크플로 JSON 스켈레톤 [`../02_Course_Design/N8N_WORKFLOW_TEMPLATES.md`](../02_Course_Design/N8N_WORKFLOW_TEMPLATES.md); 영상 노트는 [`TIGERAI_VIDEO_LEARNING_NOTES.md`](TIGERAI_VIDEO_LEARNING_NOTES.md).

#### 🎯 [`nousresearch/hermes-agent`](https://github.com/nousresearch/hermes-agent)（Nous Research, 상류 LICENSE 참조）

- **무엇인가**: Nous Research 의 오픈소스 **Knowledge-grade Autonomous Agent** 레퍼런스 구현 — **Wiki-Capability-Map-Memory + ingest / query / update 3 단계 Knowledge-Compounding + 스케줄 태스크 + Gate 4A-4E + HITL Human Review**. 설계 목표: 검증 가능한 「완전 자율 AI Agent 슈퍼 어시스턴트」.
- **왜 평가하는가**: 「**Autonomous Agent + Knowledge Management**」을 검증 가능한 design pattern 으로 통합 — **「Knowledge-grade Agents 의 일곱 설계 원칙」**（light-day-heavy-night / Knowledge-Compounding-Loop / P1>P2 / Write-Read-Same-Source / Tool-vs-LLM-Division / Failure-driven Learning / Why-not-just-RAG）은 L4 Agent Design 에 완전한 학습 프레임워크 제공.
- **어디서 쓰는가**: **L4 Autonomous Agent 코스의 설계 백본** — [`../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](../02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md) §2 가 일곱 원칙 설명. **경계**: 코스는 **컨셉과 design pattern 만 취함 — 소스 코드 재현 안 함, 포크 안 함**.

#### 🎯 [`HKUDS/ClawTeam`](https://github.com/HKUDS/ClawTeam)（HKUDS, MIT）

- **무엇인가**: HKU Data Science Lab（HKUDS）의 오픈소스 **Multi-Agent Collaboration Framework**. 5 층 아키텍처（Team / Workspace / Task / Inbox / Transport）, 격리된 Agent 워크스페이스용 git worktree; CLI-driven; 3 개 레퍼런스 시나리오.
- **왜 평가하는가**: 「Multi-Agent Team Collaboration」을 데모 스케일에서 「**실 워크플로 감사 가능 협업**」으로 밀어 올림 — 각 Agent 는 자체 worktree, 자체 Inbox, 자체 Transport 보유. 채팅풍 toy demo 가 아니라, 실제 조직 분업에 가까움. 학술 배경（HKUDS）+ MIT 라이선스.
- **어디서 쓰는가**: **L5 Multi-Agent Organization 의 구현 플랫폼** — [`../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md`](../02_Course_Design/L5_CLAWTEAM_COURSE_PLAN.md) 완전 코스 계획; Manufacturing QA Team Walkthrough 는 [`../04_Scenarios/CLAWTEAM_WALKTHROUGH.md`](../04_Scenarios/CLAWTEAM_WALKTHROUGH.md).
- **완전 인용**: [`CLAWTEAM_REFERENCE.md`](CLAWTEAM_REFERENCE.md)

### 2.2 컨설팅 프레임워크 (03_Consulting_Report 에 영향)

#### 🎯 [`yoichiojima-2/consultant`](https://github.com/yoichiojima-2/consultant)（MIT）

- **무엇인가**: 고전적 컨설팅 분석 프레임워크（MECE, Pyramid Principle, Issue Tree, Porter's 5 Forces, SWOT, BCG Matrix, 5 Whys, Fishbone, Business Model Canvas, WBS/RACI, NPV/IRR, Lean/Six Sigma 등 — 50+ 프레임워크）의 프로그래매틱 조직화
- **왜 평가하는가**: 흩어진 컨설팅 프레임워크를 **구조화, 인용 가능, 조합 가능한 라이브러리**로 변환 — 또 다른 PPT 컬렉션이 아님
- **어디서 쓰는가**: [`../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) — 7 카테고리 + 프레임워크 선택자 + 8 단계 매핑으로 적응
- **완전 인용**: [`CONSULTANT_FRAMEWORKS_REFERENCE.md`](CONSULTANT_FRAMEWORKS_REFERENCE.md)

#### 🎯 [`Kafurtan/mckinsey-consultant-skills`](https://github.com/Kafurtan/mckinsey-consultant-skills)（MIT）

- **무엇인가**: McKinsey 같은 톱 컨설턴트의 「**문제 → 리포트 / Deck**」 생산 공예를 실행 가능한 8 단계 워크플로로 변환
- **왜 평가하는가**: 「Dummy Page → Dependency Management → 7 Page Layouts → Progressive Disclosure → Troubleshooting」 전체 셋을 처음 가르칠 수 있는 SOP 로 기록 — 「시니어 컨설턴트만 가진 암묵적 공예」 대신
- **어디서 쓰는가**: [`../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) — 8 단계 컨설팅 리포트 워크플로 + §9 Troubleshooting Playbook 으로 적응
- **완전 인용**: [`MCKINSEY_SKILLS_REFERENCE.md`](MCKINSEY_SKILLS_REFERENCE.md)

#### 🎯 **Mirza Iqbal（[next8n.com](https://next8n.com)） — Workflow Delivery Framework**（MIT）

- **무엇인가**: n8n 딜리버리 컨설팅의 **운영 SOP** — 완전한 Discovery → Sprint → Handover 생애주기, 가격 그리드, 고객 커뮤니케이션 템플릿
- **왜 평가하는가**: **딜리버리 작업의 운영 SOP**（기술 SOP 만이 아니라）를 오픈소스화한 몇 안 되는 하나 — 컨설팅 업계가 거의 말하지 않는 운영 측면을 채움
- **어디서 쓰는가**: [`../06_Delivery/`](../06_Delivery/) — Engagement Lifecycle, Role SOPs, Business Document Templates 모두 이로부터 영감
- **완전 인용**: [`WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md`](WORKFLOW_DELIVERY_FRAMEWORK_REFERENCE.md)
- **입수 경로**: <https://github.com/MorrisLu-Taipei/AI-Workflow-Delivery-Framework>（README 가 Mirza Iqbal 을 오리지널 저자로 기재）

### 2.3 Agent & Skill (02_Course_Design 에 영향)

#### 🎯 [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents)（MIT）

- **무엇인가**: 12 부서 Agent 페르소나 라이브러리（Marketing, Sales, Customer Service, HR, Finance, R&D 등） — 즉시 사용 가능
- **왜 평가하는가**: 「Agent 페르소나 설계」를 재사용 가능한 라이브러리로 만들어, 팀이 System Prompt 를 처음부터 쓰는 수고를 덜어줌
- **어디서 쓰는가**: [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) §7.6 「기존 Agent 라이브러리 사용」 모듈
- **완전 인용**: [`AGENCY_AGENTS_REFERENCE.md`](AGENCY_AGENTS_REFERENCE.md)

#### 🎯 [`MorrisLu-Taipei/TigerAI-n8n-Skill-Pack`](https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack)（혼합 라이선스）

- **무엇인가**: n8n Skill 3 층 구조（Workflow Library + Cookbook + DSL Spec）, AI 생성 Workflow Skill Pack 포함
- **왜 여기 있는가**: 이는 방법론 저자 Morris Lu 자신의 프로젝트이지만, **인용 규율을 시연**하기 위해 여기 기재 — 자신의 프로젝트도 라이선스와 제3자 소스（`_vendor/` MIT）가 같은 기준으로 문서화됨
- **어디서 쓰는가**: [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) 후반부
- **완전 인용**: [`N8N_SKILL_PACK_REFERENCE.md`](N8N_SKILL_PACK_REFERENCE.md)

### 2.4 Case-Index (04_Scenarios 에 영향)

#### 🎯 [`Shubhamsaboo/awesome-llm-apps`](https://github.com/Shubhamsaboo/awesome-llm-apps)（Apache-2.0）

- **무엇인가**: 150+ 실 LLM 애플리케이션 케이스（Agent / RAG / Fine-Tuning / Multimodal 등）의 큐레이션 리스트, 커뮤니티 유지보수
- **왜 평가하는가**: 높은 큐레이션 품질, 명확한 분류, 지속적 업데이트; 컨설턴트가 고객에게 「**다른 회사는 이 시나리오에서 이렇게 한다**」 말할 때 가장 빠른 레퍼런스
- **어디서 쓰는가**: [`../04_Scenarios/`](../04_Scenarios/) LLM Apps Case Index — Dual-Axis Index（L1-L5 × 기업 부서）에 매핑; **매핑은 우리 것**, 오리지널 케이스 리스트는 Shubham Saboo 와 커뮤니티 기여자의 저작권
- **완전 인용**: [`AWESOME_LLM_APPS_REFERENCE.md`](AWESOME_LLM_APPS_REFERENCE.md)

#### 🎯 [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub)（MIT）

- **무엇인가**: 93+ AI 엔지니어링 교육 프로젝트（RAG 부터 Multi-Agent 까지 실행 가능 구현）
- **왜 평가하는가**: 각 프로젝트에 **코드 + 교육 영상** 부속, 학습자는 바로 시작 가능; awesome-llm-apps 의 「큐레이션 케이스」를 「핸즈온 구현」 측면에서 보완
- **어디서 쓰는가**: [`../04_Scenarios/`](../04_Scenarios/) LLM Apps Case Index 제2 소스 — L2-L4 코스 실행 가능 데모에 매핑
- **완전 인용**: [`AI_ENGINEERING_HUB_REFERENCE.md`](AI_ENGINEERING_HUB_REFERENCE.md)

---

## 3. 오리지널 참고 자료 & 다이어그램 (자체 제작 또는 Public Domain)

| 파일 | 목적 |
| --- | --- |
| [`@AI-MD-PUBIC.pdf`](@AI-MD-PUBIC.pdf) | AI Transformation Maturity Model 퍼블릭 버전 매뉴얼（오리지널 PDF 방법론 초안） |
| [`MD-Map.png`](MD-Map.png) | AI Maturity Map, 루트 README 에서 사용 |
| [`Metholodgy.png`](Metholodgy.png) | Enterprise Consulting Eight-Stage Transformation Guide, 루트 README 에서 사용 |

## 4. 학술 기반 & Failure Patterns (완전 오리지널, Tiger AI + 3 AI 엔진이 집필)

| 파일 | 목적 |
| --- | --- |
| [`FAILURE_PATTERNS.md`](FAILURE_PATTERNS.md) | 14 Failure Patterns（이론 예측 + 실 케이스 + 대응 수정） |
| [`AI_GOVERNANCE_ALIGNMENT.md`](AI_GOVERNANCE_ALIGNMENT.md) | NIST AI RMF / EU AI Act / ISO 42001 과의 얼라인먼트 |
| [`PILOT_STUDY_PROTOCOL.md`](PILOT_STUDY_PROTOCOL.md) | 18-24 개월 실증 연구 설계（Pilot Study） |

학술 이론 자체（7 기둥）는 [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md).

## 5. 영상 학습 노트 (파생 노트; 오리지널 영상 저작권은 제작자 귀속)

| 파일 | 목적 |
| --- | --- |
| [`OPENWEBUI_VIDEO_LEARNING_NOTES.md`](OPENWEBUI_VIDEO_LEARNING_NOTES.md) | OpenWebUI 공식 플레이리스트 학습 노트, L1 코스 적용에 매핑 |
| [`TIGERAI_VIDEO_LEARNING_NOTES.md`](TIGERAI_VIDEO_LEARNING_NOTES.md) | TigerAI 채널 학습 노트, n8n / L3 코스 적용에 집중 |

---

## 6. 인용 규율 (미래 기여자를 위한 철칙)

본 repo 에서 제3자 자료를 인용하려면 **모두 다음 「Approach A」 원칙을 따름**:

| # | 원칙 | 어떻게 |
|---|---|---|
| 1 | **독립 적응 — 포크 안 함, 소스 코드 재현 안 함** | 구조와 컨셉 참조, 본 방법론의 목소리로 다시 씀 |
| 2 | **명시적 귀속, 이중 기재** | (a) 인용 파일의 헤더 노트; (b) 본 디렉토리의 독립 `*_REFERENCE.md` |
| 3 | **방법론 시나리오로 일반화** | 영역 고유 내용을 L1-L5 AI 트랜스포메이션 컨설팅 컨텍스트로 변환 |
| 4 | **라이선스 없음 = 통합 없음** | LICENSE 없는 제3자 프로젝트는 통합 안 함（외부 예시 URL 로만 인용） |
| 5 | **관대한 평가** | 인용 파일에서 **무엇이 좋은지 명시**, 「아래 출처 참조」만 아님 |
| 6 | **실패에 정직** | 인용 도구가 부적합 판명되면, `FAILURE_PATTERNS.md` 에 정직히 기록 — 성공담만 아님 |

**사용 로직**: 「디렉토리 Y 의 파일 X 가 무엇을 인용했는가」를 찾기 → 그 파일 헤더 읽기 → 본 디렉토리의 대응 `*_REFERENCE.md` 로 점프하여 완전 라이선스 노트 참조.

---

## 7. 크로스 디렉토리 매핑

| 디렉토리 | 본 디렉토리와의 관계 |
| --- | --- |
| [`../00_Overview/`](../00_Overview/) | 방법론 다이어그램（Metholodgy.png / MD-Map.png）이 여기서 옴; 7 이론 기둥 논의는 `00` 에 거주 |
| [`../02_Course_Design/`](../02_Course_Design/) | L1/L2/L3/L5 코스의 제3자 인용（OpenWebUI 노트, agency-agents, n8n-Skill-Pack, ClawTeam） |
| [`../03_Consulting_Report/`](../03_Consulting_Report/) | 프레임워크 라이브러리와 리포트 워크플로의 제3자 인용（consultant, mckinsey-skills） |
| [`../04_Scenarios/`](../04_Scenarios/) | LLM 애플리케이션 Case Index 의 제3자 인용（awesome-llm-apps, ai-engineering-hub） |
| [`../06_Delivery/`](../06_Delivery/) | 딜리버리 운영 층의 제3자 인용（Mirza Iqbal 프레임워크） |
| [`../07_AI_Contributions/`](../07_AI_Contributions/) | 3 AI 엔진 자체도 「감사 대상」 — Antigravity / Codex CLI / Claude Code |

---

## 8. 일반적인 사용 시나리오

- **어떤 파일이 왜 그렇게 쓰였는지 궁금**: 파일 헤더 읽기 → 본 디렉토리의 `*_REFERENCE.md` 로 매핑
- **본 방법론 재배포 / 상용화**: §6 인용 규율 + [`NOTICE`](../NOTICE) 귀속 요건 읽기
- **새 오픈소스 프로젝트 온보드** → §6 의 6 원칙 따르기: 라이선스 확인 → 독립 적응 → `*_REFERENCE.md` 생성 → 본 README §2 감사에 추가
- **상류 커뮤니티 참여, 인터랙트 / 평가**: 각 Appreciation Card 의 GitHub URL 클릭하여 Star, Follow, Issue 개설, PR 송부
- **학습자가 repo 내용을 자신의 페이퍼 / Deck 에서 인용**: §6 에 따라, 본 방법론 인용 시 오리지널 저자 귀속 유지（[`../NOTICE`](../NOTICE)）; 제3자 자료 인용 시 대응 `*_REFERENCE.md` 의 학습자 인용 형식 따르기

---

## 9. 감사

본 디렉토리에 기재된 모든 상류 저자와 커뮤니티는 **본 방법론이 서는 어깨**. 오해, 부적절한 인용, 오리지널 목표로부터의 이탈은 어떤 것이든 방법론 저자 **Tiger AI Morris Lu 盧業興** 의 단독 책임 — 상류 저자나 커뮤니티가 아님.

당신이 상류 저자이고 본 repo 의 인용이 부적절, 수정 필요, 강화되어야 한다고 느끼면 — Issue 를 열거나 Morris Lu 에게 연락해 주세요, 즉시 처리하겠습니다.

> **아키텍처 소유권**: 본 repo 의 방법론 아키텍처는 인간 저자 **Morris Lu（Tiger AI）** 가 제안. 3 AI 엔진（Antigravity / Codex / Claude Code）은 **실행, 보완, 확장, 감사**하는 도구. [`../07_AI_Contributions/README.md`](../07_AI_Contributions/README.md) §0 참조.
