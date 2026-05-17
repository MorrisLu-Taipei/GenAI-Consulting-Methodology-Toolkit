# Pilot Study Protocol: Empirischer Validierungs-Forschungsplan für Tiger AI Methodik

> 🌐 Sprache: [繁體中文](PILOT_STUDY_PROTOCOL.md) ｜ [English](PILOT_STUDY_PROTOCOL_EN.md) ｜ Deutsch ｜ [Français](PILOT_STUDY_PROTOCOL_FR.md) ｜ [Español](PILOT_STUDY_PROTOCOL_ES.md) ｜ [日本語](PILOT_STUDY_PROTOCOL_JA.md) ｜ [한국어](PILOT_STUDY_PROTOCOL_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Letzte Aktualisierung: 2026-05-16
Version: v1.0 Research Design Protocol (Pre-Registration Ready)

---

> **Zweck**: Tiger AI Methodik von einem „gut designten Consulting-Framework" in ein „erforschbares Modell" weiterentwickeln. Dieses Protokoll definiert eine 18-24-monatige, 5-10 Unternehmen umfassende empirische Pilot-Studie, **die die Methodik externer Falsifizierung statt nur Selbstvalidierung unterzieht**.
>
> Dies ist ein **Research Design Dokument**, bereit für IRB-Submission / akademische Pre-Registration / Government Research Grant Applications.

---

## 1. Hintergrund & Motivation

### 1.1 Warum empirische Forschung

Aktuelle Evidenz-Stärke der Tiger AI Methodik:

| Element | Evidence Level (Tool 8.9) | Status |
| --- | --- | --- |
| 8-Stufen-Flow Design | L2 dokumentarisches Argument | Komplett (Rosemann BPM + Industry Framework Integration) |
| 6 Constructs × 0-4 Skala | L2 Expertenkonsens | Komplett (**keine psychometrische Validierung**) |
| 7-Case Library | L2 anonymisiertes Composite | Komplett (**keine echten longitudinalen Daten**) |
| Self-Qualification (Tool 2.5) | L1 Self-Report | Komplett (**selbstreferentiell, nicht extern validiert**) |
| Inter-Rater Consistency | — | **Nicht gemacht** |
| Longitudinale KPI-Antwort auf Methodik | — | **Nicht gemacht** |

**Schlussfolgerung**: Die Methodik ist reif in „interner Konsistenz + logischer Geschlossenheit", wurde aber nicht empirisch auf „externe Reproduzierbarkeit + Predictive Validity" getestet. Diese Pilot-Studie adressiert beides.

### 1.2 Forschungsfragen

**RQ1 — Inter-Rater Reliability**: Können verschiedene Berater, die dieselbe Methode nutzen, dasselbe Unternehmen konsistent scoren?

- **H1**: Cohen's κ ≥ 0,60 (substantial agreement)

**RQ2 — Interne Konsistenz**: Wie intern konsistent sind die 6 Constructs?

- **H2**: Cronbach's α ≥ 0,70 pro Construct

**RQ3 — Construct Validity**: Tauchen die 6 Constructs sauber in der Faktoranalyse auf?

- **H3a**: EFA extrahiert 5-6 Faktoren; jedes Item lädt ≥ 0,5 auf seinen zugewiesenen Faktor
- **H3b**: CFA 6-Faktor-Modell Fit: CFI ≥ 0,90, TLI ≥ 0,90, RMSEA ≤ 0,08

**RQ4 — Predictive Validity**: Können T0-Scores T+12 Monate Business KPI Verbesserung vorhersagen?

- **H4**: Bei Kontrolle für Baseline KPI und Unternehmensgröße sagt Tiger AI Maturity Score positiv +12m KPI-Verbesserung voraus (β ≥ 0,30, p < 0,05)

**RQ5 — Longitudinales Pattern**: Zeigen Unternehmen, die Phase C 24 Monate abschließen, „rundere" Radare?

- **H5**: T0 vs T24 Radar-Fläche (6-Construct Summe) steigt signifikant, und das Wachstum jedes Constructs folgt Tool 6.1 Dekomposition (Foundation → Optimization → Excellence)

---

## 2. Studien-Design

### 2.1 Design-Typ

- **Mixed-Methods longitudinale Studie**
- **Convergent Parallel Design**: quantitativ (Scale Scoring, KPIs) + qualitativ (semi-strukturierte Interviews, Case Studies) gleichzeitig
- **Pre-Registered** (öffentliche Hypothesen, Sampling, Analyseplan; p-hacking vermeiden)

### 2.2 Sample

| Item | Spezifikation |
| --- | --- |
| **Ziel-Sample N** | 5-10 Unternehmen (Pilot-Stage; Main Study N=200+ für CFA) |
| **Industrie-Diversität** | ≥ 3 Industrien (≥ 1 jeweils Manufacturing, Services, Public Sector) |
| **Unternehmensgröße** | 100-5000 Mitarbeiter |
| **AI Startpunkt** | L0-L2 (bereits L3+ ausgeschlossen wegen limitierter Interventions-Space) |
| **Commitment Duration** | 18 Monate (Forschungs-Collaboration Agreement) |
| **Incentive** | Free / vergünstigtes Consulting + Co-Publication-Möglichkeit + Case-Anonymisierungs-Kontrolle |

### 2.3 Recruiting-Strategie

1. Über n8n Taipei Ambassador Community, Enterprise-Client-Netzwerke, akademische Partner-Institutionen (spezifische Partner offengelegt nach MOU-Unterzeichnung)
2. Public Solicitation + Apache 2.0 Open Repo als Vertrauenssignal
3. Signiertes Research Collaboration Agreement (Datennutzung, Anonymisierung, Exit-Mechanismus)

### 2.4 Ethics / IRB

- Bewerbung für akademische Partner-Institution IRB Approval (Partner offengelegt nach MOU-Unterzeichnung)
- Informed Consent: alle Teilnehmer schriftlich
- Sensitive Data Handling: PII / Business Secret Grading; Double-Blind Data Isolation
- Right to Withdraw: jedes Unternehmen kann jederzeit aussteigen; gesammelte Daten zurückgegeben oder zerstört

---

## 3. Double-Blind Scoring Design

### 3.1 Zweck

Validiere **Inter-Rater Reliability** des Tiger AI Scoring Modells.

### 3.2 Design

```
T0 Scoring Phase (pro Unternehmen):
  ↓
  Berater A vollendet unabhängig:
    • Interviews (Tool 1.1 40-Q Bank)
    • Inventory + Swimlane (Tools 1.2-1.4)
    • Reference Model Mapping (Tool 2.2)
    • 6-Construct 0-4 Scoring (Tool 2.3)
    • Primary Maturity Judgment (L1-L5)
  ↓
  Berater B vollendet unabhängig (gleiches Unternehmen, blinded gegenüber A):
    • Wiederhole alle obigen Aktionen
  ↓
  Research Analyst (neutral) vergleicht A vs B:
    • 6-Construct Score Gap (weighted kappa)
    • Primary Maturity Judgment Agreement (unweighted kappa)
    • Gap Identification Overlap (M/B/R Tabelle Overlap)
```

### 3.3 Consistency-Statistiken

| Metrik | Tool | Interpretation |
| --- | --- | --- |
| **Cohen's κ (unweighted)** | κ = (Po - Pe) / (1 - Pe) | < 0,20 slight; 0,21-0,40 fair; 0,41-0,60 moderate; 0,61-0,80 substantial; > 0,80 almost perfect |
| **Weighted κ (linear / quadratic)** | Für ordinale Skala (0-4) | Wie oben, aber strenger bei „1 Punkt off" vs „4 Punkte off" |
| **ICC (Intraclass Correlation)** | Two-way Mixed Model | < 0,5 poor; 0,5-0,75 moderate; 0,75-0,9 good; > 0,9 excellent |
| **Bland-Altman Plot** | Score-Gap visualisieren | Systematischen Bias detektieren |

---

## 4. Longitudinales KPI Tracking

### 4.1 KPI-Messzeitpunkte

| Zeitpunkt | Name | Messung |
| --- | --- | --- |
| **T0** | Baseline | Nach Phase A, vor Phase B |
| **T+6m** | Phase 1 Ende | L1 Gate Acceptance |
| **T+12m** | Mid Phase 2 | L2/L3 Gate |
| **T+18m** | Phase 2 Ende | L3 komplett |
| **T+24m** | Phase 3 Ende | L4/L5 Gate |

### 4.2 5 KPI-Dimensionen (per Tool 8.5 Value Tracking)

| Dimension | Beispiel KPIs |
| --- | --- |
| **Time** | Complaint Response, Proposal Turnaround, Month-End Close, Decision Cycle |
| **Quality** | Defekt-Rate, Error-Rate, Complaint Count, Rework Rate |
| **Scale** | Throughput, Beneficiaries, Automated Task Count |
| **Risk** | Missed Case Rate, Compliance Violations, Sensitive-Data Leakage |
| **Assets** | Skill Count, Wiki Entries, Agent Task Count, Training Completion |

### 4.3 KPI Data Quality (per Tool 8.9 Evidence Hierarchy)

- **L3 verpflichtend**: Alle Time / Scale KPIs aus System Logs (n8n / Audit Log / ERP)
- **L4 empfohlen**: Sample-verifiziert durch Internal Audit / External Accountants
- **L1-L2 supplementär**: Employee NPS / Interview Summaries

---

## 5. Qualitativ: Semi-Strukturierte Interviews

### 5.1 Interview-Zeitpunkte

Pro Unternehmen: T0, T+6m, T+12m, T+18m, T+24m — je 1 Runde (pro Interviewee).

### 5.2 Interviewees

- CEO / Sponsor
- AI Champion
- IT Lead
- ≥ 2 Department Heads
- ≥ 3 Front-line Users

### 5.3 Interview-Fragen (Auszug)

1. Was ist die impactvollste AI-Veränderung in den letzten 6 Monaten?
2. Welche erwarteten AI-Veränderungen passierten nicht? Warum?
3. Hat sich die Attitude von Personal / Abteilung gegenüber AI verschoben?
4. Würden Sie diese Methodik Peers empfehlen / nicht empfehlen?
5. Welcher Stage / Tool war am nützlichsten? Am wenigsten?
6. Cross-Time: Rückblickend auf die vor 12 Monaten signierte Ideal Practice, irgendwelche Reue?

### 5.4 Qualitative Analyse

- Verbatim Transcription + Coding (NVivo / Atlas.ti)
- Dual-Coder Reliability ≥ 80%
- Thematische Analyse, um Patterns / Counter-Examples zu extrahieren

---

## 6. Statistischer Analyseplan

### 6.1 Deskriptive Statistiken

- Score-Verteilung pro Construct (Mean, SD, Median, IQR)
- Radar Chart T0 vs T24 Visualisierung
- 6-Construct Korrelationsmatrix (Multikollinearitäts-Check)

### 6.2 Reliability & Validity

| Analyse | Tool | Mappt zu Hypothese |
| --- | --- | --- |
| Cronbach's α | SPSS / R `psych::alpha()` | H2 |
| EFA + Bartlett's + KMO | SPSS / R `psych::fa()` | H3a |
| CFA + Fit Indices | Mplus / R `lavaan::cfa()` | H3b (**N ≥ 200 erforderlich**) |
| Cohen's κ | R `irr::kappa2()` | H1 |
| ICC | R `irr::icc()` | H1 |

### 6.3 Inferenzielle Statistiken

| Analyse | Hypothese | Tool |
| --- | --- | --- |
| Paired t-Test (T0 vs T24) | H5 Radar-Flächen-Anstieg | R `t.test(paired=TRUE)` |
| Mixed-Effects Model | H4 Predictive Validity | R `lme4::lmer()` |
| ANCOVA | Kontrolliere Baseline KPI + Size | R `aov()` |
| Sensitivitätsanalyse | Gegen Missing Data + Dropout | R `mice` Multiple Imputation |

### 6.4 Signifikanz & Adjustment

- α = 0,05 Haupttest
- Bonferroni Correction für Multiple Comparisons
- Effect Size Reporting: Cohen's d, η², partial η²

---

## 7. Timeline & Meilensteine

```
Monat 0:     Design finalisieren + IRB Submission
Monat 1-3:   5-10 Unternehmen rekrutieren + Research Agreement signieren
Monat 4:     Berater A/B trainieren (Double-Blind SOP)
Monat 5-6:   T0 Double-Blind Scoring + Baseline KPI Messung
Monat 6-12:  Phase 1 Intervention + T+6m Scoring + Interviews
Monat 12-18: Phase 2 Intervention + T+12m + T+18m
Monat 18-24: Phase 3 Intervention + T+24m Final Scoring + Interviews
Monat 24-27: Analyse + Forschungs-Report + Journal Submission
Monat 27-30: Revisions + Submission
```

---

## 8. Budget-Schätzung

| Item | Geschätzt (NT$) |
| --- | --- |
| Berater-Zeit (A + B 80-120 Std je pro Unternehmen) | 6-9M |
| Research Staff (neutraler Scoring-Vergleich + qualitative Analyse) | 1,5-2,5M |
| KPI System-Log Tools + Interview-Transkription | 0,5-1M |
| IRB / Legal / statistischer Berater | 0,5-1M |
| Open-Source Tools + Cloud Data Store | 0,3-0,5M |
| Kontingenz (15%) | 1,3-2M |
| **Total** | **NT$ 10,1-16M** |

⚠️ Im Austausch für kostenloses Consulting committen 5-10 Unternehmen zu 18 Monaten Datensammlung → Berater-Arbeit kann durch „equivalent Consulting Service" offset werden, **tatsächliche Cash-Outlay reduzierbar auf NT$ 4-7M**.

---

## 9. Publikations-Strategie

### 9.1 Erwartete Outputs

| Output | Journal / Plattform | Geschätztes Timing |
| --- | --- | --- |
| **Pre-Registration** | OSF | Monat 0 |
| **Protocol Paper** | BMJ Open / Pilot and Feasibility Studies | Monat 3 |
| **Methodology Paper** | MIS Quarterly / Information Systems Research / Journal of Business Research | Monat 27 |
| **Industry White Paper** | Bilingual, public Apache 2.0 | Monat 27 |
| **Case Studies (anonymisiert)** | HBR-Style Cases | Monat 30 |
| **Practitioner Guide** | Toolkit updaten + empirische Evidenz hinzufügen | Monat 30 |

### 9.2 Open Science Commitment

- Alle Forschungsdaten (de-identifiziert) öffentlich auf OSF
- Statistische R / Python Scripts auf GitHub
- Interviewee-Identität vertraulich; aggregierte Ergebnisse voll transparent

---

## 10. Risiken & Mitigation

| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
| --- | --- | --- | --- |
| Enterprise Mid-Withdrawal (Dropout) | Med | Hoch | Over-Recruit 12; Intention-to-Treat Analyse |
| Berater A/B Bias / Leakage | Niedrig | Hoch | SOP Training + Audits + strenges Double-Blind + verschiedene Offices |
| KPI System Log nicht zugänglich | Med | Med | T0 IT bestätigt Log-Verfügbarkeit; Ersatz-Indikatoren wenn nicht |
| IRB Review Delay | Med | Med | Monat 0 IRB Submission gleichzeitig mit Recruitment |
| Unzureichendes N für CFA | Hoch | Med | EFA im Pilot; CFA wartet auf Main Study N=200+ |
| Budget Shortfall | Med | Hoch | Regierungs-Grants (NSTC / MOE etc.) / akademische Partner-Grants beantragen; Multi-Enterprise Cost-Sharing |

---

## 11. Stopping Rules

Frühzeitige Beendigung mit voller Disclosure wenn:

- ≥ 50% Unternehmen ausscheiden
- Inter-Rater κ < 0,40 (Methodik inkonsistent → Scale braucht Redesign)
- IRB widerrufen
- Ernsthafte Ethik-Issues (Daten-Leak, Participant Harm)

**Früh terminierte Studien müssen trotzdem alle gesammelten Daten publizieren** (Publication Bias vermeiden).

---

## 12. Erwartete Beiträge

| Beitrag | Audience | Form |
| --- | --- | --- |
| **Theorie**: erstes empirisch validiertes GenAI Adoption Maturity Modell | Akademia (IS / BPM / Strategy) | Peer-Reviewed Paper |
| **Methode**: Cases-as-Benchmarks + Client Ideal Practice Workshop Protocol | Consulting-Industrie | Open-Source Toolkit (Apache 2.0) |
| **Politik**: empirische Evidenz für AI Governance Alignment | Regulatoren (Taiwan AI Basic Act / NIST / EU) | White Paper + Legislative Hearings |
| **Industrie**: 5-10 Enterprise reale longitudinale Cases | Peer Clients | Reale Cases (ersetzen Composites) |
| **Bildung**: in akademische Partner-Curricula integrieren | Studenten | Kursmaterialien |

---

## 13. Verwandte Dokumente

| Dokument | Beziehung |
| --- | --- |
| [`../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md`](../01_Assessment/AI_MATURITY_SCORING_MODEL_EN.md) §3.1-3.3 | Scale Construct Definitionen; diese Studie validiert |
| [`../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md`](../00_Overview/METHODOLOGY_SCIENTIFIC_LOGIC_EN.md) | Warum Methodik empirische Validierung braucht |
| [`FAILURE_PATTERNS_EN.md`](FAILURE_PATTERNS_EN.md) | Bekannte Failure Modes → Mitigation in diese Studie eingebaut |
| [`../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md`](../03_Consulting_Report/CONSULTING_TOOLKIT_TEMPLATES_EN.md) Tool 8.9 | Evidence Hierarchy Basis für KPI Evidence Grading |

---

## 14. Referenzen

- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46.
- Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16(3), 297-334.
- Rosemann, M., de Bruin, T. (2005). *Towards a Business Process Management Maturity Model*. QUT.
- Streiner, D. L., Norman, G. R., & Cairney, J. (2015). *Health measurement scales: A practical guide to their development and use* (5th ed.). Oxford University Press.
- Hair, J. F., et al. (2019). *Multivariate Data Analysis* (8th ed.). Cengage.
- Creswell, J. W. (2018). *Research design: Qualitative, quantitative, and mixed methods approaches* (5th ed.). SAGE.
- Open Science Framework: <https://osf.io/>

---

Lizenz & Zitation

Dieses Dokument ist Apache License 2.0; darf verwendet, modifiziert, kommerzialisiert werden, vorausgesetzt die [`../NOTICE`](../NOTICE) Attribution wird beibehalten. Andere Forschungsteams können dieses Design **frei adoptieren, modifizieren, replizieren**, vorausgesetzt sie folgen denselben Pre-Registration und Open-Science Commitments.
