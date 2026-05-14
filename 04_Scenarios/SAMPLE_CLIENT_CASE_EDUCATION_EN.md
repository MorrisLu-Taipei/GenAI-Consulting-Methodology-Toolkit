# Sample Client Case: Education Institution

> 🌐 中文版本 / Chinese version: [SAMPLE_CLIENT_CASE_EDUCATION.md](SAMPLE_CLIENT_CASE_EDUCATION.md)
> Apache License 2.0 · Author: Morris Lu (盧業興) · Tiger AI 虎智科技
> Source: <https://github.com/MorrisLu-Taipei/AI-Consulting-Methodology-Toolkit>
>
> **Sample case for illustration. The client is referred to by the code "University E" (not a real institution name). Content is synthesized from multiple real education engagements; numbers are illustrative.**

---

## 1. Client Profile

| Field | Content |
| --- | --- |
| Institution code | University E (private university of technology, anonymized) |
| Nature | Private university of technology |
| Scale | 600 faculty & staff (380 teachers / 220 administrative), 8,000 students |
| Starting L-level | L1 |
| Budget | NT$ 6M (18 months) |
| Regulation | Personal data law (student data), Ministry of Education rules, academic integrity |
| Main pain points | (1) Heavy teacher lesson-prep / grading load (2) Many repeated admissions-consulting Q&A (3) Time-consuming departmental accreditation document collation (4) Many paper-based administrative processes |

## 2. Engagement Onboarding & Diagnostic

### 2.1 10-Question Quick Survey Results

Average **1.0 → L1**. Tool usage Q1=2 (teachers use ChatGPT individually), governance Q6=0, process Q3=1.

### 2.2 25-Question Six Constructs

| Construct | Average |
| --- | ---: |
| Tool usage | 2.4 (high teacher acceptance) |
| Knowledge codification | 1.2 |
| Process standardization | 1.5 |
| System integration | 0.8 |
| Agent application | 0.4 |
| Governance & ROI | 0.6 |

**Insight:** high individual teacher usage (good acceptance), but the organization has no governance and no codification. The education-institution adoption pattern — teacher resistance and support are polarized, so "workload reduction" is the icebreaker; student-data protection is the red line.

### 2.3 Company Profile Bundle (key points)

```json
{
  "profile": {"industry":"education","headcount_bucket":"300-1000"},
  "systems": {"lms":"Moodle","wiki":["Google Drive"],"sis":"self-built student-records system","email":"Google Workspace for Education"},
  "risk": {"sensitive_data":["student PII","grades","health"],"regulations":["personal data law","Ministry of Education rules","academic integrity"],"llm_retention_acceptance":"30d acceptable"},
  "deployment": {"preference":"Hybrid","gpu_capacity":"4090 class","local_llm_plan":"evaluating"},
  "course": {"l1_headcount":600,"seed_team_headcount":20,"objectives":["org-wide enablement","workflow automation"]},
  "budget": {"annual_bucket":"500K-2M","kickoff":"1-3 months"}
}
```

## 3. Recommended Course Mix

| Level | Ratio | Focus |
| ---: | ---: | --- |
| L1 | 35% | Org-wide enablement; teacher + admin split tracks; student-data red lines; academic-integrity policy |
| L2 | 30% | Teacher teaching Skills + administrative Skills |
| L3 | 25% | Admissions FAQ, accreditation documents, administrative-process Workflows |
| L4 | 8% | Course search & recommendation Agent |
| L5 | 2% | Concept explanation |

Rationale: teacher acceptance is high, so L1 can move faster; the focus is on L2 teaching Skills (the biggest workload-reduction lever) + L3 administrative automation.

## 4. In-Class Artifacts

### L1 OpenWebUI (6 weeks)

- 600 faculty & staff accounts (teacher track / admin track on separate courses)
- **Hybrid deployment:** public teaching material → cloud; student PII / grades → on-prem (4090 machine)
- AI usage policy: student PII absolutely cannot enter a cloud LLM; academic integrity (the line between AI-assisted and AI-written)
- Prompt Library, 32 entries (instructional design, administrative documents, admissions replies)
- A separate policy for the student side (academic-integrity guidelines for student AI use)

