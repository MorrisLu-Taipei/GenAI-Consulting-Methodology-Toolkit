# ClawTeam 인용 & 라이선스 통지

> 🌐 언어: [繁體中文](CLAWTEAM_REFERENCE.md) ｜ [English](CLAWTEAM_REFERENCE_EN.md) ｜ [Deutsch](CLAWTEAM_REFERENCE_DE.md) ｜ [Français](CLAWTEAM_REFERENCE_FR.md) ｜ [Español](CLAWTEAM_REFERENCE_ES.md) ｜ [日本語](CLAWTEAM_REFERENCE_JA.md) ｜ 한국어

본 방법론의 **L5 Multi-Agent Organization** 코스는 **ClawTeam** 을 구현 플랫폼으로 채택. 본 문서는 상류 소스, 라이선스 조건, 인용 가이드, 우리의 사용 범위를 기록.

---

## 1. 상류 프로젝트

| 필드 | 값 |
| --- | --- |
| **프로젝트** | ClawTeam |
| **태그라인** | The Evolution of AI Agents: Solo 🤖 → Swarm 🦞🤖🤖🤖 |
| **메인테이너** | HKUDS (HKU Data Science Lab / 香港大學資料科學實驗室) |
| **GitHub URL** | <https://github.com/HKUDS/ClawTeam> |
| **라이선스** | **MIT License** |
| **작성 시점 버전** | v0.2 — v0.3 (Stabilization → Multi-User + Web UI) |
| **언어** | Python 3.10+ |
| **의존성** | `tmux`, `git`, 임의의 CLI Agent (Claude Code / Codex / nanobot / OpenClaw 등) |

## 2. ClawTeam 이란

ClawTeam 은 **다중 에이전트 자가 조직화 팀용 CLI 프레임워크**: 인간이 하나의 고수준 목표를 발표하고, Agent Team 이 자율적으로 분해, 위임, 협력, 머지. SDK 가 아닌 CLI 명령 세트 + 공유 파일시스템 + git-worktree 격리 + 메시징 층 — **임의의 CLI Agent (Claude Code, Codex, Gemini, …) 가 그것에 의해 오케스트레이션 가능**.

### 핵심 아키텍처

| 층 | 콘텐츠 |
| --- | --- |
| **Team Management** | 워크스페이스 & 작업 큐를 공유하는 Agents 풀 |
| **Workspace Isolation** | 각 Agent 가 자신의 git worktree & 브랜치에서 실행 — 충돌 없음 |
| **Task Tracking** | 의존성 체인과 auto-unblocking 이 있는 Kanban 스타일 |
| **Inter-Agent Messaging** | 점대점 Inboxes + 브로드캐스트 |
| **Transport 층** | 기본 파일 기반; 선택적 P2P (ZeroMQ); Redis 는 로드맵 |
| **Storage** | 모두 JSON 으로 `~/.clawteam/` 에; 데이터베이스 없음, 중앙 서버 없음 |

### 핵심 CLI 명령 카테고리

| 카테고리 | 핵심 명령 |
| --- | --- |
| **Team** | `clawteam team spawn-team`, `status`, `snapshot`, `restore` |
| **Task** | `clawteam task create`, `update`, `list`, `wait` (`--blocked-by` 포함) |
| **Inbox** | `clawteam inbox send`, `broadcast`, `receive`, `peek` |
| **Board** | `clawteam board show`, `live`, `attach`, `gource`, `serve` |
| **Profile** | `clawteam profile wizard`, `test`, `doctor`, `generate-profile` |
| **Context** | `clawteam context inject`, `conflicts`, `log` |
| **Spawn** | `clawteam spawn [backend] [command] --profile ...` |

### 상류로부터의 3 레퍼런스 시나리오

1. **AutoResearch (H100 위 8 Agents)** — 8 탐색 Agents 가 자율적으로 2,430+ 실험 설계; val_bpb 가 1.044 → 0.977 (+6.4%) 향상.
2. **Full-Stack Software Engineering (5 Agents)** — Architect, Backend (OAuth2 + DB), Frontend (React), Test/QA — 병렬 브랜치 자동 머지.
3. **AI Hedge Fund (7 Agents)** — Portfolio Manager + Value/Growth/Technical/Fundamentals/Sentiment Analysts + Risk Manager — 시그널이 메시징 층을 통해 수렴.

