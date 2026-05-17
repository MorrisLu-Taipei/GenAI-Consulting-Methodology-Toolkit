# TigerAI-n8n-Skill-Pack 인용 & 라이선스 통지

> 🌐 언어: [繁體中文](N8N_SKILL_PACK_REFERENCE.md) ｜ [English](N8N_SKILL_PACK_REFERENCE_EN.md) ｜ [Deutsch](N8N_SKILL_PACK_REFERENCE_DE.md) ｜ [Français](N8N_SKILL_PACK_REFERENCE_FR.md) ｜ [Español](N8N_SKILL_PACK_REFERENCE_ES.md) ｜ [日本語](N8N_SKILL_PACK_REFERENCE_JA.md) ｜ 한국어

본 방법론의 **L3 Workflow Automation** 코스 후반은 「Antigravity 로 자연어에서 n8n 워크플로 생성」 의 교육 플랫폼으로 **TigerAI-n8n-Skill-Pack** 을 인용. 본 문서는 상류 소스, 라이선스 조건, 인용 가이드, 사용 범위를 기록.

---

## 1. 상류 프로젝트

| 필드 | 값 |
| --- | --- |
| **프로젝트** | TigerAI-n8n-Skill-Pack |
| **메인테이너** | Morris Lu (盧業興) — n8n Taipei Ambassador |
| **GitHub URL** | <https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack> |
| **라이선스** | 혼합: Skills / Cookbook / Specs 는 **TigerAI Proprietary**; `skills/_vendor/` 는 **MIT** (czlonkowski/n8n-skills 에서); `reference-workflows/` 는 **MIT** (Zie619/n8n-workflows 에서, secrets 스크럽됨) |
| **규모** | 13 Skills (7 vendor + 6 custom), 8 cookbook 레시피, 2,061 reference workflows, DSL v1.2 spec, 3 플래그십 예시 |
| **지원 도구** | Antigravity (네이티브 agentic 오케스트레이션), Claude Code (CLI / VS Code), n8n (2.10.3+), 임의의 AI 어시스턴트 (cookbook few-shot prompting 을 통해) |

> **참고:** 이는 방법론 저자 Morris Lu 자신의 프로젝트; 인용에 제3자 라이선스 장애 없음, 그러나 `_vendor/` 와 `reference-workflows/` 의 MIT 소스는 저작권 통지를 유지해야 함 (상류 `THIRD_PARTY_NOTICES.md` 참조).

## 2. TigerAI-n8n-Skill-Pack 란

수동 node 구성 대신 **자연어 기술**에서 기업급 n8n 워크플로를 생성할 수 있게 함. 시스템은 「sticky-note」 평문 의도를 완전, 문서화된 배포 준비 완료 workflow JSON 으로 변환.

### 3 층 구조

`노란색 sticky-note 의도` + `파란색 sticky-note 노트` + `workflow nodes` — 사용자가 의도를 작성 → AI 가 3 층 JSON 생성 → n8n API 를 통해 배포.

### 3 사용 모드

1. **Cookbook 복사** — 8 개의 사전 구축된 레시피 템플릿에서 선택
2. **Q&R 모드** — AI 가 사용자를 요구사항 수집을 통해 안내
3. **Example finder** — 2,061 reference workflows 중에서 유사 구현 발견

### 설치

`bash install.sh` (Unix) 또는 `install.ps1` (Windows).

## 3. 왜 L3 후반에 속하는가

L3 코스는 「개념 먼저, 생성 후」 원칙으로 반으로 분할:

- **L3 전반** (§5.1 Foundation + §5.2 Builder): 학습자가 Trigger / Node / AI / Human Gate / Error Handling 을 **수작업으로 구축**, 워크플로 구조와 거버넌스를 이해.
- **L3 후반** (§5.5): 그 기반 위에서, Antigravity + TigerAI-n8n-Skill-Pack 을 사용해 자연어 의도에서 직접 workflow JSON 을 생성, 생성된 결과를 **검토** 하는 법을 배움.

> **핵심 원칙: Skill Pack 은 가속기이며, 이해의 대체가 아님.** 전반에서 워크플로를 수작업으로 구축하지 않고는, 학습자는 생성된 결과가 정확한지, 안전한지, 유지 가능한지 판단할 수 없음.

대응 코스: [`../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](../02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md) §1.1, §5.5.

## 4. 라이선스 요약

| 부분 | 라이선스 | 의무 |
| --- | --- | --- |
| `skills/` (custom), `cookbook/`, `spec/` | TigerAI Proprietary | 저자 Morris Lu 에 의해 라이선스; 본 방법론 내 사용에 장애 없음; 외부 재배포에는 저자의 동의 획득 |
| `skills/_vendor/` | MIT (czlonkowski/n8n-skills) | MIT 저작권 통지 보존 |
| `reference-workflows/` | MIT (Zie619/n8n-workflows) | MIT 저작권 통지 보존; secrets 는 스크럽되었지만 직접 검증 |

> ⚠️ **중요**
> 본 repo 는 TigerAI-n8n-Skill-Pack 소스를 **재배포하지 않음**. L3 코스에서 그 구조와 사용법을 **인용 및 교육**만 하고, 학습자에게는 **상류에서 직접 설치**하도록 안내. Skill Pack 을 사용해 학습자가 생성한 워크플로는 기업에 속함.

## 5. 인용 범위

| 범위 | 처리 |
| --- | --- |
| **교육 플랫폼으로서** | L3 후반 (§5.5) 의 주요 구현 플랫폼 |
| **소스 / Skills** | **재현하지 않음, 포크하지 않음**; 학습자는 `install.sh` / `install.ps1` 을 통해 직접 설치 |
| **reference-workflows** | 「Example finder」 레슨에서 인용; 학습자는 잔여 secrets / 내부 endpoint 가 없음을 확인해야 함 |
| **생성된 출력** | 생성된 workflow JSON 은 기업 자산; 기업급 PoC 로 카운트되려면 Gates 3A-3G 를 통과해야 함 |

## 6. 학습자용 인용 형식

> Built with TigerAI-n8n-Skill-Pack by Morris Lu — <https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack>

## 7. 면책 조항

TigerAI-n8n-Skill-Pack 은 방법론 저자 Morris Lu 자신의 프로젝트. Skills, cookbook, DSL spec, 설치가 새 버전에서 변경되면, [상류 리포지토리](https://github.com/MorrisLu-Taipei/TigerAI-n8n-Skill-Pack) 와 `THIRD_PARTY_NOTICES.md` 참조. AI 생성 워크플로는 항상 인간 검토와 Gate 3 Acceptance 를 거쳐야 함 — 생성은 Acceptance 가 아님.
