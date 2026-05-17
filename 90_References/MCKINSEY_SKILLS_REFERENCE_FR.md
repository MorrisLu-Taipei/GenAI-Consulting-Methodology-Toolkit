# mckinsey-consultant-skills — Avis de citation & licence

> 🌐 Langue : [繁體中文](MCKINSEY_SKILLS_REFERENCE.md) ｜ [English](MCKINSEY_SKILLS_REFERENCE_EN.md) ｜ [Deutsch](MCKINSEY_SKILLS_REFERENCE_DE.md) ｜ Français ｜ [Español](MCKINSEY_SKILLS_REFERENCE_ES.md) ｜ [日本語](MCKINSEY_SKILLS_REFERENCE_JA.md) ｜ [한국어](MCKINSEY_SKILLS_REFERENCE_KR.md)

Le workflow de production dans le [`03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md`](../03_Consulting_Report/REPORT_PRODUCTION_WORKFLOW.md) de cette méthodologie est référencé et réécrit en se basant sur **Kafurtan/mckinsey-consultant-skills**. Ce document enregistre la source upstream, les termes de licence, l'orientation de citation et le scope d'adaptation.

---

## 1. Projet upstream

| Champ | Valeur |
| --- | --- |
| **Projet** | mckinsey-consultant-skills (V3.1) |
| **Mainteneur** | @Kafurtan |
| **URL GitHub** | <https://github.com/Kafurtan/mckinsey-consultant-skills> |
| **Licence** | **MIT License** |
| **Forme** | AI agent skill (`SKILL.md` + `references/`) |
| **Contenu** | Un workflow en 8 étapes qui automatise « problème business → présentation style McKinsey », end-to-end en 90-110 minutes |

## 2. Ce qu'est mckinsey-consultant-skills

Il systématise la méthodologie de Problem Solving de McKinsey en un **workflow en 8 étapes** qui permet à un assistant IA de transformer un problème business en présentation professionnelle (PPT + Excel evidence trail).

### Caractéristiques structurelles

- **Workflow en 8 étapes** : définir les frontières → Issue Tree + hypothèses → Dummy Pages + design specs → production itérative page par page → PPT + Excel → rapport Word optionnel → révision itérative.
- **Dummy Page** : construire la spec wireframe avant la recherche, pour éviter la collecte de données sans but et supporter la reprise entre conversations.
- **Conscience des dépendances** : les pages sont étiquetées avec statut de dépendance, déterminant l'ordre de production (l'executive summary est fait en dernier).
- **7 layouts de page** : titre + chart unique / deux colonnes / matrice 2×2 / tableau / waterfall chart / timeline / résumé d'insight.
- **Excel evidence trail** : par page raw data + URL + processus de nettoyage.
- **Progressive disclosure** : les fichiers de référence ne sont chargés qu'aux étapes qui en ont besoin et libérés après, économisant ~70% de contexte.
- `references/` : methodology.md, layouts.md, design-specs.md, examples.md, troubleshooting.md.

## 3. Ce que nous avons adapté et cité

| Scope | Traitement |
| --- | --- |
| **Le workflow de production en 8 étapes** | Workflow référencé, réécrit dans le langage de cette méthodologie, mappé sur la structure de conseil à huit stades |
| **Le concept Dummy Page** | Discipline « skeleton-first, fill-in-later » adaptée en specs par page pour les outlines de deck de cette méthodologie |
| **Conscience des dépendances** | Concept de gestion de dépendances de page adapté |
| **Les 7 layouts de page** | Liste de layouts référencée, réécrite pour étendre `VISUAL_ASSETS_SPEC.md` |
| **Excel evidence trail, progressive disclosure** | Concepts adaptés, mappés sur la discipline Evidence de cette méthodologie et gestion de contexte AI-IDE |
| **McKinsey Problem Solving, MECE, Pyramid Principle** | Connaissance de management du domaine public, pas propriétaire à ce projet |
| **Les fichiers `SKILL.md` et `references/` originaux** | **Non reproduits, non forkés** ; cette méthodologie est une réécriture indépendante |

## 4. Résumé de la licence

mckinsey-consultant-skills est publié sous **MIT License**, qui permet usage libre, modification, redistribution et usage commercial, y compris comme partie d'un produit propriétaire ; la seule condition est de préserver l'avis de copyright MIT et le texte de licence lors de la redistribution de la source.

Cette méthodologie **ne redistribue pas** son code source — elle a réécrit `REPORT_PRODUCTION_WORKFLOW.md` indépendamment après avoir référencé le workflow et les design patterns. Le fichier réécrit est sous licence Apache 2.0 de ce repo ; néanmoins, nous **notons explicitement la source de citation** dans ce fichier et ici, en respect de la contribution de l'auteur original.

## 5. Format de citation pour les apprenants

> Workflow de production adapté de mckinsey-consultant-skills par @Kafurtan — <https://github.com/Kafurtan/mckinsey-consultant-skills> (MIT License)

## 6. Disclaimer

Toute citation, adaptation ou mapping huit-stades de mckinsey-consultant-skills dans cette méthodologie représente l'interprétation de l'auteur de la méthodologie (Morris Lu / Tiger AI 虎智科技) et ne représente pas la position officielle de @Kafurtan. « McKinsey » est une marque de McKinsey & Company ; cette méthodologie n'a aucune affiliation ou endossement de McKinsey & Company, et les noms de méthodologie relatifs sont utilisés uniquement comme références à la connaissance de management du domaine public. Si le workflow ou la structure de mckinsey-consultant-skills change dans des versions plus récentes, voir le [repository upstream](https://github.com/Kafurtan/mckinsey-consultant-skills).
