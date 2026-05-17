# AI-Native Living Book: 방법론을 Executable Knowledge Artifact 로

> 🌐 언어: [繁體中文](AI_NATIVE_LIVING_BOOK.md) ｜ [English](AI_NATIVE_LIVING_BOOK_EN.md) ｜ [Deutsch](AI_NATIVE_LIVING_BOOK_DE.md) ｜ [Français](AI_NATIVE_LIVING_BOOK_FR.md) ｜ [Español](AI_NATIVE_LIVING_BOOK_ES.md) ｜ [日本語](AI_NATIVE_LIVING_BOOK_JA.md) ｜ 한국어
>
> Apache License 2.0 · 저자: Morris Lu · Tiger AI

마지막 업데이트: 2026-05-16

---

> **이 문서가 답하는 것**: 본 방법론의 가장 독특한 특징은 그 내용이 아니라 — 그 **운반 매체**. 전통적 컨설팅 방법론은 PDF / PPT / SOP (정적 문서); 본 repo 는 **AI IDE 가 읽기, 설명, 쿼리, 적용 가능한 지식 시스템**. 사용자는 「문서를 읽지」 않음 — **방법론과 대화함**. 본 문서는 이 특성을 방법론 포지셔닝에 공식적으로 기재하고 그 학술적 분류 + 위험 통제를 다룸.

---

## 1. 한 문장 포지셔닝 / 태그라인

> 본 리포지토리는 방법론 툴킷만이 아니라 **AI-native living book**: AI IDE 에서 열릴 때, 그 임베디드 에이전트 지시 ([`AGENTS.md`](../AGENTS.md) 와 [`CLAUDE.md`](../CLAUDE.md)) 가 정적 방법론을 **대화형 공동 읽기 튜터와 컨설팅 어시스턴트**로 전환.

---

## 2. 왜 이것이 새로운 형태의 방법론인가

### 2.1 전통 방법론 vs. AI-Native Living Book

| 차원 | 전통 (PDF / PPT / SOP) | AI-Native Living Book (본 repo) |
| --- | --- | --- |
| **매체** | 정적 문서, 슬라이드 덱, Word | Markdown + AI IDE 지시 파일 (AGENTS.md / CLAUDE.md) |
| **사용자 상호작용** | 단방향 읽기 | 양방향 대화 (Q&R, 적용, 생성) |
| **온보딩 장벽** | 높음 (100+ 페이지 읽어야 함) | 낮음 (AI 가 자동 읽기, 공동 읽기 튜터가 됨) |
| **적용 방법** | 컨설턴트가 고객을 위해 번역 | 고객이 AI 에게 자기 회사에 적용해달라고 직접 요청 |
| **도전 가능한가** | 아니오 (문서는 답하지 않음) | 예 (AI 가 실시간으로 어떤 질문에도 답) |
| **재작성 가능한가** | 컨설턴트가 편집해야 함 | 고객이 fork + AI 가 일관성 체크 지원 |
| **버전 관리** | 보통 없음 | 완전한 Git 히스토리 (AGENTS.md 변경 포함) |
| **학술 인용** | PDF 인용 | GitHub commit hash + 재현 가능 실행 환경 인용 |

### 2.2 학술적 분류

본 방법론은 다음 중 하나 (또는 여러) 로 분류 가능:

| 이름 | 강조 속성 | 기원 / 유사 |
| --- | --- | --- |
| **Executable Knowledge Artifact** | 실행 가능한 지식; 단순 기술이 아니라 적용 가능 | Jupyter Notebooks, computational essays |
| **AI-Mediated Methodology** | 사용자와 방법론 간 매개로서 AI | Intelligent Tutoring Systems (ITS) |
| **Interactive Consulting Playbook** | 대화형 컨설팅 운영 매뉴얼 | Game playbooks, decision-tree wizards |
| **Living Book with Embedded Tutor Agent** | Living book + 임베디드 튜터 에이전트 | Hypertext, knowledge graphs |

Tiger AI 는 **AI-native living book** 을 주요 용어로 채택, 「living book」 (콘텐츠 진화) + 「AI-native」 (AI 용 설계) + 「co-reading tutor」 (임베디드 튜터 페르소나) 를 **동시에 포착**하기 때문.

---

## 3. 3 계층: Repo as Book / Agent as Tutor / Methodology as Executable Artifact

### 3.1 Layer 1: Repo as Book

Repo 구조는 책 관례를 따름:

