# mckinsey-consultant-skills — 인용 & 라이선스 통지

> 🌐 언어: [繁體中文](MCKINSEY_SKILLS_REFERENCE.md) ｜ [English](MCKINSEY_SKILLS_REFERENCE_EN.md) ｜ [Deutsch](MCKINSEY_SKILLS_REFERENCE_DE.md) ｜ [Français](MCKINSEY_SKILLS_REFERENCE_FR.md) ｜ [Español](MCKINSEY_SKILLS_REFERENCE_ES.md) ｜ [日本語](MCKINSEY_SKILLS_REFERENCE_JA.md) ｜ 한국어

본 방법론의 [`03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) 의 생산 워크플로는 **Kafurtan/mckinsey-consultant-skills** 에 기반해 참조 및 재작성. 본 문서는 상류 소스, 라이선스 조건, 인용 가이드, 적응 범위를 기록.

---

## 1. 상류 프로젝트

| 필드 | 값 |
| --- | --- |
| **프로젝트** | mckinsey-consultant-skills (V3.1) |
| **메인테이너** | @Kafurtan |
| **GitHub URL** | <https://github.com/Kafurtan/mckinsey-consultant-skills> |
| **라이선스** | **MIT License** |
| **형식** | AI agent skill (`SKILL.md` + `references/`) |
| **콘텐츠** | 「비즈니스 문제 → McKinsey 스타일 프레젠테이션」 을 자동화하는 8 단계 워크플로, 엔드 투 엔드 90-110 분 |

## 2. mckinsey-consultant-skills 란

McKinsey 의 Problem Solving 방법론을 **8 단계 워크플로** 로 시스템화, AI 어시스턴트가 비즈니스 문제를 전문적인 프레젠테이션 (PPT + Excel evidence trail) 으로 변환할 수 있게 함.

### 구조적 특징

- **8 단계 워크플로**: 경계 정의 → Issue Tree + 가설 → Dummy Pages + 디자인 사양 → 페이지별 반복 생산 → PPT + Excel → 선택적 Word 보고서 → 반복 개정.
- **Dummy Page**: 리서치 전에 와이어프레임 사양 구축, 목적 없는 데이터 수집을 피하고 대화 간 재개를 지원.
- **의존성 인식**: 페이지에 의존성 상태 태그 부여, 생산 순서 결정 (executive summary 는 마지막).
- **7 페이지 레이아웃**: 제목 + 단일 차트 / 2 열 / 2×2 매트릭스 / 테이블 / waterfall chart / 타임라인 / 인사이트 요약.
- **Excel evidence trail**: 페이지별 raw data + URL + 정리 프로세스.
- **Progressive disclosure**: 참조 파일은 필요한 단계에서만 로드, 그 후 해제, ~70% 컨텍스트 절약.
- `references/`: methodology.md, layouts.md, design-specs.md, examples.md, troubleshooting.md.

## 3. 무엇을 적응하고 인용했나

| 범위 | 처리 |
| --- | --- |
| **8 단계 생산 워크플로** | 워크플로 참조, 본 방법론의 언어로 재작성, 8 단계 컨설팅 구조에 매핑 |
| **Dummy Page 개념** | 「skeleton-first, fill-in-later」 규율을 본 방법론 데크 아웃라인의 페이지별 사양으로 적응 |
| **의존성 인식** | 페이지 의존성 관리 개념 적응 |
| **7 페이지 레이아웃** | 레이아웃 리스트 참조, `VISUAL_ASSETS_SPEC.md` 확장을 위해 재작성 |
| **Excel evidence trail, progressive disclosure** | 개념 적응, 본 방법론의 Evidence 규율과 AI-IDE Context Management 에 매핑 |
| **McKinsey Problem Solving, MECE, Pyramid Principle** | 퍼블릭 도메인 경영 지식, 본 프로젝트에 전용 아님 |
| **오리지널 `SKILL.md` 와 `references/` 파일** | **재현하지 않음, 포크하지 않음**; 본 방법론은 독립적 재작성 |

## 4. 라이선스 요약

mckinsey-consultant-skills 는 **MIT License** 하 출시, 프로프라이어터리 제품의 일부로 포함하여 자유 사용, 수정, 재배포, 상업적 사용을 허용; 유일한 조건은 소스 재배포 시 MIT 저작권 통지와 라이선스 텍스트를 보존하는 것.

본 방법론은 소스 코드를 **재배포하지 않음** — 워크플로와 디자인 패턴을 참조한 후, `REPORT_PRODUCTION_WORKFLOW.md` 를 독립적으로 재작성. 재작성된 파일은 본 repo 의 Apache 2.0 하; 그럼에도, 오리지널 저자의 기여에 대한 존중으로, 그 파일과 여기에 **인용 소스를 명시적으로 기재**.

## 5. 학습자용 인용 형식

> mckinsey-consultant-skills by @Kafurtan 에서 적응된 생산 워크플로 — <https://github.com/Kafurtan/mckinsey-consultant-skills> (MIT License)

## 6. 면책 조항

본 방법론에서 mckinsey-consultant-skills 의 인용, 적응, 8 단계 매핑은 방법론 저자 (Morris Lu / Tiger AI 虎智科技) 의 해석을 나타내며, @Kafurtan 의 공식 입장을 나타내지 않음. 「McKinsey」 는 McKinsey & Company 의 상표; 본 방법론은 McKinsey & Company 와 어떤 제휴나 보증도 없으며, 관련 방법론 이름은 퍼블릭 도메인 경영 지식에 대한 참조로만 사용. mckinsey-consultant-skills 의 워크플로 또는 구조가 새 버전에서 변경되면, [상류 리포지토리](https://github.com/Kafurtan/mckinsey-consultant-skills) 를 참조.
