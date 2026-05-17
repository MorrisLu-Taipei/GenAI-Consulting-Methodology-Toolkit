# OpenWebUI 영상 학습 노트와 적용 요약

> 🌐 언어: [繁體中文](OPENWEBUI_VIDEO_LEARNING_NOTES.md) ｜ [English](OPENWEBUI_VIDEO_LEARNING_NOTES_EN.md) ｜ [Deutsch](OPENWEBUI_VIDEO_LEARNING_NOTES_DE.md) ｜ [Français](OPENWEBUI_VIDEO_LEARNING_NOTES_FR.md) ｜ [Español](OPENWEBUI_VIDEO_LEARNING_NOTES_ES.md) ｜ [日本語](OPENWEBUI_VIDEO_LEARNING_NOTES_JA.md) ｜ 한국어

버전: v1.0
노트 작성: Morris Lu (盧業興) · Tiger AI 虎智科技
목적: 공개 OpenWebUI 플레이리스트를 L1 기업 온보딩 코스를 위한 학습 노트, 요약, 미래 적용 맵으로 변환.

## 原始影片版權聲明 / Third-Party Video Credits

> **本文件為第三方公開影片的學習筆記，並非影片本身。所有影片內容與版權皆歸原始創作者所有，本文件僅作為學習與課程設計用途引用其公開連結。**
>
> **본 문서는 공개적으로 이용 가능한 제3자 영상에서 파생된 학습 노트를 포함. 이는 전사 또는 복제가 **아님**. 모든 영상 콘텐츠와 저작권은 원본 크리에이터에게 남음; 링크는 교육 및 코스 설계 참조 목적으로만 여기에 인용.**

- **原始 Playlist / 오리지널 플레이리스트**: <https://www.youtube.com/watch?v=oXJ4L1G8kaI&list=PL_rTgQnnMXsXAsEiid-tWhaj03SsP4U5Z>
- 각 영상의 오리지널 링크와 제목이 아래 표에서 개별 인용됨; 권위적인 콘텐츠는 오리지널 소스를 참조해주세요.

당신이 권리 보유자이며 귀속을 업데이트하거나 인용 제거를 요청하고 싶다면, 본 리포지토리에 issue 를 열어주세요.

---

## 1. 본 문서 사용법

본 문서는 전사가 아님; 코스 설계를 위한 학습 기록. 각 영상은 다음에 매핑:

1. 영상의 주제.
2. 학습 요약.
3. TigerAI L1-L5 방법론 내에서의 미래 적용.
4. 코스 우선순위.

우선순위 정의:

| 우선순위 | 설명 |
|---|---|
| P0 | L1 기업 enablement 필수; 계정, 로그인, 사용, 권한, 데이터 보안에 직접 영향 |
| P1 | Admin / IT 필수; 배포, 모델, operations, 권한, 업데이트에 영향 |
| P2 | 선택적 기능; 고객 요구에 따라 포함 |
| P3 | 영감적 케이스; 데모용 또는 follow-on L2/L3/L4 확장으로 사용 가능 |

---

## 2. L1 코스 전체 결론

OpenWebUI 를 단순히 「무료 ChatGPT 대안」 으로 패키징해서는 안 됨. 기업 채택 동안 그 core 가치는:

> 기업이 AI 사용을 관리하는 통제된 진입점. 각 직원이 자신의 계정과 채팅 영역을 가지며, Admin 이 역할, 그룹, 권한, 모델, 도구, 데이터 경계를 관리 가능.

따라서 L1 코스의 주 스레드는:

1. 각 사람이 개별 로그인; 공유 계정 없음.
2. 각 사람이 자신의 채팅 히스토리, 폴더, Prompts, 개인 설정 보유.
3. Admin 이 users, 역할, 그룹, 권한, 모델 가시성 관리 가능.
4. IT 가 로컬 모델, 클라우드 API, Hybrid 모드, 운영 업데이트 전략 결정 가능.
5. HR / management 가 AI 사용 가이드라인과 데이터 입력 경계 수립 가능.
6. L1 출력은 L2 로 다리 놓아야 함: 고빈도 Prompts 와 작업 시나리오를 Skill 후보로 조직.

---

## 3. 영상 학습 요약과 미래 적용

