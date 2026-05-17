# consultant Frameworks — 인용 & 라이선스 통지

> 🌐 언어: [繁體中文](CONSULTANT_FRAMEWORKS_REFERENCE.md) ｜ [English](CONSULTANT_FRAMEWORKS_REFERENCE_EN.md) ｜ [Deutsch](CONSULTANT_FRAMEWORKS_REFERENCE_DE.md) ｜ [Français](CONSULTANT_FRAMEWORKS_REFERENCE_FR.md) ｜ [Español](CONSULTANT_FRAMEWORKS_REFERENCE_ES.md) ｜ [日本語](CONSULTANT_FRAMEWORKS_REFERENCE_JA.md) ｜ 한국어

본 방법론의 [`03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) 의 프레임워크 리스트와 분류는 **yoichiojima-2/consultant** 에 기반해 참조 및 재작성. 본 문서는 상류 소스, 라이선스 조건, 인용 가이드, 적응 범위를 기록.

---

## 1. 상류 프로젝트

| 필드 | 값 |
| --- | --- |
| **프로젝트** | consultant |
| **메인테이너** | @yoichiojima-2 |
| **GitHub URL** | <https://github.com/yoichiojima-2/consultant> |
| **라이선스** | **MIT License** |
| **형식** | Claude Code 플러그인 (`/plugin marketplace add` 를 통해 설치) |
| **콘텐츠** | 7 카테고리에 걸친 50+ 고전 컨설팅 프레임워크 (McKinsey / BCG / Bain / Accenture), markdown skill 로 패키징 |

## 2. consultant 란

consultant 는 **Claude Code 플러그인**, 50+ 고전 경영 컨설팅 프레임워크 (MECE, Pyramid Principle, Porter's 5 Forces, SWOT, BCG Matrix, PESTEL, 5 Whys, Fishbone, Business Model Canvas, WBS, RACI, Kotter, OKR, NPV/IRR, Lean, Six Sigma 등) 를 markdown skill 로 패키징.

### 구조적 특징

- **7 카테고리 분류**: problem solving / strategy analysis / case frameworks / business design / project & change / financial analysis / operations.
- **트리거 인식**: 자연어 「나는 …이 필요해」 문장을 프레임워크 조합으로 라우팅.
- **프레임워크 조합**: 사전 구축된 다중 프레임워크 체인 (예: PESTEL → 5 Forces → 3C → SWOT → Issue Tree).
- **프레임워크별 표준 구조**: 기원 / 핵심 개념 / 단계 / 적용 방법 / 실제 예시 / 흔한 함정.

## 3. 무엇을 적응하고 인용했나

| 범위 | 처리 |
| --- | --- |
| **프레임워크 리스트와 7 카테고리 분류** | 분류 참조, 본 방법론의 언어로 재작성 |
| **「프레임워크 셀렉터」 개념** (자연어 → 프레임워크) | 트리거 인식 패턴을 본 방법론 시나리오에 정렬된 셀렉터로 적응 |
| **「프레임워크 조합 체인」 개념** | 조합 체인 패턴 적응, 본 방법론의 8 단계에 매핑 |
| **프레임워크별 확장 형식** | 프레임워크별 구조 참조, 「maps-to-stage」 열 추가 |
| **고전 프레임워크 자체** (MECE, Porter's 5 Forces 등) | 퍼블릭 도메인 경영 지식, consultant 에 전용 아님 |
| **오리지널 markdown skill 파일** | **재현하지 않음, 포크하지 않음**; 본 방법론은 독립적 재작성 |

## 4. 라이선스 요약

consultant 는 **MIT License** 하 출시, 프로프라이어터리 제품의 일부로 포함하여 자유 사용, 수정, 재배포, 상업적 사용을 허용; 유일한 조건은 소스 재배포 시 MIT 저작권 통지와 라이선스 텍스트를 보존하는 것.

본 방법론은 consultant 의 소스 코드를 **재배포하지 않음** — consultant 의 프레임워크 리스트와 디자인 패턴을 참조한 후, `CONSULTING_FRAMEWORKS_LIBRARY.md` 를 독립적으로 재작성. 재작성된 파일은 본 repo 의 Apache 2.0 하; 그럼에도, 오리지널 저자의 기여에 대한 존중으로, 그 파일과 여기에 **인용 소스를 명시적으로 기재**.

## 5. 학습자용 인용 형식

> consultant by @yoichiojima-2 에서 적응된 프레임워크 라이브러리 — <https://github.com/yoichiojima-2/consultant> (MIT License)

## 6. 면책 조항

본 방법론에서 consultant 의 인용, 적응, 8 단계 매핑은 방법론 저자 (Morris Lu / Tiger AI 虎智科技) 의 해석을 나타내며, @yoichiojima-2 의 공식 입장을 나타내지 않음. 고전 컨설팅 프레임워크의 정의와 적용에 대해서는, 각 프레임워크의 오리지널 학술 / 산업 소스 참조. consultant 의 프레임워크 리스트 또는 구조가 새 버전에서 변경되면, [상류 리포지토리](https://github.com/yoichiojima-2/consultant) 를 참조.
