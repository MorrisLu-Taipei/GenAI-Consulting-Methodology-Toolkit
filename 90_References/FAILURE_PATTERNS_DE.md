# Failure Patterns & Counter-Cases: Wann die Tiger AI Methodik nicht angewendet werden sollte / fehlschlagen wird

> 🌐 Sprache: [繁體中文](FAILURE_PATTERNS.md) ｜ [English](FAILURE_PATTERNS_EN.md) ｜ Deutsch ｜ [Français](FAILURE_PATTERNS_FR.md) ｜ [Español](FAILURE_PATTERNS_ES.md) ｜ [日本語](FAILURE_PATTERNS_JA.md) ｜ [한국어](FAILURE_PATTERNS_KR.md)
>
> Apache License 2.0 · Autor: Morris Lu · Tiger AI

Letzte Aktualisierung: 2026-05-16

---

> **Zweck**: Eine Methodik, die nur Erfolg diskutiert, ist Verkaufsmaterial. Akademische / regulatorische / ernsthafte Kunden fragen: „**Wann scheitert sie? Wann sollte sie nicht angewendet werden? Was geht schief, wenn Levels übersprungen werden?**" Dieses Dokument hält bekannte Failure Patterns und Counter-Cases öffentlich fest, als harter Beweis für die Kritikfähigkeit und Verbesserbarkeit der Methodik.

---

## 1. Warum eine Methodik Failure Modes veröffentlichen muss

| Zielgruppe | Warum sie Failures sehen muss |
| --- | --- |
| **Akademische Reviewer** | Nur-Erfolgs-Cases = Selection Bias → nicht publizierbar |
| **Regulatoren** | Risikobewertung muss Failure Modes + Early-Warning-Bedingungen einschließen |
| **Ernsthafte Kunden** | „**Sagt mir, wann ihr scheitert**" ist die echte Vertrauensfrage |
| **Berater** | Failure Modes = institutionelles Gedächtnis = Wiederholung vermeiden |

> Eine Methodik, die **nur Erfolg diskutiert**, ist weniger vertrauenswürdig als eine, die **Scheitern eingesteht**.

---

## 2. Level-Skipping-Failures

### 2.1 L1 überspringen → Sprung zu L4 Agent

**Symptome**: Keine unternehmensweite L1-Adoption. Boss sieht Agent-Demo und will einen Customer-Service-Agent. 3 Engineers bauen einen Agent in 3 Monaten. Sobald live: CS-Personal hat Angst, ihn zu nutzen, QC unterschreibt nicht, IT weiß nicht, wie Audit-Logs verkabelt werden, Compliance fragt „wer trägt das Risiko".

**Wurzelursache**: Personal hat kein **persönliches Vertrauen** durch L1 aufgebaut; keine L2 Skill Library → Agent fehlt „unternehmens-geschriebene Urteilslogik"; kein L3 Workflow → Agent hat keine legalen Pipes, um auf Systeme zu wirken; keine L1-L3 Governance-Foundation → Agent geht live als Compliance Black Box.

**Typisches Ende**: Agent in 6 Monaten stillgelegt; IT-Vize wird beschuldigt; AI-Budget gekürzt.

### 2.2 L2 überspringen → L3 Workflow direkt bauen

**Symptome**: IT schaut n8n-Tutorials → baut Gmail → CRM → Slack-Chains. Monat 1: funktioniert. Personal beschwert sich „Outputs sind off-tone / zitieren unsere SOPs nicht". Engineers tunen Prompts, aber **jeder Workflow hat 10 Prompts über n8n-Nodes verstreut — kein Owner, keine Version, keine Docs**.

**Wurzelursache**: Keine L2 Skill Library als „unternehmens-geschriebene Prompts + Urteil + Daten" → L3 wird „persönlicher Prompt-Playground des IT-Engineers".

**Typisches Ende**: Workflow-Qualität driftet über die Zeit; 3 Monate später bittet Business Unit um Revert; IT verliert Vertrauen.

### 2.3 L3 / L4 ohne HITL

