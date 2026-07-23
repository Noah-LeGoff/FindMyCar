# RFC-005 — Final Scoring Architecture

## Status

Proposed

## Date

2026-07-23

## Author

FindMyCar Team

---

# 1. Context

FindMyCar possède actuellement plusieurs moteurs de scoring indépendants :

- CompatibilityScorer
- OpportunityScorer

Ces moteurs évaluent deux dimensions différentes d'une annonce :

- La compatibilité avec la recherche utilisateur.
- L'intérêt de l'annonce sur le marché.

Cependant, il n'existe actuellement aucun système permettant de combiner ces résultats afin de produire :

- une note finale ;
- un classement des annonces ;
- une explication claire du résultat.

Cette RFC définit l'architecture du score final de FindMyCar.

---

# 2. Philosophy

Le score FindMyCar ne représente pas la qualité absolue d'une voiture.

Il représente :

> La pertinence d'une annonce pour une recherche utilisateur donnée.

Une voiture exceptionnelle peut obtenir un mauvais score si elle ne correspond pas aux critères recherchés.

Exemple :

Une Ferrari F40 peut être une voiture exceptionnelle, mais elle obtiendra un score faible pour une recherche :

- budget : 10 000 €
- diesel
- moins de 150 000 km

Le score ne juge jamais la voiture.

Il juge son adéquation avec le besoin utilisateur.

---

# 3. Goals

Le système final doit :

- produire une note comprise entre 0 et 100 ;
- combiner compatibilité et opportunité ;
- conserver l'explication complète du score ;
- permettre un classement des annonces ;
- rester évolutif ;
- éviter les scores opaques.

---

# 4. Non Goals

Cette RFC ne définit pas :

- le fonctionnement interne des critères individuels ;
- l'analyse de marché ;
- les modèles IA ;
- le système de recherche.

Ces éléments sont traités dans d'autres RFC.

---

# 5. Final Score Model

Le score final est composé de deux grandes parties :

Final Score = Compatibility Score + Opportunity Score

Chaque partie possède un poids différent.

---

# 6. Weighting System

## Compatibility

Poids : 75%

La compatibilité est prioritaire.

Elle représente la capacité de l'annonce à répondre aux besoins exprimés par l'utilisateur.

Exemples :

- budget ;
- kilométrage ;
- année ;
- carburant ;
- boîte ;
- nombre de portes.

---

## Opportunity

Poids : 25%

L'opportunité représente la valeur potentielle de l'annonce.

Exemples :

- prix inférieur au marché ;
- rareté ;
- entretien intéressant ;
- fraîcheur de l'annonce.

---

# 7. Score Calculation

Chaque sous-score est normalisé avant combinaison.

Exemple :

CompatibilityScore = 72 / 75

OpportunityScore = 18 / 25

FinalScore = 90 / 100

Le score final doit toujours être compris entre :

0 <= score <= 100

---

# 8. Score Explainability

Le score final doit toujours conserver ses détails.

Un score ne doit jamais être représenté uniquement par un nombre.

Mauvais exemple :

```python
score = 91
```

Bon exemple :

```python
FinalScore(
    total=91,

    compatibility=72,

    opportunity=19,

    compatibility_breakdowns=[...],

    opportunity_breakdowns=[...],
)
```

L'utilisateur doit pouvoir comprendre :

- pourquoi une annonce est bien classée ;
- quels sont ses points forts ;
- quels sont ses points faibles.

---

## 9. No Negative Scores

Le système n'utilise jamais de score négatif.

Un critère peut :

- apporter des points ;
- ne rien apporter.

Il ne doit jamais dégrader le score en dessous de zéro.

Cette règle permet :

- une meilleure compréhension utilisateur ;
- une meilleure stabilité du système.

---

## 10. Score Recalculation

Les scores ne sont jamais considérés comme définitifs.

Ils doivent être recalculés lorsque :

- une nouvelle recherche est effectuée ;
- une annonce est modifiée ;
- de nouvelles données sont disponibles.

Le score représente toujours l'état actuel des informations disponibles.

---

## 11. Equality Management

Deux annonces peuvent avoir exactement le même score.

Exemple :

BMW E36 : 92/100

Honda Civic : 92/100

Le système ne doit pas créer artificiellement des différences.

Les égalités sont acceptées.

Un tri secondaire pourra éventuellement être ajouté plus tard.

---

## 12. Recommendation System

Le score final pourra être accompagné d'une recommandation utilisateur.

Cette recommandation n'est pas un nouveau calcul.

Elle est uniquement une interprétation du score.

Version V1 :

Score	Recommendation
95-100	Exceptional choice
85-94	Excellent choice
70-84	Very interesting
55-69	Worth considering
40-54	Low interest
0-39	Avoid

---

## 13. Architecture

Le flux global devient :

```
Search

    |
    v

CompatibilityScorer

    |
    v

OpportunityScorer

    |
    v

ScoreAggregator

    |
    v

FinalScore

    |
    v

RankingService
```

---

## 14. Main Components

### FinalScore

Responsabilité :

Représenter le résultat final d'une annonce.

Contient :

- score total ;
- score de compatibilité ;
- score d'opportunité ;
- détails des critères ;
- recommandation.

### ScoreAggregator

Responsabilité :

Combiner les résultats des différents moteurs.

Il ne contient aucune logique métier de critère.

Il applique uniquement les règles de pondération.

### RankingService

Responsabilité :

Classer plusieurs annonces selon leur FinalScore.

Il ne calcule pas les scores.

Il utilise uniquement les résultats existants.

---

## 15. Future Improvements

### Dynamic Weighting

Version future :

Permettre de modifier les poids selon le profil utilisateur.

Exemple :

Utilisateur passionné :

Compatibility : 60%
Opportunity : 40%

Utilisateur pratique :

Compatibility : 85%
Opportunity : 15%
Explainability Engine

Version future :

Créer automatiquement un résumé :

"Cette BMW E36 est classée première car elle respecte parfaitement votre budget, possède un historique d'entretien complet et son prix est inférieur de 18% au marché."

### User Preference Learning

Version future :

Adapter les poids automatiquement selon :

les voitures consultées ;
les favoris ;
les achats réalisés.

---

## 16. Conclusion

Le score final représente la philosophie principale de FindMyCar :

Trouver la voiture la plus pertinente pour une personne donnée, et expliquer clairement pourquoi.

Le système ne cherche pas simplement la voiture la moins chère ou la mieux notée.

Il cherche la meilleure décision possible selon le contexte utilisateur.