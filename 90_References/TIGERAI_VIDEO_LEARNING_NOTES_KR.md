# TigerAI 채널 영상 학습 노트와 L3 적용 요약

> 🌐 언어: [繁體中文](TIGERAI_VIDEO_LEARNING_NOTES.md) ｜ [English](TIGERAI_VIDEO_LEARNING_NOTES_EN.md) ｜ [Deutsch](TIGERAI_VIDEO_LEARNING_NOTES_DE.md) ｜ [Français](TIGERAI_VIDEO_LEARNING_NOTES_FR.md) ｜ [Español](TIGERAI_VIDEO_LEARNING_NOTES_ES.md) ｜ [日本語](TIGERAI_VIDEO_LEARNING_NOTES_JA.md) ｜ 한국어

버전: v1.0
저자: Morris Lu (盧業興) · Tiger AI 虎智科技
채널: 虎智科技 TigerAI
오리지널 채널: `https://www.youtube.com/@%E8%99%8E%E6%99%BA%E7%A7%91%E6%8A%80TigerAI`

---

## 1. 본 문서 사용법

본 문서는 L1-L4 코스 설계에 사용 가능한 TigerAI 채널 영상을 조직, 특히 n8n 과 L3 Workflow Automation 에 집중.

조직 접근:

1. 공개적으로 이용 가능한 영상 카탈로그와 제목 기반 학습 요약 구축.
2. 영상을 L1 / L2 / L3 / L4 코스 사용에 매핑.
3. n8n 영상을 L3 코스 모듈과 PoC 로드맵으로 조직.
4. OpenGenie 영상을 기업 거버넌스, 계정, 권한, 모델, Prompts, Channels, n8n 통합, RAG/Vision, 피드백 시스템 다루는 채택 스레드로 조직.

우선순위:

| 우선순위 | 설명 |
|---|---|
| P0 | L3 n8n 핵심 코스 필수 |
| P1 | L1 / L2 / L3 / L4 의 중요 지원 콘텐츠 |
| P2 | 산업- 또는 부서-특정 선택 케이스 |
| P3 | 데모 또는 영감 케이스 |

---

## 2. L3 코스 전체 결론

TigerAI n8n 영상은 단순히 도구 튜토리얼이 아님; 완전한 기업 프로세스 자동화 케이스 라이브러리. 그들이 드러내는 L3 훈련 로직은:

> L2 가 생성한 Skill / Workflow Blueprint 가 끝난 지점부터 이어받아, n8n 을 사용해 실행 가능, 검증 가능, 백업 가능, 운영 가능, 플랫폼 간 통합 가능한 프로세스 PoC 로 전환.

따라서 L3 코스는 강조해야:

1. Trigger: Webhook, schedule, Gmail, LINE, Facebook, YouTube, GCS / API event.
2. Data Handling: Data Tables, Sheets, BigQuery, CRM / ERP / API data.
3. AI Processing: Gemini, 이미지, 오디오, 영상, 문서, 카피라이팅, 요약, 분류.
4. Platform Integration: LINE, Facebook, YouTube, 소셜 플랫폼, Gmail, GitHub.
5. Reuse: Sub-workflow 모듈화.
6. Governance: Credentials, Execution Log, GitHub backup, human review, error handling.
7. L4 Readiness: Hermes Agent 가 미래에 n8n Workflows 호출 가능하게.

---

## 3. OpenGenie Enterprise Governance 영상 요약