| # | 영상 | 학습 요약 | 미래 적용 | 우선순위 |
|---:|---|---|---|---|
| 1 | [Open WebUI: The Free, Private ChatGPT Alternative](https://www.youtube.com/watch?v=oXJ4L1G8kaI) | OpenWebUI 의 포지셔닝, 가치, 기본 사용 시나리오. | L1 오프닝 세션, 기업이 자체 AI 진입점이 필요한 이유 설명에 사용. | P0 |
| 2 | [How to Install OpenWebUI](https://www.youtube.com/watch?v=d6Su3Nmv7-8) | OpenWebUI 의 기초 설치 흐름. | IT 사전 코스 준비, PoC 환경 셋업, 배포 체크리스트. | P1 |
| 3 | [Local AI Model Requirements](https://www.youtube.com/watch?v=CYBu9dTVWC4) | 로컬 모델에 필요한 CPU, RAM, GPU 개념. | 클라우드 AI / Hybrid / 완전 온프레 배포 평가; 고객이 하드웨어 임계값 판단 도움. | P1 |
| 4 | [Exploring the OpenWebUI Admin Panel](https://www.youtube.com/watch?v=4pIzLtUhJLM) | Admin Panel 기능과 관리 진입점 개요. | L1 Admin 코스 필수; 계정, 모델, 기능, 설정 관리 다룸. | P0 |
| 5 | [Exploring Open WebUI: Features, Models, & Tools](https://www.youtube.com/watch?v=CDiVq3mPZc8) | OpenWebUI 기능, 모델, 도구 개요. | L1 올핸즈 투어, 트레이니가 사용 가능한 기능과 경계 이해. | P0 |
| 6 | [How to Chat with Your Own Documents](https://www.youtube.com/watch?v=lqKapMX2GAI) | 자신의 문서로 채팅과 Q&A. | L1 문서 요약과 저민감도 문서 Q&A; 고민감도 데이터는 별도 가이드라인 필요. | P0 |
| 7 | [How to Add Real-Time Web Search](https://www.youtube.com/watch?v=_KoifHHJhNY) | 실시간 Web Search 추가. | 리서치, 영업, 마케팅 시나리오; 기업은 출처 인용 규칙과 권한 설정해야 함. | P2 |
| 8 | [How to Add GPT-4 to OpenWebUI](https://www.youtube.com/watch?v=ZUc50fcWO2E) | OpenAI API / GPT-4 클래스 모델 통합. | Admin / IT 클라우드 모델 제공자 셋업; Hybrid 아키텍처에 사용 가능. | P1 |
| 9 | [How to Use Community Tools](https://www.youtube.com/watch?v=juAbnns5Ohg) | 커뮤니티 도구로 기능 확장. | L2/L3 전구; 기업은 먼저 보안 검토와 도구 화이트리스트 수행. | P2 |
| 10 | [Text-to-Speech with ElevenLabs API](https://www.youtube.com/watch?v=LzlzXQzBUcg) | TTS 와 오디오 출력 통합. | 고객 서비스, 교육, 훈련 자료 선택; L1 core 아님. | P2 |
| 11 | [How to Create Custom AI Models](https://www.youtube.com/watch?v=Fd_1zePgCLE) | 커스터마이즈된 모델 설정 또는 모델 페르소나 생성. | 부서 기본 모델, 페르소나 기반 어시스턴트; L2 Skills 로 다리. | P2 |
| 12 | [AI Images with OpenWebUI & DALL-E 3](https://www.youtube.com/watch?v=3rg8Tdyn_RA) | 이미지 생성 기능. | 마케팅과 디자인 선택; 저작권, 브랜드, 검토 주의 필요. | P2 |
| 13 | [LLAVA Multimodal / GPT-4 Image Analysis](https://www.youtube.com/watch?v=yZkmolyV0Zk) | 멀티모달 모델로 이미지 분석. | QC, 헬스케어, 문서 이미징 예비 탐색; 고위험 시나리오는 사람 검토 필요. | P2 |
| 14 | [AI Clone](https://www.youtube.com/watch?v=dXaFbHw5-m8) | 개인화된 AI 클론 데모. | 영감 데모; 기업 채택은 프라이버시와 유사성/음성 라이선싱의 특별 처리 필요. | P3 |
| 15 | [Functions to Build Websites & Apps](https://www.youtube.com/watch?v=KbkfaapAvpE) | Functions 로 애플리케이션 기능 확장. | L2/L3 확장: 채팅 기능을 실행 가능한 도구 또는 앱 프로토타입으로 전환. | P2 |
| 16 | [Reduce AI Hallucinations with Advanced Parameters](https://www.youtube.com/watch?v=OWsFsnnrMdE) | 고급 파라미터로 환각 위험 감소. | L1 필수; 데이터 신뢰성, 인간 검증, 모델 파라미터 교육에 사용. | P0 |
| 17 | [Choosing the Right Ollama Model](https://www.youtube.com/watch?v=KIc1lRmehyY) | 적절한 로컬 Ollama 모델 선택. | IT / Admin 모델 관리와 온프레 배포 평가. | P1 |
| 18 | [Mobile Access with Ngrok](https://www.youtube.com/watch?v=DFtI1m957XM) | Ngrok 을 통한 OpenWebUI 원격 또는 모바일 액세스. | 선택; 기업은 보안, VPN, 노출 표면, 액세스 제어 고려해야 함. | P2 |
| 19 | [Choosing the Best Language Model](https://www.youtube.com/watch?v=-yhChXlYjbQ) | 다양한 언어 모델 중 선택 방법. | 모델 카탈로그와 부서 적합 모델 관리; 모델 평가 시트로 다리. | P1 |
| 20 | [Vision LLMs for Local Inference](https://www.youtube.com/watch?v=VDLNtKbfewQ) | 로컬 비전 모델 비교. | QC, 이미지 문서, 의료 이미징 탐색; 고급 선택 콘텐츠. | P2 |
| 21 | [AI Recruiter Meets AI Clone](https://www.youtube.com/watch?v=649qtKjbnk4) | AI 클론으로 채용 데모 시나리오. | HR 영감 케이스; L2 채용 Skill 또는 L3 채용 워크플로로 전환 가능. | P3 |
| 22 | [Groq Cloud & OpenWebUI](https://www.youtube.com/watch?v=Ukft9qfb67o) | Groq Cloud 같은 클라우드 모델 통합. | IT / Admin 다중 모델 제공자 전략. | P1 |
| 23 | [Docker & Watchtower](https://www.youtube.com/watch?v=W0Yh_HsMkOQ) | Docker 컨테이너 자동 업데이트와 operations. | IT operations 필수; OpenWebUI 업데이트와 서비스 안정성 다룸. | P1 |
| 24 | [OpenWebUI Pipelines](https://www.youtube.com/watch?v=DFlSd6GrMIk) | 커스텀 Pipelines 워크플로 기능. | L3 미리보기; 나중에 n8n, API, 데이터 처리 파이프라인으로 다리 가능. | P2 |
| 25 | [Set Up User Roles for Secure Collaboration](https://www.youtube.com/watch?v=xlE782FrW_s) | 사용자 역할과 보안 협업 셋업. | L1 Admin 필수; 개인별 계정, 역할, 그룹, 권한 다룸. | P0 |
| 26 | [Writing Better Prompts](https://www.youtube.com/watch?v=FYTir7cor1c) | 더 좋은 Prompts 작성. | 모든 L1 필수; Prompt Library 와 L2 Skill 후보로 다리. | P0 |
| 27 | [Arena Model](https://www.youtube.com/watch?v=PU7B5FHalrg) | 모델 비교와 성능 테스트. | Admin / 시드 유저가 모델 평가와 조달 결정에 사용. | P1 |
| 28 | [Run Text-to-Speech Locally](https://www.youtube.com/watch?v=lwk0QGLou9Y) | 로컬 TTS. | 고프라이버시 음성 요구의 선택; L1 core 아님. | P2 |
| 29 | [OpenWebUI Memory Explained](https://www.youtube.com/watch?v=a0H2w5z_uk4) | 메모리와 개인화 개념. | 개인화 기능 소개로 작동 가능; 기업은 프라이버시, 삭제, 데이터 보존 정책 다뤄야 함. | P2 |
| 30 | [Quantization](https://www.youtube.com/watch?v=7J-AKL2TAD0) | 모델 양자화와 성능 향상. | IT 의 선택; 온프레 배포와 비용 통제 지원. | P2 |
| 31 | [AI-Powered Recruiter Bot](https://www.youtube.com/watch?v=XPeZGo6McLc) | 리크루터 봇 구축. | HR / L2 / L3 케이스: 직무 분석, 이력서 요약, 인터뷰 질문 작성. | P3 |
| 32 | [Open WebUI v0.4 Updates](https://www.youtube.com/watch?v=qESVuLFHYqI) | 버전 업데이트와 새 기능. | IT / Admin 버전 인식; 업데이트 체크 SOP 수립. | P1 |
| 33 | [Anthropic Claude Models in OpenWebUI](https://www.youtube.com/watch?v=1jahR-BA6Ts) | Claude 모델 통합. | Admin / IT 다중 제공자 셋업; Hybrid 모델 전략에 적합. | P1 |
| 34 | [Public Access to OpenWebUI Chatbots](https://www.youtube.com/watch?v=0pyHYhzqdRQ) | 공용 Chatbot 액세스. | 고위험 기능; 기업은 엄격히 거버넌스해야 함. 외부 고객 서비스에 대한 사전 PoC 논의에 적합. | P2 |
| 35 | [Tools, Functions & Pipelines Deep Dive](https://www.youtube.com/watch?v=wRkAko8yphs) | Tools, Functions, Pipelines 의 딥 다이브. | L2/L3 미리보기; OpenWebUI 를 채팅 진입점에서 도구와 워크플로로. | P2 |
| 36 | [Online? Offline? Both?](https://www.youtube.com/watch?v=W9czUS3trMU) | 온라인, 오프라인, 하이브리드 모드 논의. | L1 배포 모드 논의 필수; 클라우드 AI / Hybrid / 완전 온프레 다룸. | P0 |

---

## 4. 권장 시청 경로

### 4.1 모든 L1 사용자

권장 시청:

1. #1 OpenWebUI 포지셔닝.
2. #5 기능, 모델, 도구 개요.
3. #6 문서 채팅.
4. #16 환각 감소와 고급 파라미터.
5. #26 Prompt 작성.
6. #36 온라인 / 오프라인 / 하이브리드 모드.

목적: 직원이 안전하게 로그인, 자신의 채팅 영역 구축, 일일 작업 완료, 데이터 경계 이해 가능하게 함.

### 4.2 Admin / IT

권장 시청:

1. #2 설치.
2. #3 로컬 모델 하드웨어 요구사항.
3. #4 Admin Panel.
4. #8 OpenAI API.
5. #17 Ollama 모델.
6. #19 모델 선택.
7. #22 Groq Cloud.
8. #23 Docker / Watchtower.
9. #25 User Roles.
10. #32 버전 업데이트.
11. #33 Claude 모델.

목적: IT 가 OpenWebUI 를 구축, 운영, 관리, 거버넌스할 수 있게 함.

### 4.3 L2 / L3 확장

권장 시청:

1. #9 Community Tools.
2. #11 Custom AI Models.
3. #15 Functions.
4. #24 Pipelines.
5. #35 Tools / Functions / Pipelines Deep Dive.

목적: OpenWebUI 를 L1 채팅 진입점에서 L2 Skills 와 L3 Workflows 로 다리.

### 4.4 산업 / 부서 선택

| 산업 / 부서 | 권장 영상 |
|---|---|
| HR | #21, #31 |
| 마케팅 / 디자인 | #12 |
| 고객 서비스 / 교육과 훈련 | #10, #28 |
| QC / 헬스케어 / 이미지 문서 | #13, #20 |
| 고프라이버시 기업 | #3, #17, #23, #30, #36 |

---

## 5. 코스와 딜리버리 적용

### 5.1 L1 코스 적용

다음 코스 산출물로 전환해야 함:

- OpenWebUI 사용자 운영 매뉴얼.
- OpenWebUI Admin Runbook.
- 계정 / 그룹 / 권한 / 모델 가시성 구성 시트.
- AI 사용 가이드라인.
- Prompt Library v1.
- Gate 1 수락 시트.

### 5.2 L2 코스 적용

다음 영상은 Skill 후보로 전환 가능:

- #26 Prompt 작성 → Prompt Skill.
- #6 문서 채팅 → 문서 요약 Skill.
- #11 Custom AI Models → 부서 페르소나 모델 Skill.
- #15 Functions → 도구화된 Skill.
- #35 Tools / Functions / Pipelines → L2-에서-L3 다리.

### 5.3 L3 코스 적용

다음 영상은 Workflow 후보로 전환 가능:

- #7 Web Search → 시장 조사 Workflow.
- #24 Pipelines → 커스텀 처리 흐름.
- #35 Tools / Functions / Pipelines → OpenWebUI + n8n 흐름 다리.
- #34 Public Chatbots → 외부 고객 서비스 Bot PoC, 그러나 엄격한 권한과 검토 필요.

---

## 6. 기업 채택 노트

1. 계정은 공유해서는 안 됨; 그렇지 않으면 개인별 채팅 영역, 책임, 권한 거버넌스 불가능.
2. 신규 사용자는 기본적으로 고급 기능을 받지 않아야 함; Admin 검토 권장.
3. File Upload, Web Search, Tools, Functions, Pipelines, Public Share 는 모두 고급 기능으로 다뤄야 함.
4. 각 부서는 자체 그룹과 모델 가시성 전략 가져야 함.
5. 고민감 산업은 먼저 클라우드 AI / Hybrid / 완전 온프레 배포 모드 결정해야 함.
6. 메모리와 개인화 기능은 프라이버시, 삭제, 데이터 보존 정책 필요.
7. Public Chatbots 또는 외부 액세스는 L1 에서 광범위하게 개방하면 안 됨; 별도 PoC 필요.
8. 각 버전 업데이트는 Admin Runbook 과 사용 가이드라인을 새로 고쳐야 함.
