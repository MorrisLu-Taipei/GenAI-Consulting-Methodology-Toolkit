# GenAI Consulting Methodology Toolkit

ภาษา: [繁體中文](README.md) | [English](README_EN.md) | ภาษาไทย | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [日本語](README_JA.md) | [한국어](README_KR.md)

ชุดเครื่องมือสำหรับการประเมินความพร้อมและการนำ AI ไปใช้ในการเปลี่ยนผ่านองค์กร (Enterprise AI Transformation Maturity Assessment & Implementation Methodology Toolkit)

ผู้สร้าง: **Tiger AI Morris Lu 盧業興**  
ตำแหน่ง: **n8n Taipei Ambassador / นักศึกษาปริญญาเอก สถาบัน Intelligent Manufacturing, National Taiwan University of Science and Technology / M.IT, Queensland University of Technology (QUT), ออสเตรเลีย**

สรุปลิขสิทธิ์: โครงการนี้ใช้ **[Apache License 2.0](LICENSE)** สามารถใช้งาน คัดลอก แก้ไข เผยแพร่ซ้ำ และนำไปใช้เชิงพาณิชย์ได้อย่างอิสระ เมื่อเผยแพร่ซ้ำ โปรดเก็บข้อความลิขสิทธิ์ Apache 2.0 และการระบุชื่อผู้สร้างใน [`NOTICE`](NOTICE) ไว้

> **มีเวลาแค่ 5 นาที?** เริ่มจาก [`00_Overview/EXECUTIVE_SUMMARY_EN.md`](00_Overview/EXECUTIVE_SUMMARY_EN.md) — สรุปทั้งระเบียบวิธีในหน้าเดียว

---

## 🌟 นี่ไม่ใช่แค่หนังสือ แต่คือ AI-Native Living Book — หนังสือที่ "มีชีวิต" จริงๆ

หนังสือได้วิวัฒนาการมาตลอด แต่ละยุคแก้โจทย์ได้อย่างหนึ่ง แต่ก็ทิ้งช่องว่างไว้อย่างหนึ่ง — **ไม่เคยเป็นหนังสือที่ "มีชีวิต" เลย**:

- **ยุคที่ 1 — หนังสือพิมพ์ (Printed Books)**: เก็บความรู้และส่งต่อให้ผู้อ่านคนต่อไป แต่ **อ่านได้อย่างเดียว ตอบกลับไม่ได้** ตอบคำถามคุณไม่ได้ และไม่รู้ว่าบริษัทคุณเป็นยังไง — เป็นเพียง **กระดาษที่หยุดนิ่ง**
- **ยุคที่ 2 — หนังสือแบบ Interactive (Interactive Books)**: เมื่อย้ายขึ้นเว็บและ Wiki ก็ค้นหาได้ คลิกได้ คอมเมนต์ได้ มี "การโต้ตอบ" มากกว่าหนังสือพิมพ์ แต่ยัง **ไม่แนะนำอะไรให้คุณก่อน** ไม่วิเคราะห์ ไม่ผลิตของใหม่ — ยังคงเป็น passive อยู่ดี อินเทอร์เฟซมีชีวิตแต่เนื้อหายังไม่
- **ยุคที่ 3 — AI-Native Book (repo นี้) — หนังสือที่ "มีชีวิต" จริงๆ**: เขียนระเบียบวิธีในรูป Markdown แล้วเปิดด้วย AI IDE — AI อ่านทั้งเล่มอัตโนมัติ **ให้คุณถาม ตอบให้คุณ คิดไปกับคุณ** และให้ **คำแนะนำที่ปรับให้เข้ากับสภาพจริงของบริษัทคุณ ทำการวินิจฉัย ร่างรายงาน รันการจำลองสถานการณ์** หนังสือเองตอบสนอง ขยายตัว และเติบโตบทใหม่ตามคำถามของคุณ

อีกนัยหนึ่ง: หนังสือพิมพ์ส่งต่อความรู้ หนังสือ Interactive ทำให้ค้นหาได้ — **AI-Native Book ทำให้ "หนังสือ" มีชีวิตจริงๆ เป็นครั้งแรก กลายเป็นคู่คิดที่นั่งคิดไปด้วยกัน** การตัดสินใจสุดท้ายยังคงเป็นของมนุษย์ แต่คุณไม่ได้เผชิญหน้ากับระเบียบวิธีที่หยุดนิ่งคนเดียวอีกต่อไป

> *Three generations of books: printed (read-only, dead) → interactive (search & link, still passive) → **AI-native (truly alive — advises, analyzes, simulates, and grows with your questions)**. Open with an AI IDE; AI becomes your reading partner, consulting assistant, and auditor.*

### 🔱 สาม AI Engine ที่เชี่ยวชาญต่างกัน

เนื้อหาเดียวกัน เมื่อเปิดด้วย AI IDE ที่แตกต่างกัน จะแสดง **บุคลิกที่แตกต่างกันโดยสิ้นเชิง**:

| Engine | บทบาท | สิ่งที่เก่งที่สุด |
| --- | --- | --- |
| 🟦 **Antigravity** | ที่ปรึกษาแนวหน้า | คุยกับลูกค้า รันแบบสอบถาม ร่างรายงาน |
| 🟪 **Codex CLI** | ผู้ตรวจสอบระเบียบวิธี | ทดสอบข้ามไฟล์ red-team review ควบคุมเวอร์ชัน ซ่อมแซมลิงก์ที่ขาด |
| 🟨 **Claude Code** | คู่คิดข้ามไฟล์ | สังเคราะห์เชิงลึก โต้แย้งหลายมุมมอง จำลองสถานการณ์ Fork สำหรับลูกค้าเฉพาะ |

สาม engine ไม่แทนที่กัน แต่ **แบ่งงานกัน**: เช้าใช้ Antigravity ประชุมลูกค้า บ่ายใช้ Codex ตรวจร่างรายงาน เย็นใช้ Claude Code รันการจำลองสถานการณ์ พื้นที่ทำงานของแต่ละ engine แยกกัน (`.agent/` / `.codex/` / `.claude/`) ไม่รบกวนกัน

