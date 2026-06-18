# Buch II AI Prompt Pack (Lieferung von Beratungsprojekten)

> 🌐 Sprache: [繁體中文](AI_PROMPT_PACK_DELIVERY.md) ｜ [English](AI_PROMPT_PACK_DELIVERY_EN.md) ｜ **Deutsch**
> Gegenstück zum [`11_AI_Prompt_Pack.md`](https://github.com/MorrisLu-Taipei/consultant-thinking-framework/blob/main/11_AI_Prompt_Pack.md) aus Buch I. Das Pack aus Buch I trainiert *Urteilsvermögen*; dieses Pack treibt dieses Urteilsvermögen durch jede Phase der *Lieferung*.
> Gemeinsame Disziplin: **Signal von Schlussfolgerung trennen, niemals erfinden, Unbestätigtes als „zu bestätigen" kennzeichnen, Kundendaten nur mit freigegebener KI / privaten Endpunkten verarbeiten.**

---

## Verwendung
Fügen Sie Kundendaten / Interviewnotizen in das `{{ }}` des jeweiligen Prompts ein oder lösen Sie über die `consulting-delivery-coach`-Skill aus. Jeder Prompt fordert die KI auf, **die Evidenzquelle zu zitieren** und **die Grundlage für das L-Level anzugeben**.

---

### 1. Kundenprofil → vorläufiges L-Level
```
Du bist ein Diagnose-Berater für KI-Transformation. Gib aus dem folgenden Kundenhintergrund ein vorläufiges L1-L5-Reifegrad-Urteil ab.
Regel: Verknüpfe jedes Urteil mit konkreter Evidenz im Hintergrund; kennzeichne Dimensionen mit unzureichender Evidenz als „zu diagnostizieren" — rate nicht.
Ausgabe: vorläufiges L-Level + die 3 wichtigsten Folgefragen.
Kundenhintergrund: {{einfügen}}
```

### 2. Interviewnotizen → Phase-A-Diagnosezusammenfassung
```
Wandle das folgende Interview-Transkript in eine Phase-A-Diagnosezusammenfassung um.
Struktur: (1) wörtliche Aussagen des Kunden (Fakten) (2) wahre Schmerzpunkte (Oberfläche → Wurzel) (3) das aktuelle job-to-be-done (4) die Diagonale (diagonal) (blinder Fleck des Wettbewerbers × künftiger Bedarf des Kunden × unser Einstieg) (5) Evidenzlücken (mit „zu bestätigen" kennzeichnen).
Füge nichts hinzu, was nicht im Transkript steht.
Transkript: {{einfügen}}
```

### 3. Diagnose → Empfehlung zur Kursgestaltung
```
Empfiehl aus der folgenden L-Level-Diagnose einen L1-L5-Kurspfad.
Regel: Entscheide zuerst, ob dem Kunden Fähigkeit / Prozess / Governance / Werkzeug fehlt, und gestalte dann den Kurs; erkläre die Reihenfolge.
Ausgabe: Kurspfad + Zielergebnis pro Stufe + Risiken.
Diagnose: {{einfügen}}
```

### 4. Diagnose → Gliederung des Beratungsberichts
```
Wandle die folgende Diagnose in eine achtstufige Gliederung des Beratungsberichts um.
Muss enthalten: Executive Problem Statement (aus der Diagonale (diagonal) geschrieben), Roadmap, Risk Register, Stage Gate Criteria.
Zitiere für jede Schlussfolgerung eine Evidenzquelle (evidence); formuliere nichts ohne Evidenz als Schlussfolgerung.
Diagnose: {{einfügen}}
```

### 5. Roadmap → Liefer-Checkliste
```
Wandle die folgende Roadmap in eine abnahmebereite Liefer-Checkliste um.
Regel: Jeder Punkt benötigt ein „Abnahmekriterium" (was als erfolgreiche Lieferung gilt) + „liefert dies Fähigkeit oder ein Werkzeug". Kennzeichne reine Werkzeug-Punkte mit einer Warnung.
Roadmap: {{einfügen}}
```

### 6. Projektstatus → Risiken und nächster Schritt
```
Du bist ein Projekt-Reviewer. Liste aus dem folgenden Projektstatus die Risiken und den nächsten Schritt auf.
Fokus: Scope Creep, ob ein Stage Gate ausgelöst werden sollte, Risiko der Schlusszahlung, ob sich die Struktur des Kunden tatsächlich verbessert hat.
Ausgabe: Top-3-Risiken + empfohlener nächster Schritt + ob die nächste Phase A/B/C betreten werden soll.
Status: {{einfügen}}
```

---

## Sicherheits- und Ehrlichkeitshinweis
- Verarbeite Kundendaten nur mit **unternehmensfreigegebener KI oder einem privaten Endpunkt**; füge sie niemals in öffentliche Dienste ein.
- Ein menschlicher Berater prüft jede KI-Ausgabe; **alles, was mit „zu bestätigen" gekennzeichnet ist, darf nicht als Schlussfolgerung geliefert werden**.
- Anonymisiere externe Fälle („Company ABC" / „City X"). Dieses Pack ist ein Werkzeug, kein endgültiger rechtlicher / finanzieller / sicherheitstechnischer Rat.