### L2 Skill AI (8 weeks)

12 Skills:

| # | Skill | Owner |
| --- | --- | --- |
| 1 | Lesson plan / course syllabus draft | Teachers |
| 2 | Assignment feedback summary (formative) | Teachers |
| 3 | Assessment item generation (with rubric) | Teachers |
| 4 | Slide outline and lecture-script draft | Teachers |
| 5 | Course-recording auto-captioning + summary | Teaching Development Center |
| 6 | Admissions FAQ reply draft | Admissions Office |
| 7 | Parent / student communication draft | Homeroom teachers / Admin |
| 8 | Departmental accreditation document collation | Department assistants |
| 9 | Administrative document drafting | Administrative offices |
| 10 | Meeting notes and resolution tracking | Secretariat |
| 11 | Student counseling-record structuring | Student Affairs / Counseling (strict permissions) |
| 12 | Research-proposal summary and format check | Research & Development Office |

### L3 n8n Workflow (6 weeks)

4 Workflow PoCs:

1. **Admissions FAQ auto-reply** — admissions mailbox / form → Skill #6 → Admissions Office review → send
2. **Accreditation document collation Pipeline** — accreditation item → RAG over Drive → Skill #8 → department-assistant review
3. **Course-recording processing** — recording upload → Whisper → Skill #5 → Moodle captions + summary
4. **Administrative document workflow** — document arrives → Skill #9 → handler review

### L4 Hermes Agent (4 weeks)

**Course Search & Recommendation Agent:**
- Wiki: all university course data, course-selection rules, program maps, career mapping
- Skills: course search, program explanation
- Task card: a student asks "what courses should I take to develop toward X" → the Agent gives a course combination + program path + reasoning
- Reviewer: Office of Academic Affairs / department chair
- Gates 4A-4E passed
- **Student PII does not enter this Agent** (course data only)

### L5 ClawTeam

Concept explanation only.

## 5. Eight-Stage Analysis

### Stage 1 Current-State Discovery
- Interviews: President, VP of Academic Affairs, VP of Student Affairs, 3 department chairs, Teaching Development Center, Admissions Office, Information Center
- Pain density: lesson prep / grading (teachers 95%), admissions Q&A (Admissions Office 100%), accreditation (departments 90%)

### Stage 2 Vision Alignment
- President's vision: within 18 months, teacher administrative load -30%, admissions-consulting response < 1 day, halve accreditation document-prep time
- Sponsor = VP of Academic Affairs + Director of the Information Center

### Stage 3 Industry Benchmark
- International: ASU (Arizona State University) AI applications, Khan Academy's Khanmigo (vision reference)
- Hybrid, benchmarked against the personal data law + academic-integrity rules

### Stage 4 Gap Analysis

Missing/Broken/Redundant:
- **Missing:** AI governance policy, academic-integrity AI guidelines, Skill Library, student-data boundaries
- **Broken:** accreditation documents re-collated manually each time (departments spend 200+ hours per accreditation)
- **Redundant:** 60% of admissions Q&A are repeated questions; each department has its own course introductions

