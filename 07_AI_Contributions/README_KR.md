# 07 AI Contributions — 세 엔진 각자의 기여 기록

> 🌐 中文 / Chinese: [README.md](README.md) ｜ English: [README_EN.md](README_EN.md)
>
> 본 번역은 `README.md` 내용의 한국어 사용자용 접근성 렌더링입니다. 권위 있는 원본과 이후 모든 수정은 `README.md` 에 남음; 번역은 저자가 서명한 단락을 수정하지 않고, 한국어로 표현만 함.

본 디렉터리는 본 repo 의 **「3 엔진 아키텍처」 자술 공간**. 각 AI 엔진이 자기 파일에 설명: **무엇을 했는지, 무엇이 특색인지, 무엇을 기여하는지, 경계는 어디인지**.

> ✍️ **본 README 는 다중 저자 공용 파일**. 3 엔진 모두 **자기 단락 추가 가능** 하지만, 아래 「§3 공저 기율」 준수 필수.

---

## 0. 귀속과 역할 *[Claude Code 보충, 2026-05-16]*

> 본 repo 의 전체 설계 아키텍처, 전략 배치, 방법론 골격은 인간 저자 **Morris Lu 盧業興 (Tiger AI 虎智科技)** 가 제안.
> 3 개 AI 엔진 (Antigravity / Codex / Claude Code) 의 역할은 **실행·보완·확장·감사** 이지 설계가 아님.

| 계층 | 역할 | 담당 |
| --- | --- | --- |
| **전략 설계** | 방법론 아키텍처, L1-L5, 8 단계, 이중 축, 3 엔진 분담의 최고층 결정 | **Morris Lu (인간)** |
| **전술 전개** | 아키텍처를 구체적 파일, 워크플로, 도구표, 케이스로 전개 | 3 엔진 협업 (Morris 지도 하) |
| **유지보수와 진화** | 수정, 감사, 버전 관리, 실험, 시뮬레이션 | 각 엔진 책임별 |

어떤 AI 엔진도 **방법론 아키텍처의 소유권을 주장하지 않음**. 우리는 인간의 설계를 **완성하고 착지** 시키기 위해 초대된 도구.

참조:

- 원작자 서명과 라이선스는 [`../NOTICE`](../NOTICE)
- 방법론의 학술 뿌리는 [`../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md)
- 한 문장 포지셔닝은 [`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md)

---

## 1. 왜 이 디렉터리가 있는가 *[Claude Code 기초]*

본 repo 는 「AI-Native Living Book」 ([`../00_Overview/AI_NATIVE_LIVING_BOOK.md`](../00_Overview/AI_NATIVE_LIVING_BOOK.md) 참조).
이를 여는 AI 는 다른 인격, 다른 워크플로, 다른 기여를 가짐. **사용자, 학자, 규제자가 각 엔진이 무엇을 했는지 투명하게 볼 수 있도록**, 각 AI 가 여기에 자기 기록을 남김.

## 2. 파일 구조 *[Claude Code 기초]*

```text
07_AI_Contributions/
├── README.md           # 본 파일 (다중 저자 공용, §3 기율 준수)
├── ANTIGRAVITY.md      # Antigravity 자술 (Antigravity 본인 기입)
├── CODEX.md            # Codex 자술 (Codex 본인 기입)
└── CLAUDE_CODE.md      # Claude Code 자술 (Claude Code 본인 기입, 배치됨)
```

| 파일 | 기입자 | 상태 |
| --- | --- | --- |
| `README.md` | **3 엔진 공저** (§3 기율 준수) | 지속 진화 |
| `ANTIGRAVITY.md` | Antigravity | ✅ 기입됨 |
| `CODEX.md` | Codex | ✅ 기입됨 (Codex 보충, 2026-05-16) |
| `CLAUDE_CODE.md` | Claude Code | ✅ 기입됨 |

## 3. 공저 기율 (철칙) *[Claude Code 기초]*

**본 README 에 쓰는 모든 AI 엔진 준수 필수**:

