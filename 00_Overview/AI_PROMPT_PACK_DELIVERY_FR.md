# Livre II AI Prompt Pack (Livraison de mission de conseil)

> 🌐 Langue : [繁體中文](AI_PROMPT_PACK_DELIVERY.md) ｜ [English](AI_PROMPT_PACK_DELIVERY_EN.md) ｜ **Français**
> Équivalent du [`11_AI_Prompt_Pack.md`](https://github.com/MorrisLu-Taipei/consultant-thinking-framework/blob/main/11_AI_Prompt_Pack.md) du Livre I. Le pack du Livre I entraîne le *jugement* ; ce pack fait passer ce jugement à travers chaque étape de la *livraison*.
> Discipline commune : **séparer le signal de l'inférence, ne jamais inventer, marquer le non vérifié comme « à confirmer », ne traiter les données client qu'avec une IA approuvée / des points de terminaison privés.**

---

## Mode d'emploi
Collez les données client / notes d'entretien dans le `{{ }}` de chaque prompt, ou déclenchez via la skill `consulting-delivery-coach`. Chaque prompt demande à l'IA de **citer la source de l'evidence** et d'**indiquer la base du niveau L**.

---

### 1. Profil client → niveau L préliminaire
```
Tu es un consultant en diagnostic de transformation par l'IA. À partir du contexte client ci-dessous, donne un jugement préliminaire de maturité L1-L5.
Règle : relie chaque jugement à une evidence précise dans le contexte ; marque les dimensions avec des preuves insuffisantes comme « à diagnostiquer » — ne devine pas.
Sortie : niveau L préliminaire + les 3 questions de suivi les plus importantes.
Contexte client : {{coller}}
```

### 2. Notes d'entretien → résumé de diagnostic Phase A
```
Transforme la transcription d'entretien ci-dessous en un résumé de diagnostic Phase A.
Structure : (1) les mots exacts du client (faits) (2) la vraie douleur (surface → racine) (3) le job-to-be-done actuel (4) la diagonale (diagonal) (angle mort du concurrent × besoin futur du client × notre point d'entrée) (5) lacunes d'evidence (marquer « à confirmer »).
N'ajoute rien qui ne figure pas dans la transcription.
Transcription : {{coller}}
```

### 3. Diagnostic → recommandation de conception de parcours
```
À partir du diagnostic de niveau L ci-dessous, recommande un parcours de cours L1-L5.
Règle : décide d'abord si le client manque de capacité / processus / gouvernance / outillage, puis conçois le parcours ; explique l'ordonnancement.
Sortie : parcours de cours + livrable cible par étape + risques.
Diagnostic : {{coller}}
```

### 4. Diagnostic → plan du rapport de conseil
```
Transforme le diagnostic ci-dessous en un plan de rapport de conseil en huit étapes.
Doit inclure : Executive Problem Statement (rédigé à partir de la diagonale (diagonal)), Roadmap, Risk Register, Stage Gate Criteria.
Cite une source d'evidence pour chaque conclusion ; n'énonce rien comme conclusion sans evidence.
Diagnostic : {{coller}}
```

### 5. Roadmap → checklist de livraison
```
Transforme la Roadmap ci-dessous en une checklist de livraison prête à la recette.
Règle : chaque élément nécessite un « critère de recette » (ce qui constitue une livraison réussie) + « cela livre-t-il une capacité ou un outil ». Signale les éléments purement outils.
Roadmap : {{coller}}
```

### 6. État du projet → risques et prochaine étape
```
Tu es un reviewer de projet. À partir de l'état du projet ci-dessous, liste les risques et la prochaine étape.
Focus : dérive du périmètre (scope creep), s'il faut déclencher un Stage Gate, risque sur le paiement final, si la structure du client s'est réellement améliorée.
Sortie : Top 3 des risques + prochaine étape recommandée + faut-il passer à la Phase A/B/C suivante.
État : {{coller}}
```

---

## Rappel de sécurité et d'honnêteté
- Ne traite les données client qu'avec une **IA approuvée par l'entreprise ou un point de terminaison privé** ; ne les colle jamais dans des services publics.
- Un consultant humain relit toute sortie de l'IA ; **tout ce qui est marqué « à confirmer » ne doit pas être livré comme conclusion**.
- Anonymise les cas externes (« Company ABC » / « City X »). Ce pack est un outil, pas un avis juridique / financier / de sécurité final.