รายละเอียดของแต่ละ engine ดูได้ที่ [`07_AI_Contributions/`](07_AI_Contributions/); ขั้นตอนติดตั้งดูได้ใน [คู่มือติดตั้งและเริ่มใช้สาม AI Engine](#-คู่มือติดตั้งและเริ่มใช้สาม-ai-engine--three-ai-engines-setup-guide) ด้านล่าง

### สำหรับผู้อ่านแต่ละบทบาท สิ่งนี้หมายถึงอะไร

- **CEO / ผู้บริหารระดับสูง**: โยน repo นี้เข้า ChatGPT / Claude / Gemini ถาม-ตอบ 10 นาทีจะได้คำตอบเบื้องต้นว่า "บริษัทผมอยู่ระดับไหน? ควรเริ่มจากอะไร?"
- **ที่ปรึกษา / ผู้เรียน**: เปิดด้วย AI IDE สามารถรันประสบการณ์ที่ปรึกษาแบบสนทนาครบชุด — ตั้งแต่การวินิจฉัย การทำรายงาน ไปจนถึง Roadmap 24 เดือน
- **นักวิชาการ / นักวิจัย**: รัน `/devil-pair-debate`, `/thought-experiment` โดยตรงเพื่อโต้แย้งสมมติฐานเชิงค่านิยมของระเบียบวิธี โดยมีเสาทฤษฎี 7 ต้นและ classics 28 ฉบับให้อ้างอิง
- **กำกับดูแล / Compliance**: รัน `/evidence-audit`, `/generate-traceability` เพื่อให้ได้ห่วงโซ่หลักฐานที่ตรวจสอบได้ และสอดคล้องกับ NIST AI RMF / EU AI Act / ISO 42001

> ⚠️ **เปิดเผยตามตรง**: สถาปัตยกรรมระเบียบวิธีโดยรวมออกแบบโดย **Morris Lu (มนุษย์)** สาม AI engine เป็นเพียงเครื่องมือสำหรับการดำเนินงาน ขยายความ และตรวจสอบเท่านั้น รายละเอียดดู [`07_AI_Contributions/README.md`](07_AI_Contributions/README.md) §0 — กรณีศึกษาทั้งหมดในหนังสือเป็นการสร้างจำลองด้วย AI เพื่อการสอน **ไม่ใช่ข้อมูลลูกค้าจริง**

---

## ระเบียบวิธีนี้แก้โจทย์อะไร

หลายองค์กรเริ่มนำ AI มาใช้ด้วยการกระโดดเข้าไปที่เครื่องมือทันที — วันนี้ซื้อ ChatGPT พรุ่งนี้ลอง n8n สัปดาห์หน้าอยากทำ Agent ปัญหาที่พบบ่อยคือพนักงานใช้ไม่เป็น กระบวนการไม่เชื่อมต่อ ข้อมูลไม่ถูกกำกับดูแล PoC ผ่านการยอมรับไม่ได้ และสุดท้ายผู้บริหารก็ไม่รู้ว่า AI ขององค์กรอยู่ที่ระดับใด

กลยุทธ์ของชุดเครื่องมือนี้คือ: ใช้แบบสอบถามง่ายๆ เพื่อวินิจฉัยระดับความพร้อม AI ขององค์กรในปัจจุบันก่อน แล้วออกแบบสัดส่วนหลักสูตรและเส้นทางการนำไปใช้ตาม L1-L5 หลักสูตรไม่ใช่แค่เรียนจบแล้วจบ แต่ในทุกระดับจะมีผลส่งมอบที่ตรวจสอบได้ และสุดท้ายใช้กระบวนการ 8 ขั้นตอนของการวินิจฉัย AI Transformation เพื่อผลิตรายงานการวินิจฉัยที่ปรึกษาที่สมบูรณ์ Roadmap ROI และคำแนะนำด้านการกำกับดูแล

## จินตนาการอนาคตก่อนเริ่มหลักสูตร

ก่อนที่ลูกค้าจะตัดสินใจเรียนหลักสูตร L1-L5 สิ่งที่จำเป็นที่สุดคือต้องเห็นภาพอนาคตก่อน: ไม่ใช่ "เราจะเรียนเครื่องมือห้าตัว" แต่เป็น "**หลังเรียนจบ งานประจำวันของบริษัทจะเปลี่ยนยังไง?**"

แกนเรื่องคือ **ขนาดขยายทีละชั้น และในที่สุดเติบโตจาก 'มนุษย์ใช้ AI' กลายเป็น 'AI ทำงานเอง'**: **บุคคล → แผนก → ข้ามแผนก/ทั้งบริษัท → AI Super-Assistant (Entity) → AI Team** จินตนาการถึงเช้าวันจันทร์อีกสามเดือนข้างหน้า:

- **L1 Controlled AI Access ─ Scale Axis · บุคคล**: **พนักงานแต่ละคน** เข้าระบบ OpenWebUI ด้วยบัญชีของตัวเอง มีพื้นที่แชท ประวัติการใช้งาน และสิทธิ์ตามแผนก ฝ่ายขายเขียนอีเมลลูกค้า HR สรุปการอบรม ผู้จัดการสรุปประชุม — ทั้งหมดเริ่มจากจุดเข้า AI ที่ควบคุมจุดเดียวกัน **หน่วยคือ "บุคคล"** AI อยู่ข้างคนแต่ละคน
- **L2 Knowledge Codification ─ Scale Axis · แผนก**: **หน่วยขยายเป็น "แผนก"** พนักงานอาวุโสไม่ใช่แค่ตัวคนเดียวเก่ง แต่ใช้ **ความรับผิดชอบของแผนกเป็นขอบเขต** จัดระเบียบ copywriting รายงาน คำตอบ customer service การตีความ SOP วิธีพัฒนาโปรแกรม ให้เป็น Skill ที่ใช้ซ้ำได้ พนักงานใหม่และคนในแผนกเดียวกันใช้วิธีเดียวกัน คุณภาพผลผลิต **ทั้งแผนก** เริ่มสม่ำเสมอ
- **L3 Workflow Automation ─ Scale Axis · ข้ามแผนก / ทั้งบริษัท**: **หน่วยขยายขึ้นอีกเป็น "ข้ามแผนก ทั้งบริษัท"** n8n เชื่อม Skill ของแต่ละแผนกเข้ากับระบบ (Gmail, Sheets, Notion, CRM, API, ERP) อีเมลร้องเรียนลูกค้าหนึ่งฉบับที่เข้ามา สามารถ **ข้าม Sales, Customer Service, CRM, ผู้จัดการหลายแผนก** อย่างอัตโนมัติ — ระบบสืบค้น CRM อัปเดตแบบฟอร์ม สร้างงาน สรุปให้ผู้จัดการ คนรับผิดชอบแค่ตัดสินใจและอนุมัติ AI เริ่มเข้าสู่ **กระบวนการทั้งบริษัท**
- **L4 Autonomous Agent ─ AI-Autonomy Axis · Super-Assistant (AI Entity)**: **นอกจากกองทัพมนุษย์ บริษัทก็เริ่มมี AI Entity เพิ่มขึ้นมา** Hermes Agent อ่านงาน เอกสาร ผลของ Workflow และความจำใน Wiki ทุกวัน แล้วผลิต briefing รายการติดตาม และจุดตัดสินใจที่ต้องการ HITL (Human-in-the-Loop, มนุษย์รีวิวใน loop) บริษัทเริ่มมี **AI Entity แบบ knowledge-grade ที่ตรวจสอบได้** เหมือนจ้าง super-assistant อัตโนมัติเต็มรูปแบบเพิ่มขึ้นอีกคน
- **L5 Multi-Agent Organization ─ AI-Autonomy Axis · AI Team**: **AI Entity หลายตัวจัดเป็น "AI Team"** ClawTeam รวม Agent ของ Marketing, Product, Customer Service, Finance, Operations เป็นทีมแบ่งหน้าที่ ทำงานร่วมกันเพื่อ launch สินค้าใหม่ ปรับปรุงคุณภาพ ปรับปรุงบริการผู้ป่วย หรือดูแลลูกค้า — บริษัทมี **สองทีมพร้อมกัน: ทีมมนุษย์ + ทีม AI**

เรื่องเล่านี้ต้องเล่าก่อนเริ่มหลักสูตร เมื่อลูกค้าเข้าใจ "**ขนาดขยายตัวยังไง AI เติบโตจากเครื่องมือเป็นกำลังคนดิจิทัลยังไง**" แล้วค่อยกลับมาเข้าใจว่าทำไมต้องมีการวินิจฉัยด้วยแบบสอบถาม ทำไมหลักสูตรต้องแบ่ง L1-L5 ทำไมทุกระดับต้องมี deliverables, evidence และ Stage Gate

> ⚠️ คำอธิบายสองแกนที่ละเอียดกว่า (ทำไม L3 → L4 เป็นเส้นแบ่งสำคัญ ทำไมการกำกับดูแลยังเป็นของมนุษย์เสมอ) ดูได้ใน [§สองแกนของ L1-L5](#สองแกนของ-l1-l5) ด้านล่าง

## แผนที่ความพร้อม AI

![AI Maturity Map](90_References/MD-Map.png)

## ภาพรวมระเบียบวิธี

![Enterprise Consulting Methodology: Eight-Stage Transformation Guide](90_References/Metholodgy.png)

## เรื่องเล่าหลัก

```text
แบบสอบถามความพร้อม AI
→ สำรวจคุณสมบัติบริษัท สถานการณ์อุตสาหกรรม รูปแบบการ deploy
→ ออกแบบสัดส่วนหลักสูตร L1-L5
→ L1 เปิดใช้บัญชี OpenWebUI องค์กรและพื้นที่แชทส่วนบุคคล
→ L2 ฝึก Skill กับ Antigravity / Claude Code / Codex
→ L3 ใช้ n8n เชื่อม Gmail, Sheets, Notion, CRM, API, ERP และระบบอื่น
→ L4 สร้าง Hermes Agent ที่ตรวจสอบได้สำหรับงานอัตโนมัติ
→ L5 จัดทีม Agentic ด้วย ClawTeam
→ กรณีศึกษา หลักฐาน Stage Gate
→ การวินิจฉัย 8 ขั้นตอน AI Transformation
→ รายงานการวินิจฉัย AI Transformation, Roadmap, ROI, คำแนะนำการกำกับดูแล
```

## โมเดลความพร้อม L1-L5

| ระดับ | ชื่อ | เครื่องมือ / แพลตฟอร์ม | แกน | ตำแหน่งในองค์กร |
| --- | --- | --- | --- | --- |
| L1 | Controlled AI Access | OpenWebUI | Scale Axis · บุคคล | สร้างจุดเข้า AI ภายในองค์กร ให้พนักงานแต่ละคนมีบัญชี พื้นที่แชท และขอบเขตสิทธิ์ของตัวเอง |
| L2 | Knowledge Codification | Antigravity / Claude Code / Codex | Scale Axis · แผนก | ใช้ความรับผิดชอบของแผนกเป็นหน่วย จัดระเบียบความรู้ส่วนบุคคล prompt เอกสาร และวิธีการทำงานเป็น Skill ที่ใช้ซ้ำได้ |
| L3 | Workflow Automation | n8n | Scale Axis · ข้ามแผนก / ทั้งบริษัท | เชื่อม Skill ข้ามแผนกและเชื่อมกับ email, Sheets, Notes, CRM, API, ERP และระบบอื่น ให้ AI เข้าสู่กระบวนการอัตโนมัติทั้งบริษัท |
| L4 | Autonomous Agent | Hermes Agent | AI-Autonomy Axis · Super-Assistant | รวม Wiki capability map, AI tools, Workflow, scheduling, autonomous learning เป็น AI Agent Super-Assistant อัตโนมัติเต็มรูปแบบที่ตรวจสอบได้ |
| L5 | Multi-Agent Organization | ClawTeam | AI-Autonomy Axis · AI Team | ให้ Agent หลายตัวแบ่งหน้าที่กัน ทำงานร่วมกันในงานองค์กรที่ข้ามแผนก ข้ามกระบวนการ ในรูปแบบ AI Team |

### สองแกนของ L1-L5

L1-L5 ไม่ใช่ "เครื่องมือห้าตัว" แต่เป็นเส้นทางความพร้อมที่เชื่อมด้วย **สองแกน**:

- **L1 → L2 → L3: Scale Axis (มนุษย์ใช้ / กำกับดูแล AI)** สามชั้นนี้คือช่วงของ "มนุษย์อยู่ใน loop, มนุษย์ใช้ AI, มนุษย์กำกับดูแล AI" ขยายตามขนาดองค์กรไปทีละชั้น — **L1 บุคคล** (พนักงานแต่ละคนใช้ AI เอง) → **L2 แผนก** (ใช้ความรับผิดชอบของแผนกเป็นหน่วย ห่อความรู้ส่วนบุคคลเป็น Skill ที่ใช้ซ้ำได้) → **L3 ข้ามแผนก / ทั้งบริษัท** (เชื่อม Skill ข้ามแผนกและเชื่อมกับระบบ ให้ AI เข้าสู่กระบวนการอัตโนมัติทั้งบริษัท)
- **L4 → L5: AI-Autonomy Axis (AI ทำงานเอง ไม่ต้องมนุษย์กำกับแบบ real-time)** สองชั้นนี้คือ AI Entity ที่บริษัท "**สร้างเพิ่ม**" นอกเหนือจากกองทัพมนุษย์ — **L4 AI Super-Assistant** (AI Agent Entity อัตโนมัติเต็มรูปแบบ) → **L5 AI Team** (Agent หลายตัวแบ่งหน้าที่ทำงานร่วมกัน)

> เส้นแบ่งสำคัญ: **L1-L3 คือ "มนุษย์ช่วย / กำกับดูแล AI" AI เป็นเครื่องมือ; L4-L5 คือ "AI ทำงานเอง" AI เป็นกำลังคนดิจิทัลเพิ่มเติม** ตามลำดับการนำมาใช้ L1-L3 ต้องทำให้คนและองค์กรพร้อมก่อน L4-L5 จึงจะเติบโตบนรากฐานที่มั่นคงได้
>
> แม้จะถึง L4-L5 **กรอบการกำกับดูแลยังคงสร้างโดยมนุษย์ มนุษย์ยังคงมีสิทธิ์กำกับดูแล** — สิ่งที่ AI ทำเองคือ "การดำเนินงาน" ไม่ใช่ "การตัดสินใจเชิงกำกับดูแล" ทุกระดับยังคงรักษา HITL (Human-in-the-Loop) และ Stage Gate ไว้ ยิ่ง AI ทำงานเองมากขึ้น บทบาทของมนุษย์ก็ยกระดับขึ้นเป็น "ผู้กำกับดูแล" มากขึ้น ไม่ถูกแทนที่

## วิธีการยอมรับในแต่ละระดับ

| ระดับ | Input | Process | Output | Evidence | Stage Gate |
| --- | --- | --- | --- | --- | --- |
| L1 | บทบาทพนักงาน งานที่พบบ่อย จุดเจ็บปวด ความต้องการสิทธิ์ | ตั้ง OpenWebUI, บัญชี / กลุ่ม / สิทธิ์, พื้นที่แชทส่วนบุคคล, ฝึก Prompt พื้นฐาน | จุดเข้า AI องค์กร, รายการ Prompt, รายการ use case | ตารางบัญชี, ตารางสิทธิ์, log การ login, screenshot พื้นที่แชท, ตัวอย่าง Prompt | สามารถ login ปลอดภัย แยกสิทธิ์ และเก็บ log ที่ติดตามได้หรือไม่ |
| L2 | Prompt ที่ใช้บ่อยจาก L1, เอกสาร, SOP, วิธีการทำงานส่วนตัว | ใช้ Antigravity / Claude Code / Codex ห่อความรู้เป็น Skill และ artifact ที่ใช้ซ้ำได้ | Skill Library, Agentic artifacts, Workflow Blueprint | เอกสาร Skill, test case, version history, ตัวอย่างผลลัพธ์ | Skill สามารถถูกใช้ซ้ำโดยคนอื่นและผลิตผลลัพธ์ที่เสถียรหรือไม่ |
| L3 | Skill จาก L2, blueprint กระบวนการ, รายการระบบ, สิทธิ์ API / CRM / ERP / Sheet | ใช้ n8n สร้าง workflow อัตโนมัติ, Data Table, Execution Log, การจัดการ error | Workflow PoC, Sub-workflow Library, Data Tables, L4 Workflow Contract | n8n workflow, execution log, log การ retry หลัง fail, screenshot การเชื่อมระบบ | Workflow สามารถรันเสถียรบนข้อมูลจริงและระบบจริงหรือไม่ |
| L4 | Workflow จาก L3, Skill จาก L2, Wiki องค์กร, กฎของ task, จุด HITL | ใช้ Hermes Agent สร้าง task card, Wiki ingest/query/update, scheduling, การเรียกใช้ tool และ Gate 4A-4E | Agent ที่ตรวจสอบได้, Briefing, log การจัดการ task, ลายเซ็น sign-off | Agent log, version ของ Wiki, task card, briefing, บันทึกการอนุมัติของมนุษย์ | Agent สามารถทำ task อัตโนมัติในขอบเขตที่ควบคุมและทิ้ง evidence ไว้หรือไม่ |
| L5 | L4 Agent หลายตัว, task ข้ามแผนก, ความรับผิดชอบบทบาท, กฎการกำกับดูแล | ใช้ ClawTeam จัด Agentic Team, กำหนดบทบาท กฎการทำงานร่วม การส่งต่อและการกำกับดูแล | Agent Team, role card, flow การทำงานร่วม, ผลข้ามแผนก | Team run log, role card, log การส่งต่อ, เอกสารผลลัพธ์, log การกำกับดูแล | Agent Team สามารถทำงานร่วมเสถียรและผลิตผลที่ติดตามความรับผิดชอบได้หรือไม่ |

## หลักการออกแบบหลักสูตร

สัดส่วนหลักสูตรกำหนดโดยความพร้อม อุตสาหกรรม รูปแบบ deploy และสถานการณ์เป้าหมายของลูกค้า ไม่ใช่ทุกบริษัทต้องเรียนครบ L1-L5 ในครั้งเดียว แต่หาชั้นที่สามารถสร้างผลส่งมอบได้ทันทีที่สุดก่อน แล้วต่อยอดขึ้นไป

| มิติการสำรวจ | วัตถุประสงค์ |
| --- | --- |
| คุณสมบัติบริษัท | ตัดสินว่าเป็นโรงงานวิจัยและผลิต บริการการตลาด สถานพยาบาล หน่วยงาน operation ภายใน หรือประเภทอื่น |
| รูปแบบ Deploy | ตัดสินว่าใช้ cloud AI, Hybrid, หรือ on-prem เต็มรูปแบบ |
| สถานะระบบปัจจุบัน | สำรวจ Gmail, Sheets, Notion, CRM, API, ERP, database และระบบภายใน |
| ความพร้อมของกระบวนการ | ตัดสินว่ามี SOP, process owner, data field, exception handling แล้วหรือไม่ |
| ข้อกำหนดความเสี่ยง | ประเมินความปลอดภัย ความเป็นส่วนตัว compliance ทางการแพทย์ / การผลิต / การเงิน และความต้องการ sign-off ของมนุษย์ |

## โครงสร้างไดเรกทอรี

| ไดเรกทอรี | วัตถุประสงค์ |
| --- | --- |
| [`00_Overview`](00_Overview/) | บทสรุปโซลูชัน เรื่องเล่าหลัก WBS |
| [`01_Assessment`](01_Assessment/) | แบบสอบถามความพร้อม AI, โมเดลคะแนน, ผลส่งมอบและ matrix การตรวจสอบ |
| [`02_Course_Design`](02_Course_Design/) | แผนหลักสูตร L1-L5, คุณสมบัติบริษัท, รูปแบบ deploy, matrix โมดูลหลักสูตร |
| [`03_Consulting_Report`](03_Consulting_Report/) | template รายงานการวินิจฉัย AI Transformation |
| [`04_Scenarios`](04_Scenarios/) | สถานการณ์ลูกค้า, control table, กรณีศึกษาการผลิต, กรณีศึกษาโรงพยาบาล |
| [`05_Sales`](05_Sales/) | value proposition, sales talking points, FAQ |
| [`06_Delivery`](06_Delivery/) | delivery package และเกณฑ์การยอมรับ |
| [`90_References`](90_References/) | PDF ต้นฉบับ, รูปภาพระเบียบวิธี, บันทึกการเรียนจากวิดีโอ, การอ้างอิง |

## 5 บทบาทที่อยากดูเรื่อง เริ่มจาก 5 ไฟล์นี้

| คุณคือ | เริ่มจาก |
| --- | --- |
| **CEO / เจ้าของบริษัท / คนในครอบครัว** — อยากเข้าใจระเบียบวิธีนี้ใน 20 นาที | [`00_Overview/CLIENT_JOURNEY_STORY_EN.md`](00_Overview/CLIENT_JOURNEY_STORY_EN.md) — เรื่องของ Ming |
| **ที่ปรึกษา / ผู้เรียน** — อยากรู้ว่า 8 ขั้นรันยังไง สัญญาแบ่งยังไง | [`00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md`](00_Overview/EIGHT_STAGE_FLOW_STORY_EN.md) — กระบวนการครบ |
| **คณะกรรมการ / กำกับดูแล / วิชาการ** — อยากรู้ทำไมระเบียบวิธีนี้ทนการโต้แย้ง | [`00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) — การโต้แย้งทางวิทยาศาสตร์ |
| **IT องค์กรใหญ่ / ที่ปรึกษาย้ายบริษัท** — อยากรู้สอดคล้องกับ McKinsey/BCG/TOGAF/Gartner ยังไง | [`00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md`](00_Overview/INDUSTRY_FRAMEWORK_ALIGNMENT_EN.md) — แผนที่การจัดสอดคล้อง |
| **ผู้บริหารที่รีบ** — มีเวลาแค่ 5 นาที | [`00_Overview/EXECUTIVE_SUMMARY_EN.md`](00_Overview/EXECUTIVE_SUMMARY_EN.md) — Executive Summary |
| **นักวิจัยระเบียบวิธี / นักวิชาการ AI Pedagogy** — ทำไมนี่เป็นระเบียบวิธีแบบใหม่ | [`00_Overview/AI_NATIVE_LIVING_BOOK_EN.md`](00_Overview/AI_NATIVE_LIVING_BOOK_EN.md) — การออกแบบ AI-Native Living Book |
| **นักวิชาการ / กำกับดูแล / คณะกรรมการ** — เสาทฤษฎี 7 ต้น (Rosemann / Cohen & Levinthal / Teece / Real Options เป็นต้น) | [`00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md`](00_Overview/ACADEMIC_THEORETICAL_FOUNDATIONS_EN.md) — รากฐานทฤษฎีวิชาการ |
| **ที่ปรึกษา / การคาลิเบรตคะแนน** — จะให้คะแนน 0-4 อย่างเป็นกลาง หลีกเลี่ยงความเอนเอียงยังไง | [`01_Assessment/BARS_RUBRICS_EN.md`](01_Assessment/BARS_RUBRICS_EN.md) — BARS Behavioral Anchors |

## ลำดับการอ่านที่แนะนำ

1. [`00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md`](00_Overview/AI_TRANSFORMATION_STORY_AND_STRUCTURE.md)
2. [`01_Assessment/AI_MATURITY_QUESTIONNAIRE.md`](01_Assessment/AI_MATURITY_QUESTIONNAIRE.md)
3. [`01_Assessment/AI_MATURITY_SCORING_MODEL.md`](01_Assessment/AI_MATURITY_SCORING_MODEL.md)
4. [`01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md`](01_Assessment/AI_MATURITY_DELIVERABLES_AND_EVIDENCE_MATRIX.md)
5. [`02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md`](02_Course_Design/L1_L5_COMPLETE_COURSE_PLAN.md)
6. [`02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md`](02_Course_Design/L1_OPENWEBUI_COURSE_PLAN.md)
7. [`02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md`](02_Course_Design/L2_ANTIGRAVITY_COURSE_PLAN.md)
8. [`02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md`](02_Course_Design/L3_N8N_TIGERAI_COURSE_PLAN.md)
9. [`02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md`](02_Course_Design/L4_HERMES_AGENT_COURSE_PLAN.md)
10. [`04_Scenarios/CASE_CONTROL_TABLES.md`](04_Scenarios/CASE_CONTROL_TABLES.md)
11. [`06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md`](06_Delivery/DELIVERY_PACKAGE_AND_ACCEPTANCE.md)
12. [`03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md`](03_Consulting_Report/CONSULTING_REPORT_TEMPLATE.md)

## ผลส่งมอบที่ตรวจสอบได้

- แบบสอบถามและผลคะแนนความพร้อม AI
- การสำรวจคุณสมบัติบริษัทและรูปแบบ deploy
- หลักฐานการเรียนจบหลักสูตร L1-L5
- ตารางบัญชี / กลุ่ม / สิทธิ์ OpenWebUI และบันทึกการเปิดใช้พื้นที่แชทส่วนบุคคลของแต่ละคน
- Skill Library และ artifact ของ Antigravity / Claude Code / Codex
- n8n Workflow PoC, Execution Log, Data Tables, Sub-workflow Library
- Hermes Agent task card, Wiki, log ingest/query/update, briefing และ Gate 4A-4E
- ClawTeam Agent Team role card, log การทำงานร่วม และเอกสารผลลัพธ์
- บันทึกการยอมรับ Stage Gate
- รายงานการวินิจฉัย AI Transformation
- Roadmap 30 / 60 / 90 วัน

## เอกสารอ้างอิง

- [`90_References/@AI-MD-PUBIC.pdf`](90_References/@AI-MD-PUBIC.pdf)
- [`90_References/MD-Map.png`](90_References/MD-Map.png)
- [`90_References/Metholodgy.png`](90_References/Metholodgy.png)
- [`90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md`](90_References/OPENWEBUI_VIDEO_LEARNING_NOTES.md)
- [`90_References/TIGERAI_VIDEO_LEARNING_NOTES.md`](90_References/TIGERAI_VIDEO_LEARNING_NOTES.md)

## กิตติกรรมประกาศ

ขอขอบคุณเป็นพิเศษ **Prof. Michael Rosemann**, Queensland University of Technology (QUT), Brisbane, ออสเตรเลีย  
Profile: <https://www.qut.edu.au/about/our-people/academic-profiles/m.rosemann>

รากฐานทางทฤษฎีของระเบียบวิธีที่ปรึกษาทั้งหมดใน repo นี้ มาจากการเรียนของผู้สร้างที่ QUT Queensland University of Technology และการสร้างแรงบันดาลใจและการสอนระยะยาวของ Prof. Michael Rosemann ใน **Business Process Management (BPM)**, **Capability Maturity Models** และ **ระเบียบวิธีนวัตกรรมองค์กร**

มีสองส่วนหลักที่ได้รับอิทธิพลเป็นพิเศษ:

- **โครงสร้างที่ปรึกษา 8 ขั้นตอน**: สอดคล้องกับการวินิจฉัยกระบวนการองค์กร การประเมินความสามารถ การออกแบบเส้นทางการเปลี่ยนผ่าน และการกำกับดูแลการนำไปใช้
- **โมเดลความพร้อม AI L1-L5**: อ้างอิงตรรกะของ Capability Maturity Model และปรับให้เข้ากับท้องถิ่นในรูปกรอบ 5 ชั้นสำหรับการนำ AI มาใช้ในองค์กร

ข้อยกเว้นความรับผิดชอบ: ข้อผิดพลาด การละเลย การปรับให้เข้ากับท้องถิ่น หรือการขยายการประยุกต์ใช้ในด้าน AI ในระเบียบวิธีนี้ ทั้งหมดเป็นความรับผิดชอบส่วนตัวของผู้สร้าง Tiger AI Morris Lu 盧業興 ไม่ได้สะท้อนมุมมองหรือจุดยืนของ Prof. Michael Rosemann หรือ QUT

## ลิขสิทธิ์และการระบุชื่อ

โครงการนี้ใช้สัญญาอนุญาต **[Apache License 2.0](LICENSE)** คุณสามารถใช้งาน คัดลอก แก้ไข ดัดแปลง ทำซ้ำ เผยแพร่ สอน ส่งมอบที่ปรึกษา และใช้เชิงพาณิชย์ได้อย่างอิสระ

เมื่อเผยแพร่ซ้ำ ดัดแปลง ทำเชิงพาณิชย์ ใช้ในสื่อการสอน เอกสารส่งมอบที่ปรึกษา หรือเอกสารผลิตภัณฑ์ โปรดเก็บข้อความสัญญาอนุญาต Apache 2.0 และการระบุชื่อต่อไปนี้ใน [`NOTICE`](NOTICE) ไว้:

```text
Original Author: Tiger AI Morris Lu 盧業興
Role: n8n Taipei Ambassador / PhD Student, Graduate Institute of Intelligent Manufacturing, National Taiwan University of Science and Technology / M.IT, Queensland University of Technology (QUT), Australia
Source: https://github.com/MorrisLu-Taipei/GenAI-Consulting-Methodology-Toolkit
```

ชื่อแพลตฟอร์มของบุคคลที่สาม เครื่องหมายการค้า วิดีโอ โครงการภายนอก และเนื้อหาที่อ้างอิง ยังคงเป็นของผู้มีสิทธิ์เดิมแต่ละราย repo นี้ใช้ข้อมูลของบุคคลที่สามเพื่อบันทึกการเรียนรู้ การอ้างอิง การจัดระเบียบ และการอ้างอิงสำหรับการออกแบบหลักสูตรเท่านั้น

---

## ทำให้หนังสือเล่มนี้มีชีวิต: อ่านไปกับ AI

คู่มือติดตั้งด้านล่างจะนำคุณเชื่อม repo กับ AI IDE ก่อนเริ่มลงมือ ทำความเข้าใจโมเดลการใช้งานและเส้นแดงหนึ่งเส้นก่อน

**โมเดลการใช้งานในประโยคเดียว**: `git clone` หรือดาวน์โหลด zip → เปิดด้วย AI IDE (Antigravity / Claude Code / Codex เป็นต้น) → AI อ่าน [`AGENTS.md`](AGENTS.md) (และ `<ENGINE>.md` ของแต่ละ engine) อัตโนมัติ และตั้งบทบาทตัวเองเป็น **co-reading tutor ของระเบียบวิธีนี้** จากนั้นคุณสามารถ (1) ถามคำถามใดๆ เกี่ยวกับระเบียบวิธี (2) ให้มันประยุกต์ระเบียบวิธีกับสภาพบริษัทคุณ (3) ทำการวินิจฉัย L1-L5 กับมันและหาก้าวต่อไป

คำอธิบายเต็มดูได้ที่ [`00_Overview/AI_NATIVE_LIVING_BOOK_EN.md`](00_Overview/AI_NATIVE_LIVING_BOOK_EN.md)

> ⚠️ **ประกาศความซื่อสัตย์ทางวิชาการ / Academic Integrity Disclaimer**
>
> **กรณีศึกษาที่มีชื่อทั้งหมดใน repo นี้ (Manufacturing, Hospital, Marketing, B2B, Financial, Government, Education — 7 SAMPLE_CLIENT_CASE) และตัวละครเอกในเรื่อง (เช่น "Ming" / "MingChang Packaging") เป็นกรณีจำลองที่สร้างด้วย AI** ไม่ใช่ข้อมูลลูกค้าจริง
> ตัวเลขทั้งหมด (เวลา, ROI, person-month, งบประมาณ, KPI) เป็นเพียง **ตัวอย่าง** **ห้ามใช้เพื่อประชาสัมพันธ์ภายนอก ภาระผูกพันตามสัญญา หรือหลักฐานเชิงประจักษ์ทางวิชาการ**
> กรณี longitudinal จริงต้องผ่านการวิจัยเชิงประจักษ์ 18-24 เดือนตาม [`90_References/PILOT_STUDY_PROTOCOL_EN.md`](90_References/PILOT_STUDY_PROTOCOL_EN.md) ก่อนจะถูกเปลี่ยน
>
> **All named cases and story protagonists in this repo are AI-generated fictional examples**, NOT real client data. Numbers are illustrative; real cases will replace after the pilot study.

## 🚀 คู่มือติดตั้งและเริ่มใช้สาม AI Engine / Three AI Engines Setup Guide

**บทบาทและการแบ่งงาน** ของสาม engine ได้แนะนำไว้ในส่วน "🔱 สาม AI Engine ที่เชี่ยวชาญต่างกัน" ด้านบนแล้ว ส่วนนี้เน้น **วิธีติดตั้ง วิธีเริ่ม วิธีเรียก workflow** สามส่วนนี้แยกอิสระ เลือก engine ที่จะใช้แล้วอ่านเฉพาะส่วนนั้น

> ⚠️ **ตาม [`07_AI_Contributions/README.md`](07_AI_Contributions/README.md) §0**: สถาปัตยกรรมระเบียบวิธี, L1-L5, 8 ขั้นตอน, การแบ่งงาน 3 engine และการออกแบบเชิงกลยุทธ์อื่นๆ ทั้งหมดเสนอโดย **Morris Lu (มนุษย์)** สาม AI engine ภายใต้การกำกับดูแลของ Morris ทำหน้าที่ **ดำเนินงาน ขยายความ และตรวจสอบ** ไม่อ้างสิทธิ์เป็นเจ้าของสถาปัตยกรรมระเบียบวิธี รายละเอียดของแต่ละ engine ดูได้ที่ไฟล์ที่เกี่ยวข้องใน [`07_AI_Contributions/`](07_AI_Contributions/)

---

### 🟦 1. ผู้ใช้ Antigravity — ที่ปรึกษาแบบโต้ตอบแนวหน้า

> ยกระดับ "หนังสือที่มีชีวิต" นี้เป็น "**Conversational Consulting App**" ของคุณโดยตรง

**ขั้นตอนการติดตั้งและใช้งาน:**

1. **โหลดโปรเจค**: `git clone` หรือดาวน์โหลด zip ของโปรเจคนี้ลงเครื่อง
2. **เริ่ม IDE**: เปิดโฟลเดอร์โปรเจคด้วย Antigravity
3. **เริ่มต้นอัตโนมัติ**: Antigravity อ่าน [`ANTIGRAVITY.md`](ANTIGRAVITY.md) และ [`SKILL.md`](SKILL.md) อัตโนมัติ ตั้งตัวเองเป็น "**co-reading tutor**"
4. **รัน Workflow (Slash Commands)**: พิมพ์คำสั่งในกล่องสนทนาเพื่อเริ่มการโต้ตอบ

**คำสั่ง Antigravity ที่ใช้บ่อย:**

- `/diagnose` ── เริ่มการสนทนาแบบสมจริง นำคุณ (หรือลูกค้าคุณ) ทำการวินิจฉัยความพร้อม AI ขององค์กรในระดับ L1-L5
- `/generate-report` ── นำผลการวินิจฉัยและการอภิปรายก่อนหน้า เขียนเข้า template รายงานที่ปรึกษามาตรฐานและผลิตร่าง

ดูเพิ่มเติม [`.agent/workflows/`](.agent/workflows/) และ [`07_AI_Contributions/ANTIGRAVITY.md`](07_AI_Contributions/ANTIGRAVITY.md)

> คุณค่าหลักของ Antigravity: เปลี่ยนระเบียบวิธีเป็นประสบการณ์ที่ปรึกษาที่ **ลูกค้าฟังเข้าใจและโต้ตอบได้ทันที**

---

### 🟪 2. ผู้ใช้ Codex — Engine วิศวกรรมระเบียบวิธี

> มอง repo นี้เป็น "**workspace วิศวกรรมระเบียบวิธี**" — ดูแล AI-native living book นี้ในฐานะผลิตภัณฑ์ระเบียบวิธีที่ **ทดสอบได้ ตรวจสอบได้ ติดตามได้ ซ่อมได้ ออกเวอร์ชันได้**

**ขั้นตอนการติดตั้งและใช้งาน:**

1. **โหลดโปรเจค**: `git clone` หรือดาวน์โหลด zip ของโปรเจคนี้ลงเครื่อง
2. **เริ่ม Codex**: เปิดโฟลเดอร์โปรเจคใน Codex
3. **อ่านไฟล์เริ่มต้น Codex**: ให้ Codex อ่าน [`CODEX.md`](CODEX.md) และ [`.codex/README.md`](.codex/README.md) ก่อน
4. **รัน Workflow Codex**: พิมพ์ชื่อ workflow ในการสนทนา หรือขอให้ Codex ทำตามไฟล์ที่เกี่ยวข้องอย่างชัดเจน

**คำสั่ง Codex ที่ใช้บ่อย (10 คำสั่ง):**

| ประเภท | คำสั่ง | วัตถุประสงค์ |
| --- | --- | --- |
| Production | `/diagnose` | การวินิจฉัยความพร้อม AI เบื้องต้นแบบโต้ตอบ |
| Production | `/generate-report` | ร่างรายงานการวินิจฉัยที่ปรึกษา |
| Quality | `/evidence-audit` | ตรวจสอบ evidence chain ของรายงาน |
| Quality | `/consistency-review` | ตรวจสอบความสอดคล้องของ L1-L5, Stage Gate, HITL, Evidence ข้ามเอกสาร |
| Evolution | `/academic-upgrade` | แปลงข้อเสนอเชิงวิชาการเป็นแผนซ่อมระเบียบวิธี |
| Evolution | `/harvest-insights` | เก็บเกี่ยว insight ร่วมจากรายงานหลายฉบับ |
| Defense | `/test-methodology` | ทดสอบ stress ระเบียบวิธีในสถานการณ์สุดขั้ว |
| Defense | `/red-team-review` | Red-team review ของร่างรายงาน |
| Audit | `/generate-traceability` | สร้าง matrix การติดตาม questionnaire → maturity → evidence → report |
| DevOps | `/bump-version` | เสนอเลขเวอร์ชันเชิงความหมายและ CHANGELOG |

**วิธีการเรียกที่แนะนำ:**

```text
กรุณาทำตาม .codex/workflows/evidence-audit.md ตรวจสอบร่างรายงานที่ปรึกษานี้
```

ดูเพิ่มเติม [`.codex/workflows/`](.codex/workflows/) และ [`07_AI_Contributions/CODEX.md`](07_AI_Contributions/CODEX.md)

> คุณค่าหลักของ Codex: ให้ระเบียบวิธีนี้มีวงจรชีวิตวิศวกรรมแบบ "**ทดสอบได้ ตรวจสอบได้ ติดตามได้ ซ่อมได้ ออกเวอร์ชันได้**"

---

### 🟨 3. ผู้ใช้ Claude Code — Engine คิดเชิงกลยุทธ์ข้ามไฟล์และทดลอง

> **เล่น / ทดลอง / รื้อ / ชน** ระเบียบวิธี ใช้ Claude Code 1M context + multi-persona ขนาน + การคิดเชิงนามธรรมข้ามสาขา เพื่อ **จำลอง ทดลอง โต้แย้ง Fork**

**ขั้นตอนการติดตั้งและใช้งาน:**

1. **โหลดโปรเจค**: `git clone` หรือดาวน์โหลด zip ของโปรเจคนี้ลงเครื่อง
2. **เริ่ม Claude Code**: เปิดโฟลเดอร์โปรเจคใน Claude Code CLI / IDE
3. **อ่านไฟล์เริ่มต้น Claude Code**: ให้ Claude Code อ่าน [`CLAUDE.md`](CLAUDE.md) และ [`.claude/README.md`](.claude/README.md) ก่อน
4. **รัน Workflow Claude Code**: พิมพ์ชื่อ workflow ในการสนทนา

**คำสั่ง Claude Code ที่ใช้บ่อย (10 คำสั่ง):**

| ประเภท | คำสั่ง | วัตถุประสงค์ |
| --- | --- | --- |
| Tier 1 Tactical | `/deep-synthesize` | สังเคราะห์ข้ามหลายไฟล์ในเชิงลึก (1M context) |
| Tier 1 Tactical | `/theory-bridge` | สถานการณ์ลูกค้า ↔ ตรงกับเสาทฤษฎี 7 ต้น |
| Tier 1 Tactical | `/scenario-planning` | จากข้อจำกัด สร้าง 3 roadmap เปรียบเทียบ + trade-off |
| Tier 1 Tactical | `/socratic-challenge` | คำถามแบบ Socratic เพื่อลับการคิดของผู้ใช้ |
| Tier 1 Tactical | `/cross-stage-trace` | ติดตามผลกระทบ downstream ของการเปลี่ยนแปลงเดียว |
| Tier 2 Original | `/simulate-engagement` | รันโครงการที่ปรึกษาครบ 6 สัปดาห์ใน 30 นาที (ผลิต 12+ deliverable) |
| Tier 2 Original | `/parallel-perspectives` | stakeholder 6 คน **พร้อมกัน** ออกเสียงต่อการตัดสินใจเดียว + แผนที่ความขัดแย้ง |
| Tier 2 Original | `/thought-experiment` | counterfactual stress test ของระเบียบวิธี ("ถ้า EU AI Act ห้าม L4 ล่ะ?") |
| Tier 2 Original | `/devil-pair-debate` | Claude 2 ตัวโต้แย้งจริง + ผู้ตัดสินสังเคราะห์ |
| Tier 2 Original | `/methodology-fork` | Fork ระเบียบวิธีมาตรฐานเป็นเวอร์ชันเฉพาะลูกค้า (Methodology-as-Code) |

**วิธีการเรียกที่แนะนำ:**

```text
กรุณาทำตาม .claude/workflows/simulate-engagement.md จำลองโครงการที่ปรึกษา 6 สัปดาห์
สำหรับลูกค้าผลิตขนาด 500 คน
```

ดูเพิ่มเติม [`.claude/workflows/`](.claude/workflows/) และ [`07_AI_Contributions/CLAUDE_CODE.md`](07_AI_Contributions/CLAUDE_CODE.md)

> คุณค่าหลักของ Claude Code: ยกระดับระเบียบวิธีจาก "**มาตรฐาน**" เป็น "**มาตรฐาน + N เวอร์ชันต่อยอด + การจำลองครบ + การโต้แย้งหลายมุมมอง**" หนังสือมีชีวิตที่ทดลองได้

---

### ข้อเสนอแนะการทำงานร่วมสาม Engine / Three-Engine Workflow Suggestions

จังหวะการทำงานร่วมที่พบบ่อยในทางปฏิบัติ:

```text
Phase A การวินิจฉัยลูกค้า
  → Antigravity รัน /diagnose เก็บสภาพปัจจุบัน
  → Claude Code รัน /theory-bridge ตรงกับการวินิจฉัยทฤษฎี
  → Antigravity รัน /generate-report ผลิตร่างรายงานกลางทาง
  → Codex รัน /evidence-audit ตรวจ evidence chain
  → Codex รัน /consistency-review จัดสอดคล้องข้ามไฟล์

Phase B การออกแบบกลยุทธ์
  → Claude Code รัน /scenario-planning ให้ 3 roadmap
  → Claude Code รัน /parallel-perspectives มุมมอง 6 stakeholder
  → Codex รัน /red-team-review โจมตีความ optimist เกินไป
  → Claude Code รัน /devil-pair-debate โต้แย้งสมมติฐานเชิงค่านิยม

Phase C การนำไปใช้และการวิวัฒน์
  → Codex รัน /generate-traceability ตรวจสอบรายไตรมาส
  → Claude Code รัน /thought-experiment ทดสอบ counterfactual
  → Codex รัน /bump-version ดูแลเวอร์ชันระเบียบวิธี
  → Claude Code รัน /methodology-fork สร้างเวอร์ชันต่อยอดสำหรับลูกค้าใหญ่
```

> Workflow ของสาม engine ไม่ exclusive ซึ่งกันและกัน **จุดสำคัญคือให้แต่ละ engine ทำสิ่งที่ตัวเองเก่งที่สุด** มนุษย์ (ที่ปรึกษา / Client Owner / Sponsor) ตัดสินว่าเมื่อไหร่จะสลับ engine