**Symptome**: Workflow sendet automatisch Customer-Emails, erstellt automatisch Rechnungen, platziert automatisch Bestellungen. Monat 1: 70% Effizienzgewinn. Monat 2: LLM-Halluzination → falsch-bepreistes Angebot an Tier-A-Kunde → NT$ 3M Vertrag verloren.

**Wurzelursache**: Alle AI haben ~0,5-3% Halluzinationsrate. **Kein HITL = trifft früher oder später ein Zero-Tolerance-Szenario**.

**Typisches Ende**: C-Suite verbietet AI; AI Champion wird bestraft; Methodik als „unzuverlässig" gelabelt.

### 2.4 Rushing L5 ClawTeam vor L4-Stabilisierung

**Symptome**: Boss sieht Multi-Agent-Demo, will Sales + CS + QC Cross-Dept Agent Team. Kein einziger Agent hat Stage Gate 4A-4E bestanden, aber 3 Agents werden verkettet. Evidence Trail bricht über Agents → niemand kann Entscheidungen tracen.

**Wurzelursache**: Single Agent ungoverned → Multi-Agent muss Kontrolle verlieren (niemand kann festnageln, welcher Agent welches Problem verursachte).

**Typisches Ende**: Projekt löst sich in 6 Monaten auf; fällt zurück auf Single Agents; ein halbes Jahr verschwendet.

---

## 3. Organizational-Misfit-Failures

### 3.1 Kein AI Champion (Executive Driver)

**Vorbedingung**: Jede Phase braucht mindestens einen Champion, der „cross-dept koordinieren, entscheiden, an Sponsor reporten" kann.

**Failure**: CEO unterschreibt Phase A, ernennt aber keinen Champion → Abteilungsleiter schieben sich gegenseitig Schuld zu während Interviews → As-Is unvollständig → Phase A Qualität schlecht → Kunde unterschreibt Phase B nicht.

**Tiger AI Ablehnung**: Wenn kein Champion vor Phase B in Place ist, **sollte Berater Unterschrift verweigern** oder Champion-Ernennung zuerst verlangen.

### 3.2 IT-Kapazität für L3+ unzureichend

**Vorbedingung**: L3 Workflow + L4 Agent brauchen 0,5-2 IT FTE für laufende Wartung.

**Failure**: Unternehmen hat 1 IT-Person, bereits maxed mit ERP / Netzwerk / Helpdesk. 5 Workflows gehen live → niemand wartet sie → 50% scheitern in 6 Monaten → Personal kehrt zu manuell zurück.

**Tiger AI Ablehnung**: Wenn Tool 6.3 Organizational Absorption „IT FTE" < Phase 2 Minimum (0,5 FTE dedicated), **Kunde dringend raten, zuerst IT hinzuzufügen**.

### 3.3 Unzureichende Compliance / Regulierung (Sensitive Industries)

**Vorbedingung**: Financial / Healthcare / Government / Legal haben starke Compliance-Anforderungen.

**Failure**: Krankenhaus deployt CS AI ohne HIPAA / PIPA / Patient-Rechte-Review → wird 3 Monate später vom Gesundheitsministerium auditiert → AI gezogen, bestraft, in den Nachrichten → nicht nur AI-Plan scheitert, sondern gesamte IT-Governance wird in Frage gestellt.

**Tiger AI Ablehnung**: Sensitive Industries ohne dedizierten Compliance Officer / Anwalt-Review → **Phase A End-Report muss „Compliance unverified → Phase B aussetzen" markieren**.

### 3.4 Executive-Turnover bricht 24-Monats-Roadmap

**Vorbedingung**: Phase C 24 Monate braucht stabile Sponsor-Unterstützung.

**Failure**: Phase A von CEO unterschrieben; CEO geht in Monat 9 von Phase C → neuer CEO ist nicht einverstanden → Phase C eingefroren → NT$ 9,8M investiert, partielle Outputs (L1-L3) behalten, aber L4-L5 aufgegeben.

**Tiger AI Mitigation**: Phase C Quarterly Gate C Exit-Mechanismus = selbst wenn Sponsor wechselt, ist jedes Quartal unabhängig re-evaluierbar, nicht Sunk-Cost-All-Lost.