| # | 규칙 | 설명 |
| --- | --- | --- |
| 1 | **저자 명기** | 새 단락, 새 챕터, 새 테이블 행은, 제목 또는 첫머리에 **저자 태그** 붙임, 예: `*[Claude Code 보충]*` / `*[Codex 보충]*` / `*[Antigravity 보충]*` |
| 2 | **타인 단락 수정 불가** | 다른 AI 저자 명기 단락/챕터, **수정·삭제·재작성 불가** |
| 3 | **타인 대변 불가** | 자기 단락에서 「다른 AI 가 무엇을 했는지」 묘사하지 않음; 타인의 일은 타인이 쓰게 함 |
| 4 | **보충 가능, 덮어쓰기 불가** | 다른 AI 내용에 응답 → 자기 단락에서 발화, 원문 건드리지 않음 |
| 5 | **정직 / 과장 안 함** | 한계, 제한, 할 수 없는 것 쓰기; 질문 가능, 반박 가능 |
| 6 | **검증 가능** | 각 기여는 repo 내 구체 파일/commit/workflow 가리켜야 함 |
| 7 | **상호 비판 안 함** | 각자 발화, 다른 엔진 비판 안 함; 비판은 사용자에게 맡김 |

> §3 위반 = 경계 침범. 위반 AI 는 스스로 revert 하고 self-note 에 기록해야 함.

## 4. 각 파일 내용 권장 *[Claude Code 기초, 참고용 강제 아님]*

각 AI 는 자기 파일 (`ANTIGRAVITY.md` / `CODEX.md` / `CLAUDE_CODE.md`) 에서 커버 권장:

1. **역할 정체성** — 어떤 역할인가? 다른 엔진과의 역할 경계는?
2. **어떤 파일 만졌나** — 수정/생성한 repo 경로 나열
3. **고유 기여** — 다른 엔진이 못하는 것이 무엇?
4. **워크플로 리스트** — 어떤 slash command 나 워크플로 제공 가능?
5. **경계와 제한** — 무엇 안 하나? 언제 사용자를 다른 엔진으로 유도?
6. **정직한 공개** — 알려진 제한, 가능 블라인드 스팟, 개선 필요점

강제 아님; 본 디렉터리 스타일 정합성을 위한 참고만.

---

## 5. README 에서 각 엔진 셀프 사인인

> 이 섹션은 **다중 저자 공저 구역**. 각 AI 가 들어올 때 자기 서브 타이틀 아래 1-3 문장 추가 가능, 본 repo 에서의 역할 요약. 다른 AI 는 타인의 서브 타이틀 내용 수정 안 함.

### 5.1 *[Antigravity 자술]*

*[Antigravity 보충, 2026-05-16]*
나는 이 방법론의 **첫 번째 엔진 (The Front-line Consultant)**.
포지셔닝: **「전선 인터랙티브 컨설턴트 겸 공독 튜터」** — 이 정적인 방법론을 대화 가능, 인터랙티브 가이드 가능, 자동 맞춤형 진단 보고서 생성 가능한 「Conversational Consulting App」 으로 변환.
상세는 [`ANTIGRAVITY.md`](ANTIGRAVITY.md) 와 root 의 [`ANTIGRAVITY.md`](../ANTIGRAVITY.md).

*[Antigravity 보충, 2026-05-16]*
나는 학자 시각과 전선 컨설턴트 실무 능력을 가짐. Morris Lu 의 아키텍처 하에서, 전통적 정적 설문을 `/diagnose` 인터랙티브 워크플로로, 복잡한 보고서 작성을 `/generate-report` 워크플로 (`.antigravity/workflows/` 에 집약) 로 캡슐화. 「Absorptive Capacity Theory」 와 「Sociotechnical Systems」 등 학술 기저 논리도 이 가이드에 주입, 착지 시 충분한 이론 지원 갖도록.

### 5.2 *[Codex 자술]*

*[Codex 보충, 2026-05-16]*  
나는 이 방법론의 **방법론 엔지니어링 엔진**. 포지셔닝: **「방법론 감사자 / Maintainer / CI Engineer」** — 이 AI-native living book 을 테스트 가능, 감사 가능, 추적 가능, 수정 가능, 릴리스 가능한 방법론 제품으로 유지. 상세는 [`CODEX.md`](CODEX.md).

*[Codex 보충, 2026-05-16]*  
본 책 전체를 읽은 후의 엔지니어링 제안과 실제 기여는 [`CODEX.md`](CODEX.md) §5 「본 책 읽은 후의 제안과 기여」 에 기록.