| # | 영상 | 학습 요약 | 코스 적용 | 우선순위 |
|---:|---|---|---|---|
| OG-1 | [TigerAI OpenGenie 單元 1：帳號體系與權限佈署](https://www.youtube.com/watch?v=wkgx94TmFE4) | 계정, 사용자, 권한 배포. | L1 OpenWebUI / OpenGenie 기업 enablement; 개인별 계정과 권한 거버넌스 다룸. | P1 |
| OG-2 | [單元 2：後端模型 Ollama 管理與安裝](https://www.youtube.com/watch?v=fyK8lIBEdoU) | 백엔드 모델 설치와 관리. | L1 IT / Admin 모델 관리; 클라우드 AI / Hybrid / 완전 온프레 결정 지원. | P1 |
| OG-3 | [單元 3：API Key 彈性配置](https://www.youtube.com/watch?v=IdI_pqRjEOU) | API Key 와 클라우드 어시스트 전략. | L1/L3 IT; 모델 제공자, 외부 API, 권한 관리. | P1 |
| OG-4 | [單元 4：Prompts 專家設定](https://www.youtube.com/watch?v=CZwXcgtKn0Y) | 전문가 Prompt 설정. | L1 Prompt Library; L2 Skill 화. | P1 |
| OG-5 | [單元 5：群組與協作權限深度管理](https://www.youtube.com/watch?v=G1MKa10W6K0) | 그룹과 협업 권한. | L1 Admin / L3 프로세스 권한 설계. | P1 |
| OG-6 | [單元 6：Channels 協作與會議摘要](https://www.youtube.com/watch?v=38kkwwRDOpU) | Channels, 협업, 회의 요약. | L1 부서 협업, L2 회의 요약 Skill, L3 회의 흐름. | P2 |
| OG-7 | [單元 7：n8n 串接與自動化工作流](https://www.youtube.com/watch?v=xX6e0l-TaWg) | OpenGenie 와 n8n 통합; 자동화 워크플로. | L3 메인 코스의 핵심, L3 진입 영상으로 작동. | P0 |
| OG-8 | [單元 8：多模態進階應用 RAG & Vision](https://www.youtube.com/watch?v=qN_2KSgbjUM) | RAG, Vision, 멀티모달 응용. | L3 Gemini / 멀티모달 흐름; L4 Hermes 지식 작업 전구체. | P1 |
| OG-9 | [單元 9：綜合應用與分享機制](https://www.youtube.com/watch?v=jQPBSZmYLbg) | 통합 응용, 공유, 협업. | L1/L3 공유 거버넌스와 데모 쇼케이스. | P2 |
| OG-10 | [單元 10：管理監督與回饋系統](https://www.youtube.com/watch?v=4Lrgg-vdhi8) | 관리 감독과 피드백. | L3 운영, 피드백, 품질 향상, Gate 3 수락. | P1 |

---

## 4. Antigravity / L2 영상 요약

| # | 영상 | 학습 요약 | 코스 적용 | 우선순위 |
|---:|---|---|---|---|
| AG-1 | [1部曲：AI 全自動寫代碼、測試還幫你錄影](https://www.youtube.com/watch?v=LCO700FzoXg) | Antigravity 기반; AI 가 코드 작성, 테스트, 증거 녹화. | L2 Antigravity Foundation. | P1 |
| AG-2 | [2部曲：AI 寫 Code 鬼打牆怎麼辦](https://www.youtube.com/watch?v=RRWtnqqQI0E) | 디버깅 마인드셋; Skill 플러그인 확장. | L2 Debug / Skill 화. | P1 |
| AG-3 | [3部曲：開發環境零手動](https://www.youtube.com/watch?v=kHywZFPsju8) | AI 가 패키지와 UI 설치. | L2 엔지니어링 실천. | P1 |
| AG-4 | [4部曲：爬蟲與架站](https://www.youtube.com/watch?v=K4UMhFj9ztE) | 데이터 스크래핑과 커스텀 Web UI. | L2 앱 프로토타입; L3 가 여기서 데이터 흐름 이어받기 가능. | P1 |
| AG-5 | [5部曲：Docker 容器化與打包](https://www.youtube.com/watch?v=IILRXP2cMbo) | Docker 컨테이너화. | L2 엔지니어링 산출물과 L3 배포 전구체. | P1 |
| AG-6 | [6部曲：互動 App 與個人專屬 Skill](https://www.youtube.com/watch?v=q9rNgnqNXlc) | 인터랙티브 App 과 개인 Skill 구축. | L2 Skill Library 와 L2-에서-L3 다리. | P1 |

---

## 5. n8n / L3 영상 요약

| # | 영상 | 학습 요약 | L3 코스 적용 | 우선순위 |
|---:|---|---|---|---|
| N27 | [不寫程式也能用 Gemini：n8n 整合 Google Gemini 全攻略](https://www.youtube.com/watch?v=DT5Gx5tMxGs) | n8n 을 사용해 Gemini 를 이미지, 오디오, 영상, 문서용으로 통합. | L3 AI Node / 멀티모달 처리 기반. | P0 |
| N28 | [n8n 進階教學：Sub-workflow 模組化自動化術](https://www.youtube.com/watch?v=hbvHwjrexds) | 재사용 가능한 Sub-workflows 구축. | L3 모듈화와 프로세스 표준화 필수. | P0 |
| N29 | [AI 即時查詢神器：高鐵時刻查詢機器人](https://www.youtube.com/watch?v=T1hzDrIhHSk) | 일정, 요금, 시간표용 LINE 자동 답장. | Webhook / LINE / API 쿼리 흐름 케이스. | P0 |
| N30 | [AI 人資革命：自動履歷篩選系統](https://www.youtube.com/watch?v=EgSFZm6hvE8) | n8n + Gemini + Gmail + LINE HR 프로세스. | HR 프로세스 PoC: 이력서 접수, AI 스크리닝, 알림. | P0 |
| N31 | [史上最強社群自動化](https://www.youtube.com/watch?v=Eb-DwLnNjUk) | 제품 이미지에서 영상, 카피라이팅, 다중 플랫폼 마케팅. | 마케팅 자동화 PoC. | P2 |
| N32 | [AI 自動發文 2.0](https://www.youtube.com/watch?v=hlhByT2m28M) | 영상 생성, 카피라이팅, 다중 플랫폼 게시. | 소셜 게시 Workflow; human review Gate 필요. | P2 |
| N33 | [YouTube AI 留言機器人](https://www.youtube.com/watch?v=3cB4BtGUA9w) | YouTube 자동 답장 댓글과 키워드 인터랙션. | 소셜 인터랙션과 고객 서비스 흐름. | P2 |
| N34 | [n8n 終極備份術](https://www.youtube.com/watch?v=zrsE4-G6MRY) | Workflows + Credentials 를 GitHub 로 자동 동기화. | L3 운영, 백업, 버전 거버넌스 필수. | P0 |
| N35 | [Facebook 聊天機器人實戰](https://www.youtube.com/watch?v=c9VuLN_DasA) | n8n + Webhook 으로 Facebook AI 고객 서비스 봇 구축. | 고객 서비스 자동화 주요 케이스. | P0 |
| N36 | [Data Tables 實戰：Facebook 智能客服](https://www.youtube.com/watch?v=v4plNZNSG08) | n8n Data Tables, Meta 플랫폼 통합, 커스텀 AI 답장. | L3 Data Tables 와 state 관리 필수. | P0 |
| N37 | [AI 客服升級版：FB 粉專自動回圖、回訊息](https://www.youtube.com/watch?v=pEWn2yh1Dkg) | Facebook 고객 서비스용 이미지와 메시지 답장. | 선택적 멀티모달 고객 서비스. | P2 |
| N38 | [AI 自動行銷機器人](https://www.youtube.com/watch?v=njcKlnhEaUM) | Freepik + DataForSEO: 자동 이미지 소싱, 카피라이팅, 키워드 선택, 게시. | 마케팅 콘텐츠 공급망 흐름. | P2 |
| N39 | [Sora 2 全自動影片工廠](https://www.youtube.com/watch?v=3NJZ99lY8kU) | n8n + Kie AI: 원클릭 영상 생성과 FB, IG, Threads, YouTube 로 게시. | 고급 영상 공장 케이스; review 와 brand Gates 필요. | P3 |

---

## 6. L3 코스 설계 함의

### 6.1 n8n 기초만 가르칠 수 없음

TigerAI 영상은 L3 에서 진정으로 가치있는 것은 「노드 드래그」 가 아니라, 프로세스에서 완전한 폐쇄 루프 형성:

`Trigger → Data → AI → System Action → Human Gate → Log → Backup → Reuse`

### 6.2 L3 는 네 케이스 풀 가져야 함

| 케이스 풀 | 대표 영상 | 적합 고객 |
|---|---|---|
| 고객 서비스 자동화 | N35, N36, N37 | 서비스, e-commerce, 팬 페이지, 고객 서비스 센터 |
| HR 자동화 | N30 | HR, 채용, HR 공유 서비스 |
| 마케팅 자동화 | N31, N32, N33, N38, N39 | 마케팅, 콘텐츠, 소셜, 브랜드 |
| 쿼리 / 유틸리티 봇 | N29 | 운영, 고객 서비스, 내부 쿼리 |

### 6.3 L3 는 거버넌스 코스 추가해야

영상 N34 의 GitHub 백업은 매우 중요하며 L3 의 필수 부분이어야 함, 선택 아님. 기업이 n8n 채택 후, 백업, 버전 관리, 자격 증명 관리, Execution Log, 오류 알림 없이는, PoC 가 쉽게 유지 불가능한 장난감이 됨.

---

## 7. 권장 시청 경로

### 7.1 L3 Core Track

1. OG-7: OpenGenie 와 n8n 통합.
2. N27: n8n + Gemini 멀티모달.
3. N28: Sub-workflows.
4. N34: GitHub 백업.
5. N35: Facebook Webhook 고객 서비스.
6. N36: Data Tables.

### 7.2 Customer Service Track

1. N35.
2. N36.
3. N37.
4. OG-10.

### 7.3 HR Track

1. N30.
2. OG-4.
3. OG-6.
4. N34.

### 7.4 Marketing Track

1. N31.
2. N32.
3. N33.
4. N38.
5. N39.

### 7.5 IT / Operations Track

1. OG-1.
2. OG-3.
3. OG-5.
4. N28.
5. N34.
6. OG-10.

---

## 8. 딜리버리에 적용

TigerAI 영상은 다음 산출물로 전환해야:

- L3 n8n Workflow Blueprint.
- n8n Workflow JSON.
- Credential / API / Webhook 권한 시트.
- Data Tables 스키마.
- Sub-workflow Library.
- Execution Log 와 테스트 기록.
- GitHub 백업과 버전 관리 SOP.
- Human Gate 설계.
- Error Handling / Retry / Fallback 설계.
- L4 Hermes Agent 가 호출 가능한 Workflows 리스트.