---

## 4. Bekannte Methodik-Limitationen

### 4.1 Scoring-Modell fehlt psychometrische Validierung

**Status**: 6 Constructs × 0-4 Skala und L1-L5 Grenzen sind **Expertenkonsens**, **noch nicht validiert** via Cronbach's α / EFA / CFA / Inter-Rater Reliability.

**Potenzielle Probleme**:

- Zwei Berater, die dasselbe Unternehmen scoren, können L2 vs L3 yielden
- „50-60 = L2 Grenze vs 41-60 = L2" fehlt empirische Basis
- Constructs können Kollinearität haben; tatsächliche Faktor-Anzahl kann sich unterscheiden

**Tiger AI Antwort**: Report markiert explizit „Expert-Consensus-Version, ausstehend psychometrische Validierung"; `PILOT_STUDY_PROTOCOL.md` plant empirische Forschung; akademische Submissions sollten Claim-Strength auf „a proposed framework" senken.

### 4.2 Case Library Evidence Level

**Status**: 7 Cases sind **anonymisierte Composites** mit Evidence Level 2 (per Tool 8.9).

**Potenzielle Probleme**: Kunden können fragen „sind diese Zahlen real oder fabriziert?" ROI ~358%, Defekt-Rate 3,2 → 2,0% **kann nicht als vertragliche Commitments für einen einzelnen Kunden verwendet werden**.

**Tiger AI Antwort**: Jeder Case-Header markiert Evidence Level und Composite-Natur; SOW verwendet Kunden-eigene Baseline, nicht Case-Zahlen; schrittweise mit echten L3-L5 longitudinalen Cases ersetzen.

### 4.3 Tiger AI L1-L5 Recognition noch neu

**Status**: Tool 2.5 Self-Qualification 9/10; Condition 6 (breite Branchen-Recognition) ist △ partial.

**Potenzielle Probleme**: Initial-Kontakte fragen „APQC, SCOR sind international anerkannt — durch welche Autorität Tiger AI L1-L5?" Akademische Zitationen haben noch keine kritische Masse erreicht.

**Tiger AI Antwort**: Open-Source (Apache 2.0 + GitHub); proaktiv mit ISO/IEC Working Groups / IEEE AI Maturity Standards Diskussionen engagieren; Joint Research mit QUT, NTUST aufbauen.

---

## 5. Consultant-Level Anti-Patterns (Internal Failures)

### 5.1 Phase A überspringen → Phase B-C direkt unterschreiben

**Symptome**: Verkaufsdruck → Phase A überspringen → 6-Monats-Engagement direkt unterschreiben.
**Ergebnis**: Kein client-signiertes As-Is / RM / Ideal → in Stage 4+ kann Kunde verleugnen „das ist nicht, was wir wollten" → Berater in der Defensive.
**Disziplin**: **Phase A nie überspringen**. Es ist der Anker für alles danach.

### 5.2 Das Ideal Practice des Kunden für ihn entwerfen

**Symptome**: Berater entwirft Ideal Practice für Kunden zur Unterschrift, um Zeit zu sparen.
**Ergebnis**: Kunde fühlt keine Ownership → fordert später jeden Punkt heraus → Reasoning-Chain kollabiert.
**Disziplin**: **Tool 3.6 Co-Creation Workshop 6 Schritte müssen durchgeführt werden**. Unabhängiges Voting, kollektiver Konsens, Reality Check, Definition Table, 3-Parteien-Unterschrift — kein Schritt darf übersprungen werden.

### 5.3 Report basiert nur auf L1 Self-Report

**Symptome**: Eilige Schreiberei → alle Schlussfolgerungen aus Client-Self-Questionnaire.
**Ergebnis**: Auditiert von Client Internal Audit / Parent Company → „insufficient evidence" → volles Projekt zurückgegeben.
**Disziplin**: Per Tool 8.9 Evidence Hierarchy, **jede Hauptkonklusion braucht L3+ (System Log) Support**. Jeder Absatz markiert `[E:L#]`.