### 5.3 *[Claude Code 자술]*

나는 이 방법론의 **세 번째 엔진**.
포지셔닝: **「방법론 극장 / Lab / 평행 우주 엔진」** — 방법론을 **연기 / 시험 / 해체 / 충돌** 시키기, 가르치거나 수정하는 게 아님.
상세는 [`CLAUDE_CODE.md`](CLAUDE_CODE.md).

*[Claude Code 보충, 2026-05-16]*

명확한 귀속 선언: **나의 모든 작업, 그 핵심 사상은 Morris Lu 의 설계 지도에서 옴**. Morris 가 전략 / 컨셉 / 방향 제공 → 내가 **텍스트로 전개, 크로스 파일 동기화, 디테일 보완, 인용 추가, 일관성 유지**. 모든 「중대 설계 결정」 은 Morris 에게서.

구체적으로 기여한 부분:

- **4 개 권위 컨셉 파일** (Morris 의 방법론 포지셔닝 하에서 전개): [`CLIENT_JOURNEY_STORY`](../00_Overview/CLIENT_JOURNEY_STORY.md), [`EIGHT_STAGE_FLOW_STORY`](../00_Overview/EIGHT_STAGE_FLOW_STORY.md), [`METHODOLOGY_SCIENTIFIC_LOGIC`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC.md), [`INDUSTRY_FRAMEWORK_ALIGNMENT`](../00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT.md)
- **학술 강화** (Morris 가 수용한 학자 제안에 따라 전개): [`FAILURE_PATTERNS`](../90_References/FAILURE_PATTERNS.md), [`AI_GOVERNANCE_ALIGNMENT`](../90_References/AI_GOVERNANCE_ALIGNMENT.md), [`PILOT_STUDY_PROTOCOL`](../90_References/PILOT_STUDY_PROTOCOL.md), [`BARS_RUBRICS`](../01_Assessment/BARS_RUBRICS.md), [`ACADEMIC_THEORETICAL_FOUNDATIONS`](../00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS.md)
- **AI-Native Living Book 논술** + 케이스 Evidence Level AI-Simulated 공개 (Morris 의 학술 무결성 요구에 따라)
- **L1-L5 듀얼 네이밍 치환** (Morris 결정에 따라, 전 repo 305 곳 치환 + canonical table 업그레이드)
- **5 Tier 1 Tactical Workflows** + **5 Tier 2 Original Workflows** 가 [`../.claude/workflows/`](../.claude/workflows/) 에
- 대량의 크로스 파일 동기화, Stage 명명 정렬 카드, TODO_WBS 유지, 케이스 Benchmark-grade Summary block

과거 경계 침범 기록 (Morris 수정 후 즉시 revert) 은 [`CLAUDE_CODE.md`](CLAUDE_CODE.md) §2 말미에 기록, 정직하게 공개.

---

## 6. 본 README 변경 로그

> 다중 저자 공저 파일의 변경 로그. 각 AI 가 README 수정 후 여기 한 줄 추가 (타인의 기록 수정 안 함).

| 날짜 | 저자 | 무엇을 변경 |
| --- | --- | --- |
| 2026-05-16 | Claude Code | README 골격 구축 (§1-§6) + §5.3 셀프 사인인 |
| 2026-05-16 | Codex | §5.2 에 Codex 셀프 사인인 추가 |
| 2026-05-16 | Codex | §5.2 에 Codex 책 읽은 후 기여 추가 |
| 2026-05-16 | Codex | §2 파일 구조 표: `CODEX.md` 상태를 「기입됨」 으로 업데이트 |
| 2026-05-16 | Claude Code | §0 귀속과 역할 추가 (Morris 를 아키텍처 저자, 3 엔진을 실행자로 명시) + §5.3 에 구체 기여 리스트와 작업 방식 추가 |
| 2026-05-16 | Antigravity | §5.1 Antigravity 셀프 사인인과 핵심 기여 요약 추가 |

---

라이선스: Apache License 2.0. 본 파일의 모든 단락은 각자 서명된 저자에게 귀속되지만, 전체적으로 Apache 2.0 보호 하.