### 로드맵 요약

- **v0.3** — Config 시스템, Multi-User (`CLAWTEAM_USER`), Web UI 대시보드, SSHFS / 클라우드 기반 크로스머신 공유
- **v0.4** — Redis transport (크로스머신 메시징)
- **v0.5** — 공유 state 층 (NFS 또는 Redis); `RedisTeamStore` / `RedisTaskStore`
- **v0.6** — 아이덴티티, 권한, 네임스페이싱, 토큰 인증 (분산 팀)
- **v1.0** — 완전한 Web UI, 실시간 WebSocket, 멀티팀 개관

---

## 3. 라이선스 요약

ClawTeam 은 **MIT License** 하 출시. MIT 는 다음을 허용:

- 자유롭게 사용, 수정, 재배포
- 상업적으로 사용
- 프로프라이어터리 제품의 일부로 포함

**유일한 조건**: 재배포 시, 오리지널 **MIT 저작권 통지** 와 **MIT License 텍스트** 를 보존해야 함.

> ⚠️ **중요**
> 본 repo 는 ClawTeam 소스 코드를 **재배포하지 않음**. L5 코스에서 그 아키텍처, CLI, 디자인 원칙을 **인용 및 교육**만 하고, 학습자에게는 **상류에서 직접 설치**하도록 안내 (`pip install clawteam`). 코스 파생물 (예: 포크, 배포 또는 커스터마이즈) 이 ClawTeam 코드를 재배포하는 경우, 오리지널 MIT 라이선스 통지를 포함해야 함.

---

## 4. 본 방법론에서의 인용 범위

| 범위 | 처리 |
| --- | --- |
| **아키텍처 & 디자인 개념** | L5 의 **주요 교육 플랫폼**으로 사용; 강의 계획서가 그 Team / Workspace / Task / Inbox / Transport 아키텍처를 기술 |
| **CLI 명령** | L5 핸즈온 세션 중 **직접** 사용 |
| **3 레퍼런스 시나리오** | **영감**으로 사용; 본 방법론은 제조, 병원, 소매 기업 시나리오로 로컬라이즈 |
| **소스 코드** | **재현하지 않음, 포크하지 않음**; 학습자는 상류에서 `pip install` |
| **브랜드 / 로고** | 코스와 본 문서에서 「ClawTeam」 이름으로 인용; 로고 재현 없음 |

## 5. 학습자용 인용 형식

슬라이드, 보고서, PoC 또는 파생 작업에서 ClawTeam 을 인용할 때, 다음 형식 사용:

**APA 스타일:**

> HKUDS. (2026). *ClawTeam: Agent Swarm Intelligence* (Version 0.2-0.3) [Computer software]. GitHub. https://github.com/HKUDS/ClawTeam

**축약형:**

> Built on ClawTeam by HKUDS — <https://github.com/HKUDS/ClawTeam> (MIT License)

**학술 인용:**

> ClawTeam [Software]. HKUDS, 2026. Available at: https://github.com/HKUDS/ClawTeam. MIT License.

## 6. 감사

**HKUDS (HKU Data Science Lab)** 가 ClawTeam 을 오픈소스화한 것에 감사, 이것은 기업 멀티 에이전트 협업을 연구 프로젝트에서 가르칠 수 있고, 배울 수 있고, 배포 가능한 엔지니어링 실천으로 승화시켰음. 본 방법론의 L5 코스 디자인은 그 아키텍처에 깊이 정보를 얻었고 대만과 중국어권에서의 기업 채택을 위해 로컬라이즈됨.

---

## 7. 면책 조항

- 본 방법론에서 ClawTeam 의 기술, 적용 또는 로컬 적응은 방법론 저자 (Morris Lu / Tiger AI 虎智科技) 의 해석을 나타내며, HKUDS 또는 ClawTeam 메인테이너의 공식 입장을 **나타내지 않음**.
- ClawTeam 의 API, 명령 또는 아키텍처가 새 버전에서 변경되면, 권위 있는 현재 상태에 대해서는 [상류 리포지토리](https://github.com/HKUDS/ClawTeam) 참조.
- 방법론 저자는 상류 ClawTeam 변경에 맞춰 본 문서를 업데이트할 권리를 보유.