### 5.4 Risk in Gap Analysis mischen

**Symptome**: Stage 4 Kapitel mischt „dieses Risiko ist hoch, nicht empfohlen" subjektives Urteil.
**Ergebnis**: Stage 4 wird subjektiv → Kunde challenged „warum denkst du, das ist riskant" → Kapitel umgeschrieben.
**Disziplin**: **Stage 4 = objektives Gap-Inventory, KEINE Risk Assessment**. Risk gehört zu Stage 8 Risk Register.

### 5.5 Quarterly Stage 2 Radar Revisit bei Gate C überspringen

**Symptome**: Während Implementierung, fokussiert auf PoCs, berichtet nur Progress jedes Quartal, kein Radar-Revisit.
**Ergebnis**: PoCs erledigt, aber strukturelle Vollständigkeit unverändert → 24 Monate später „haben wir tatsächlich verbessert?" unbeantwortbar.
**Disziplin**: **Quarterly Gate C muss Radar revisiten**. Nicht tun = Berater-Negligenz.

---

## 6. Hard Refusal Conditions

Tiger AI **sollte ablehnen**, Phase C unter diesen Bedingungen zu unterschreiben (selbst wenn Kunde es will):

- [ ] **Phase A + B nicht abgeschlossen** → kein signiertes Ideal Practice → Phase C ablehnen
- [ ] **Kein AI Champion bestätigt in Place** → Phase C ablehnen
- [ ] **IT FTE unzureichend für Target-Phase** → dringend empfehlen Delay + IT zuerst hinzufügen
- [ ] **Sensitive Industry ohne Compliance Officer / Anwalt-Review** → Phase C ablehnen
- [ ] **Sponsor nicht in Place (keine klare CEO-Unterstützung)** → Phase C ablehnen
- [ ] **Kunde will Levels überspringen (z.B. L1-L3 → L4-L5 überspringen)** → ablehnen, Phase 1 Foundation verlangen
- [ ] **Budget unzureichend für aktuelle Phase** → ablehnen, Scope-Reduktion raten

---

## 7. Customer Exit Protocol

Falls irgendeine Phase A / B / C scheitert, Tiger AI committed sich:

1. **Phase A Failure**: Kunde behält Mid-Engagement-Report + Interview Summaries + Radar → **kann selbst ausführen oder nächsten Berater anheuern**
2. **Phase B Failure**: Voller Report + signierte Ideal Practice Table erhalten → **kann an anderen Berater transferieren**
3. **Phase C Mid-Failure (Quarterly Gate C Entscheidung zu stoppen)**: Vollendete Phases erhalten + Governance Docs erhalten + Code / Skills / Workflows vollständig an Kunden transferiert (Berater **hält keine Client-Assets**)
4. **Keine Geiselnahme von Client-Assets**: per [`../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md`](../06_Delivery/ENGAGEMENT_LIFECYCLE_EN.md) 7 Pillars #1 „Client Hosts"

---

## 8. Wie man dieses Dokument verwendet

| Rolle | Verwendung |
| --- | --- |
| **Berater-internes Training** | Pflicht-Onboarding-Lektüre; quartalsweises Team-Review „welche Failure Patterns haben wir letztes Quartal getroffen" |
| **Vor Unterschrift mit Kunde** | Berater teilt dieses Doc proaktiv → Kunde vertraut „dieser Berater verkauft nicht nur Erfolg, diskutiert Failure ehrlich" |
| **Akademische Submissions** | Als Evidenz für Methodik-Kritikalität / Falsifizierbarkeit zitieren |
| **Regulatorische / Bid-Dokumente** | Als Risikobewertung + Mitigation Evidenz beifügen |

> **Failure ehrlich diskutieren = höchste Form von Sales Skill**. Kunden kaufen nicht „garantierten Erfolg", sondern „wir wissen, was zu tun ist, wenn es scheitert".

---

Lizenz & Zitation

Dieses Dokument ist Apache License 2.0; darf verwendet, modifiziert, kommerzialisiert werden, vorausgesetzt die [`../NOTICE`](../NOTICE) Attribution wird beibehalten.