Impact × Effort:
- Quick Win: admissions FAQ (L3-W1); lesson-plan draft Skill (L2-#1)
- Big Bet: accreditation document Pipeline (L3-W2)
- Avoid: AI grading directly into a grade (high academic risk, assistive only)

### Stage 5 Executive Problem Statement

```
CONTEXT: Under declining birth rates, admissions competition is fierce; Ministry of Education
         accreditation is frequent; teacher attrition is rising (administrative load is a major
         cause).
TENSION: Individual teacher AI acceptance is high (L1+) but the organization has zero governance
         and zero codification; student-data protection pressure is high.
COI: If no action for 18 months: (1) teacher attrition intensifies (2) admissions conversion
     lags peer schools (3) accreditation prep continues to drain department staff.
DESIRED: Reach L3-L4 in 18 months; teacher administrative load -30%; admissions response < 1 day;
         accreditation prep -50%.
CONSTRAINT: NT$ 6M budget; student PII on-prem; clear academic-integrity boundaries; teacher
            resistance must be handled.
```

### Stage 6 Roadmap

| Phase | Month | Main deliverables | Gate | KPI |
| --- | --- | --- | --- | --- |
| 1 | 1-3 | L1 org-wide + governance + academic-integrity guidelines | Gate 1 | weekly teacher usage ≥ 60% |
| 2 | 4-9 | L2 12 Skills | Gate 2 | Skill Library ≥ 12 |
| 3 | 10-14 | L3 4 Workflows | Gate 3 | admissions response < 1 day |
| 4 | 15-18 | L4 Course Recommendation Agent | Gate 4 | student usage rate ≥ 30% |

### Stage 7 Solution Architecture

- **Variant B, Hybrid:**
  - Public teaching material → cloud (Claude / Gemini for Education)
  - Student PII / grades / counseling records → on-prem (4090 + Llama 8B/70B)
- Moodle LMS integration; Google Workspace integration

### Stage 8 Governance & ROI

- Permissions: tiered — teacher / admin / counseling / IT; strict ACL on student data
- Academic integrity: a teacher-side "AI-assisted" guideline + a student-side "academic honesty" guideline
- Audit: all LLM calls 1 year; student-data-related 3 years
- ROI Tracker: teacher administrative time, admissions response time, accreditation prep hours, Skill usage rate

## 6. Diagnostic Report Summary

> **Core finding:** University E has high individual teacher AI acceptance (L1+) but zero organizational governance and codification. The education-institution adoption pattern — "teacher workload reduction" is the most effective icebreaker, and student PII is an untouchable red line. Recommend reaching L3-L4 in 18 months.
>
> **Expected ROI:** quantifiable benefit of NT$ 24M over 18 months, ROI ≈ 300%.

## 7. 30/60/90-Day Roadmap

### 30 days
- L1 OpenWebUI 600 accounts (teacher track first)
- AI usage policy + academic-integrity guidelines draft
- 4090 on-prem machine built (for student PII)

### 60 days
- L1 admin track live
- Academic-integrity guidelines passed by the University Affairs Council
- 5 quick-win Skills live (#1, #3, #6, #9, #10)

### 90 days
- Skill Library reaches 12
- Admissions FAQ Workflow live (before the admissions peak season)
- Gate 1 + Gate 2 passed

## 8. ROI Projection

| Initiative | Baseline | 18-month Target | NT$ impact |
| --- | --- | --- | --- |
| Teacher administrative / lesson-prep time | high | -30% | NT$ 10M/year (equivalent headcount) |
| Admissions-consulting response | 2-3 days | < 1 day | NT$ 6M/year (conversion uplift) |
| Accreditation document prep | 200+ hours/department | -50% | NT$ 4.8M/year |
| Administrative document processing | slow | -35% | NT$ 3.2M/year |
| Teacher-attrition protection | - | - | NT$ 6M (recruiting + transition cost) |
| **Subtotal** | | | **NT$ 30M** |
| **Less investment** | | | **-6M** |
| **Net benefit** | | | **NT$ 24M/year** |

## 9. Risks & Governance

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Student PII leaked to a cloud LLM | Medium | Critical | student data on-prem; redact; Audit |
| AI ghostwriting undermines academic integrity | High | High | student-side academic-honesty guideline + AI content checking + teacher education |
| AI grading misjudges and assigns a wrong grade | Medium | High | AI is formative-assistive only; grades always confirmed by the teacher |
| Polarized teacher resistance | High | Medium | icebreak with workload reduction; seed teachers demonstrate; not mandatory |
| Accreditation document AI content questioned | Medium | Medium | department-assistant review; source traceability |

## 10. Outcome Summary

After 18 months:
- Advanced from L1 to L3-L4
- Teacher administrative load -30%; admissions response < 1 day; accreditation prep -50%
- The academic-integrity guidelines become a permanent University Affairs policy
- The Course Recommendation Agent reaches a 35% student usage rate
- The Teaching Development Center transforms into an "AI Teaching Support Center"

References: full PoC `02_Course_Design/POC_SCENARIO_SPECS.md`; industry `INDUSTRY_SCENARIOS.md` (education section); consulting toolkit `03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES.md`.