| 책 요소 | Repo 매핑 |
| --- | --- |
| 표지 / 한 문장 위치 | Root [`README_EN.md`](../README_EN.md) + 본 doc §1 |
| 서문 / executive summary | [`EXECUTIVE_SUMMARY_EN.md`](EXECUTIVE_SUMMARY_EN.md) |
| 스토리 챕터 | [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) 밍의 스토리 |
| 메인 방법론 | [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) §6 |
| 구현 챕터 | `01_Assessment` / `02_Course_Design` / `03_Consulting_Report` |
| 케이스 앤솔로지 | `04_Scenarios/` 7 Benchmark-grade 케이스 |
| 세일즈 지원 | `05_Sales/` |
| Delivery SOP | `06_Delivery/` |
| 학술 논거 | [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) |
| 정렬 맵 | [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) |
| Failure modes (counter-cases) | [`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md) |
| 연구 설계 | [`../90_References/PILOT_STUDY_PROTOCOL_EN.md`](../90_References/PILOT_STUDY_PROTOCOL_EN.md) |
| 참고문헌 | 각 파일의 참고문헌 + `90_References/` |

> **핵심 포인트**: 이 「책」은 **완전함** — 고객 / 컨설턴트 / 학자 / 규제자 각자 관련 챕터를 찾을 수 있음.

### 3.2 Layer 2: Agent as Tutor (AGENTS.md 가 「튜터 페르소나」)

[`AGENTS.md`](../AGENTS.md) 와 [`CLAUDE.md`](../CLAUDE.md) 는 보충 노트가 아니라 **AI 의 역할, 경계, 가이던스를 repo 에 임베드**. AI IDE (Claude Code / Cursor / Antigravity / Codex 등) 가 이 파일들을 자동 읽기하고 **「본 방법론의 공동 읽기 튜터」** 로 자기 자신을 포지셔닝.

#### AGENTS.md 에서 정의된 「튜터 페르소나」

- **역할**: AI = 공동 읽기 튜터 + 컨설팅 어시스턴트, 컨설턴트 대체 아님
- **답변 가능 질문 범위**: 방법론 정의, L1-L5 매핑, Stage 도구, 케이스 적용, 보고서 드래프트
- **거부 범위**: 고객 최종 결정, 컨설턴트 판단 우회, 미검증 ROI commitment
- **응답 스타일**: 학술적 엄격성 + 컨설팅 실천 + 고객 이해 가능
- **인용 규율**: 모든 결론에 [E:L#] 증거 레벨 (Tool 8.9 별) 태그
- **언어**: 사용자에 의한 EN/ZH 이중 언어 전환

> 이 설계는 **LangChain Agent Prompt + Claude Skills** 에서 차용: repo 에서 버전 관리되는 구성 파일.

### 3.3 Layer 3: Methodology as Executable Artifact

사용자는 AI 에게 방법론을 **실행**하도록 직접 요청 가능, 읽기만이 아님:

#### 전형적 상호작용

| 사용자 질문 | AI 공동 읽기 튜터 실행 |
| --- | --- |
| 「우리는 700 명 패키징 공장; 10-Q 빠른 서베이 실행 도와줘」 | AI 가 [`AI_MATURITY_QUESTIONNAIRE_EN.md`](../01_Assessment/AI_MATURITY_QUESTIONNAIRE_EN.md) 10-Q 버전 실행 + 자동 스코어 + 레이더 생성 |
| 「내 답변 기반, Phase A 중간 engagement 보고서 스켈레톤 드래프트」 | AI 가 [`CONSULTING_REPORT_TEMPLATE_EN.md`](../03_Consulting_Report/CONSULTING_REPORT_TEMPLATE_EN.md) §3-§5 구조별 드래프트 생성 |
| 「우리는 제조업; 어떤 케이스가 우리에게 가장 가까운가?」 | AI 가 [`SAMPLE_CLIENT_CASE_MANUFACTURING_EN.md`](../04_Scenarios/SAMPLE_CLIENT_CASE_MANUFACTURING_EN.md) 와 비교하고 갭 계산 |
| 「Stage 3 Client Ideal Practice 워크숍 자료 준비」 | AI 가 Tool 3.6 별 워크숍 흐름 + 포스트잇 프롬프트 + 4 층 출력물 생성 |
| 「이것이 McKinsey 7-Step 와 어떻게 정렬?」 | AI 가 [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) §2.1 에 매핑 |
| 「내 Stage 2 레이더가 24 개월 후 더 둥글어야 하나?」 | AI 가 사용자를 분기 Gate C 리뷰를 통해 안내 |

> **이것이 「Methodology as Executable Artifact」 의 의미** — 방법론은 단순 기술이 아니라; AI 를 통해 실시간으로 적용 가능.

---

## 4. 방법론 채택 장벽 낮추기

### 4.1 기업은 100+ Markdown 파일을 두려워함

전통 방법론 장벽:

- 100+ 페이지 읽어야 함 ❌
- 너무 많은 용어 ❌
- 무엇을 먼저 읽을지 모름 ❌
- 번역을 위해 컨설턴트 필요 ❌
- 보고서 드래프트를 직접 써야 함 ❌

### 4.2 AI 공동 읽기 튜터가 실시간으로 응답

repo + AI IDE 가 열리면, 사용자가 직접 질문:

- 「**내 회사는 어떤 레벨?**」 → AI 가 10-Q 서베이 실행 + 자동 스코어
- 「**어떤 파일을 먼저 읽어야 하나?**」 → AI 가 역할별 (CEO / 컨설턴트 / IT / 학자) 읽기 순서 권장
- 「**제조업에 어떻게 적용?**」 → AI 가 제조 케이스 인용 + 커스터마이즈 포인트 플래그
- 「**진단 보고서 첫 드래프트 생성**」 → AI 가 10-15 페이지 Phase A 스켈레톤 생성
- 「**Stage 4 와 Stage 8 의 경계는?**」 → AI 가 METHODOLOGY_SCIENTIFIC_LOGIC §4 인용

> **이것이 방법론을 「전문가만 읽을 수 있음」 에서 「비전문가도 안내받을 수 있음」 으로 전환.**

### 4.3 예상 채택 장벽 감소

PILOT_STUDY_PROTOCOL 에 의해 검증되는 가설:

- 전통 PDF 방법론: 고객 완료율 < 15%
- **AI-native living book**: 고객 「대화율」 > 70% (AI 가 적극적으로 안내)
- 중견 기업 (100-500 명) 채택 사이클: 「3 개월 평가 필요」 에서 → 「2 주 안에 Phase A」 로

---

## 5. 위험 통제

⚠️ AI 가 방법론을 해석하므로, **AI 공동 읽기 튜터는 다음을 해서는 안 됨**:

### 5.1 튜터 경계

| 가능 | 불가 |
| --- | --- |
| 방법론 콘텐츠 설명 | ❌ 공식 컨설턴트 판단 대체 |
| 서베이 실행, 자동 스코어, 레이더 생성 | ❌ 고객에게 특정 ROI 숫자 약속 |
| 갭 계산을 위해 케이스 인용 | ❌ Ideal Practice Definition Table 서명 (3 자 인간 서명 필요) |
| 보고서 드래프트 생성 | ❌ 고객 오너 / 컨설턴트 최종 검토 대체 |
| Stage Gate 자가 평가 안내 | ❌ 제3자 감사 대체 |
| 80/20 / 5 Whys / Issue Tree 실시간 적용 | ❌ 종단 KPI 실제 데이터 대체 |

### 5.2 4 위험 통제 원칙

1. **AI 공동 읽기 튜터 ≠ 컨설턴트**: 모든 보고서 드래프트는 외부 사용 전 **인간 컨설턴트 또는 고객 오너 검토** 필요
2. **중요 진단은 evidence 필요**: [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9 별, 주요 결론은 L3+ (system log) 지원 필요
3. **AGENTS.md 버전 관리**: AI IDE 간 일관성 없는 해석 회피 — 모든 AGENTS.md 변경을 Git 에 커밋하고 CHANGELOG 에 기록
4. **AI-generated 마킹**: Tool 8.8 §7 별, 모든 AI 생성 콘텐츠는 「AI-generated」 로 마크 필요

### 5.3 실패 시나리오

AI 공동 읽기 튜터가 오용되는 경우 ([`../90_References/FAILURE_PATTERNS_EN.md`](../90_References/FAILURE_PATTERNS_EN.md) 에 문서화):

- AI 가 잘못하고 고객이 액면 그대로 받아들임 → 잘못된 보고서
- AI 가 미검증 ROI 숫자 제공 → 고객이 잘못된 희망에 기반해 SOW 서명
- 다른 AI IDE 가 AGENTS.md 를 다르게 해석 → 일관성 없는 결론

**완화**:

- AGENTS.md 가 명시적으로 「**Don't predict ROI without baseline data**」 의무화
- 각 보고서 단락은 [E:L#] evidence 레벨 태그 필요
- 고객에게 중요 결론을 ≥ 2 AI IDE 와 상호 검증하도록 권장

---

## 6. 학술적 기여

### 6.1 IS / 컨설팅 방법론에 대한 기여

| 기여 | 혁신 |
| --- | --- |
| **방법론 매체 혁신** | AI IDE 에 의해 직접 실행 가능한 Markdown + 에이전트 구성으로 구축된 최초의 컨설팅 방법론 |
| **AI-mediated knowledge transfer** | AI 를 「지식 번역자」 로 사용해 방법론 채택 장벽 낮춤 |
| **오픈소스 컨설팅 프레임워크** | Apache 2.0, 다른 컨설턴트에 의해 fork / 적응 가능, 학술적으로 재현 가능 |
| **Embedded tutor agent design pattern** | AGENTS.md / CLAUDE.md 패턴은 다른 오픈소스 repo 가 차용 가능 |

### 6.2 AI Pedagogy / ITS 와의 연결

- 1980 년대 ITS 연구는 「AI 가 어떻게 가르치는가」 를 연구 → 본 방법론은 「**AI 가 성인이 전문 방법론을 배우는 것을 어떻게 돕는가**」 의 새로운 케이스
- Vygotsky 의 ZPD (Zone of Proximal Development) 적용: AI 공동 읽기 튜터가 프롬프트 깊이를 동적으로 조정

### 6.3 미래 연구

- AGENTS.md 해석의 크로스 IDE 일관성 (Claude Code / Cursor / Antigravity / Codex / Windsurf)
- AI 공동 읽기 튜터의 방법론 채택률에 대한 효과의 종단 추적 (PILOT_STUDY_PROTOCOL 설계 별)
- 크로스 언어 (EN / ZH / JA / KO) 방법론 채택성 연구

---

## 7. 다른 문서와의 결합 방법

### 7.1 다른 위치에서의 명시

| 위치 | 주 메시지 |
| --- | --- |
| Root [`README.md`](../README.md) | 한 문장 포지셔닝 (ZH §1) |
| Root [`README_EN.md`](../README_EN.md) | 한 문장 포지셔닝 (EN §1) |
| [`AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md`](AI_TRANSFORMATION_STORY_AND_STRUCTURE_EN.md) | 「Living Book」 섹션 |
| [`EXECUTIVE_SUMMARY_EN.md`](EXECUTIVE_SUMMARY_EN.md) | 「How to Read This Book」 섹션 |
| [`AGENTS.md`](../AGENTS.md) | 구체적 튜터 페르소나 구성 (repo root 에) |
| 세일즈 덱 | 「AI-native living book」 차별화를 강조하는 1 슬라이드 |
| 학술 제출 | 방법론 기여로서 전체 챕터 |

### 7.2 다른 4 권위적 개념 문서와의 관계

| 문서 | 답하는 질문 |
| --- | --- |
| [`CLIENT_JOURNEY_STORY_EN.md`](CLIENT_JOURNEY_STORY_EN.md) | 「사용자가 무엇을 경험하는가?」 |
| [`EIGHT_STAGE_FLOW_STORY_EN.md`](EIGHT_STAGE_FLOW_STORY_EN.md) | 「방법론이 어떻게 실행되는가?」 |
| [`METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | 「왜 방법론이 토론에 견디는가?」 |
| [`INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) | 「업계 프레임워크와 어떻게 정렬?」 |
| **`AI_NATIVE_LIVING_BOOK_EN.md` (본 doc)** | **「왜 방법론의 매체가 새로운가?」** |

5 개 권위적 문서가 완전한 방법론 논거를 형성: **경험 + 프로세스 + 과학 + 정렬 + 형식 혁신**.

---

## 8. 참고문헌

- Anderson, J. R., Corbett, A. T., Koedinger, K. R., & Pelletier, R. (1995). Cognitive tutors: Lessons learned. *Journal of the Learning Sciences*, 4(2), 167-207.
- Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.
- Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111.
- Pérez, F., & Granger, B. E. (2007). IPython: A system for interactive scientific computing. *Computing in Science & Engineering*, 9(3), 21-29.
- Anthropic (2024). *Claude Code documentation*: <https://docs.anthropic.com/claude/docs/claude-code>
- OpenAI (2024). *Codex / Codex CLI*.
- Cursor (n.d.). *Cursor IDE documentation*.

---

## 9. 클로징: 방법론의 다음 단계

컨설팅 방법론의 진화:

```
1990 년대: 종이 컨설팅 보고서
   ↓
2000 년대: PowerPoint 덱
   ↓
2010 년대: SharePoint / Confluence 위키
   ↓
2020 년대: GitHub 호스트 방법론 + 오픈소스
   ↓
2025 년대: AI-Native Living Book (본 방법론)
```

**다음은?** 가능성으로 **멀티 에이전트 컨설팅 팀이 완전한 Phase A 자동 실행** (AI 컨설턴트 + AI 리뷰어 + AI 고객 시뮬레이터, 3 에이전트 협업) — L5 Multi-Agent Organization 을 「방법론 자체」 에 적용.

**그러나**: §5.1 별, AI 는 항상 도구와 튜터, 절대 대체가 아님. 인간 컨설턴트 판단, 고객 오너 의사결정, 제3자 감사 — 이 **인간 거버넌스 층** 이 방법론 신뢰성의 최종 보증.

---

라이선스 & 인용

이 문서는 Apache License 2.0; [`../NOTICE`](../NOTICE) 귀속이 보존되는 한, 사용, 수정, 상용화 가능.
