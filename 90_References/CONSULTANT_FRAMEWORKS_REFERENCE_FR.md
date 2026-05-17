# consultant Frameworks — Avis de citation & licence

> 🌐 Langue : [繁體中文](CONSULTANT_FRAMEWORKS_REFERENCE.md) ｜ [English](CONSULTANT_FRAMEWORKS_REFERENCE_EN.md) ｜ [Deutsch](CONSULTANT_FRAMEWORKS_REFERENCE_DE.md) ｜ Français ｜ [Español](CONSULTANT_FRAMEWORKS_REFERENCE_ES.md) ｜ [日本語](CONSULTANT_FRAMEWORKS_REFERENCE_JA.md) ｜ [한국어](CONSULTANT_FRAMEWORKS_REFERENCE_KR.md)

La liste de frameworks et la taxonomie dans le [`03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md`](../03_Consulting_Report/CONSULTING_FRAMEWORKS_LIBRARY.md) de cette méthodologie sont référencées et réécrites en se basant sur **yoichiojima-2/consultant**. Ce document enregistre la source upstream, les termes de licence, l'orientation de citation et le scope d'adaptation.

---

## 1. Projet upstream

| Champ | Valeur |
| --- | --- |
| **Projet** | consultant |
| **Mainteneur** | @yoichiojima-2 |
| **URL GitHub** | <https://github.com/yoichiojima-2/consultant> |
| **Licence** | **MIT License** |
| **Forme** | Plugin Claude Code (installé via `/plugin marketplace add`) |
| **Contenu** | 50+ frameworks classiques de consulting (McKinsey / BCG / Bain / Accenture) sur 7 catégories, empaquetés comme skill markdown |

## 2. Ce qu'est consultant

consultant est un **plugin Claude Code** qui empaquète 50+ frameworks classiques de consulting management (MECE, Pyramid Principle, Porter's 5 Forces, SWOT, BCG Matrix, PESTEL, 5 Whys, Fishbone, Business Model Canvas, WBS, RACI, Kotter, OKR, NPV/IRR, Lean, Six Sigma, etc.) dans un skill markdown.

### Caractéristiques structurelles

- **Taxonomie à 7 catégories** : problem solving / strategy analysis / case frameworks / business design / project & change / financial analysis / operations.
- **Reconnaissance de trigger** : route les phrases en langage naturel « j'ai besoin de… » vers une combinaison de frameworks.
- **Combinaisons de frameworks** : chaînes multi-framework pré-construites (ex. PESTEL → 5 Forces → 3C → SWOT → Issue Tree).
- **Structure standard par framework** : origine / concept core / étapes / comment appliquer / exemple réel / pièges courants.

## 3. Ce que nous avons adapté et cité

| Scope | Traitement |
| --- | --- |
| **Liste de frameworks et taxonomie à 7 catégories** | Taxonomie référencée, réécrite dans le langage de cette méthodologie |
| **Le concept « framework selector »** (langage naturel → framework) | Pattern de reconnaissance de trigger adapté en un selector aligné sur les scénarios de cette méthodologie |
| **Le concept « framework combination chains »** | Pattern de combination-chains adapté, mappé sur les huit stades de cette méthodologie |
| **Format d'expansion par framework** | Structure par framework référencée, ajout d'une colonne « maps-to-stage » |
| **Les frameworks classiques eux-mêmes** (MECE, Porter's 5 Forces, etc.) | Connaissance de management du domaine public, pas propriétaire à consultant |
| **Les fichiers skill markdown originaux** | **Non reproduits, non forkés** ; cette méthodologie est une réécriture indépendante |

## 4. Résumé de la licence

consultant est publié sous **MIT License**, qui permet usage libre, modification, redistribution et usage commercial, y compris comme partie d'un produit propriétaire ; la seule condition est de préserver l'avis de copyright MIT et le texte de licence lors de la redistribution de la source.

Cette méthodologie **ne redistribue pas** le code source de consultant — elle a réécrit `CONSULTING_FRAMEWORKS_LIBRARY.md` indépendamment après avoir référencé la liste de frameworks et les design patterns de consultant. Le fichier réécrit est sous licence Apache 2.0 de ce repo ; néanmoins, nous **notons explicitement la source de citation** dans ce fichier et ici, en respect de la contribution de l'auteur original.

## 5. Format de citation pour les apprenants

> Bibliothèque de frameworks adaptée de consultant par @yoichiojima-2 — <https://github.com/yoichiojima-2/consultant> (MIT License)

## 6. Disclaimer

Toute citation, adaptation ou mapping huit-stades de consultant dans cette méthodologie représente l'interprétation de l'auteur de la méthodologie (Morris Lu / Tiger AI 虎智科技) et ne représente pas la position officielle de @yoichiojima-2. Pour les définitions et l'application des frameworks classiques de consulting, référer à la source académique / industrielle originale de chaque framework. Si la liste de frameworks ou la structure de consultant change dans des versions plus récentes, voir le [repository upstream](https://github.com/yoichiojima-2/consultant).
