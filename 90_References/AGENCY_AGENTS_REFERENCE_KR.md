# agency-agents 인용 & 라이선스 통지

> 🌐 언어: [繁體中文](AGENCY_AGENTS_REFERENCE.md) ｜ [English](AGENCY_AGENTS_REFERENCE_EN.md) ｜ [Deutsch](AGENCY_AGENTS_REFERENCE_DE.md) ｜ [Français](AGENCY_AGENTS_REFERENCE_FR.md) ｜ [Español](AGENCY_AGENTS_REFERENCE_ES.md) ｜ [日本語](AGENCY_AGENTS_REFERENCE_JA.md) ｜ 한국어

본 방법론의 **L2 Knowledge Codification** 코스 후반 (구체적으로 L2-B Agentic Developer 트랙) 은 「기성 Agent 페르소나 라이브러리」 모듈의 교재로 **agency-agents** 를 인용. 본 문서는 상류 소스, 라이선스 조건, 인용 가이드, 사용 범위를 기록.

---

## 1. 상류 프로젝트

| 필드 | 값 |
| --- | --- |
| **프로젝트** | agency-agents |
| **메인테이너** | @msitarzewski (커뮤니티 메인테넌스) |
| **GitHub URL** | <https://github.com/msitarzewski/agency-agents> |
| **라이선스** | **MIT License** |
| **규모** | 12 부서에 걸친 144+ Agent 페르소나 |
| **지원 도구** | Claude Code, GitHub Copilot, Cursor, Aider, Windsurf, OpenCode, Antigravity, Gemini CLI, OpenClaw, Qwen Code, Kimi Code |

## 2. agency-agents 란

agency-agents 는 **AI Agent 페르소나 정의 컬렉션**: 각 Agent 는 ID 특성, 핵심 미션, 기술 사양, 워크플로 프로세스, 측정 가능한 성공 기준을 포함하는 markdown 파일. 일반적인 프롬프트 템플릿의 세트가 아니라, 「배포 가능한 가상 스페셜리스트」 의 로스터.

### 12 부서

`engineering` (25+ Agent: Frontend Developer, Backend Architect, Security Engineer…), `design`, `marketing`, `sales`, `product`, `project-management`, `testing`, `support`, `finance`, `game-development`, `academic`, `specialized`, `spatial-computing`.

### 설치

`./scripts/install.sh` 를 통해 설치, 설치된 AI 도구를 자동 감지하고 병렬 처리.

## 3. 왜 L2 에 속하는가

L2 Knowledge Codification 의 핵심은 「작업 경험을 재사용 가능한 Skills 로 패키징」. L2-B Agentic Developer 트랙 후반은 중요한 아이디어를 가르침: **모든 Skill 이 처음부터 구축될 필요는 없다**. agency-agents 는 출발점으로 144+ 성숙한 Agent 페르소나를 제공 — 학습자는 바퀴를 재발명하는 대신, 선택, 커스터마이즈하고 기업 Skill Library 에 통합.

대응 코스: [`../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](../02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md) §7.6.

## 4. 라이선스 요약

agency-agents 는 **MIT License** 로 출시. MIT 는 프로프라이어터리 제품의 일부로 포함하여 자유 사용, 수정, 재배포, 상업적 사용을 허용; **유일한 조건**은 재배포 시 오리지널 MIT 저작권 통지와 라이선스 텍스트를 보존해야 함. MIT 는 엔드 유저에 대한 가시적 귀속을 엄격히 요구하지 않음 (저자는 감사하다고 명시하지만).

> ⚠️ **중요**
> 본 repo 는 agency-agents 소스를 **재배포하지 않음**. L2 코스에서 그 구조와 사용법을 **인용 및 교육**만 하고, 학습자에게는 **상류에서 직접 설치**하도록 안내. 학습자가 커스터마이즈한 Agent 페르소나는 기업에 속하지만, Skill 문서에 오리지널 소스 (agency-agents + 버전) 를 기재할 것을 권장.

## 5. 인용 범위

| 범위 | 처리 |
| --- | --- |
| **교재로서** | L2-B 후반의 「기성 Agent 라이브러리」 케이스로 사용; 설치, 브라우즈, 선택, 커스터마이즈를 가르침 |
| **소스 / 페르소나 파일** | **재현하지 않음, 포크하지 않음**; 학습자는 `./scripts/install.sh` 를 통해 직접 설치 |
| **커스터마이즈된 출력** | 커스터마이즈된 페르소나는 기업 Skill Library 항목이 됨; 소스 귀속 권장 |

## 6. 학습자용 인용 형식

> agency-agents by @msitarzewski 기반 — <https://github.com/msitarzewski/agency-agents> (MIT License)

## 7. 면책 조항

본 방법론에서 agency-agents 의 기술, 적용, 커스터마이즈 가이드는 방법론 저자 (Morris Lu / Tiger AI 虎智科技) 의 해석을 나타내며, @msitarzewski 또는 agency-agents 커뮤니티의 공식 입장을 나타내지 않음. agency-agents 의 구조, 설치, Agent 분류가 새 버전에서 변경되면, [상류 리포지토리](https://github.com/msitarzewski/agency-agents) 를 참조.
