# RFC-002 - Scoring System

## Status

Accepted

## Author

FindMyCar Team

## Date

2026-07-08

---

# 1. Problem

Le système de recherche actuel permet uniquement de déterminer si une annonce correspond aux critères de recherche d'un utilisateur grâce au `MatchingService`.

Cependant, plusieurs annonces peuvent correspondre aux mêmes critères sans avoir la même valeur pour l'utilisateur.

Exemple :

Deux véhicules peuvent respecter une recherche "BMW E36 moins de 15 000€", mais :

* l'un peut avoir beaucoup de kilomètres ;
* l'autre peut avoir un historique complet et un entretien récent ;
* l'un peut être une mauvaise opportunité malgré son prix attractif ;
* l'autre peut être une excellente affaire malgré un prix supérieur.

Le rôle du `ScoringService` est donc de classer les annonces compatibles selon leur pertinence et leur intérêt réel.

---

# 2. Goals

Le système de scoring doit permettre de :

* classer les annonces compatibles ;
* identifier les meilleures opportunités ;
* expliquer pourquoi une annonce est recommandée ;
* être facilement modifiable et extensible ;
* permettre une personnalisation future selon les préférences utilisateur ;
* recalculer automatiquement les scores lorsque les informations évoluent.

Le score doit représenter :

> La pertinence globale d'une annonce pour un utilisateur à un instant donné.

---

# 3. Non Goals

Pour la première version, le système ne doit pas :

* remplacer l'expertise d'un mécanicien ;
* prédire parfaitement la valeur réelle d'un véhicule ;
* utiliser immédiatement du machine learning ;
* analyser automatiquement les photos ;
* prendre une décision d'achat à la place de l'utilisateur.

---

# 4. Scoring Model

Le système utilise deux scores complémentaires.

## 4.1 Compatibility Score

Le `Compatibility Score` répond à la question :

> "Est-ce que cette voiture correspond aux critères et préférences de l'utilisateur ?"

Il prend en compte :

* marque ;
* modèle ;
* version ;
* année ;
* kilométrage ;
* carburant ;
* boîte de vitesse ;
* équipements ;
* préférences utilisateur.

Exemple :

```
BMW E36 325i

Compatibility Score : 94%
```

---

## 4.2 Opportunity Score

Le `Opportunity Score` répond à la question :

> "Est-ce une bonne opportunité d'achat actuellement ?"

Il prend en compte :

* cohérence du prix ;
* évolution du prix ;
* ancienneté de l'annonce ;
* rareté ;
* qualité détectée ;
* historique d'entretien.

Exemple :

```
Opportunity Score : 87%
```

---

# 5. Final FindMyCar Score

Le score final affiché par FindMyCar combine les deux dimensions.

Formule initiale :

```
FindMyCar Score =
(Compatibility Score × 70%)
+
(Opportunity Score × 30%)
```

La compatibilité possède un poids supérieur car une excellente opportunité qui ne correspond pas au besoin de l'utilisateur ne doit pas être recommandée.

Exemple :

Une Porsche très sous-évaluée peut avoir un excellent Opportunity Score, mais si l'utilisateur recherche une voiture économique, son score global restera faible.

---

# 6. Scoring Criteria V1

Le score global est basé sur plusieurs critères.

| Critère                | Poids |
| ---------------------- | ----: |
| Rapport qualité/prix   |    25 |
| Kilométrage            |    15 |
| Année                  |    10 |
| Version / finition     |    15 |
| État et entretien      |    15 |
| Localisation           |     5 |
| Rareté / opportunité   |     5 |
| Fraîcheur de l'annonce |    10 |
| Total                  |   100 |

Ces valeurs pourront évoluer grâce aux futures versions du système.

---

# 7. Price Reliability

Le prix doit être analysé avec prudence.

Certaines annonces utilisent des prix artificiels :

* 0€ ;
* 1€ ;
* prix symbolique ;
* échange uniquement ;
* prix non renseigné.

Ces annonces ne doivent pas être automatiquement considérées comme de bonnes affaires.

Le système doit intégrer une notion de fiabilité du prix avant d'attribuer des points.

Exemple :

```
Prix valide :
    calcul normal

Prix suspect :
    pénalité ou absence de bonus
```

---

# 8. Vehicle Quality Analysis

La qualité d'un véhicule doit pouvoir influencer le score.

Exemples :

Bonus possibles :

* historique complet ;
* carnet d'entretien ;
* distribution récente ;
* embrayage récent ;
* pneus neufs ;
* freins récents ;
* pièces remplacées ;
* version rare.

Cependant, les informations doivent être différenciées selon leur niveau de confiance.

Exemple :

```
Information vérifiée :
    bonus important

Simple déclaration vendeur :
    bonus limité
```

---

# 9. AI Description Analysis

Une analyse automatique des descriptions pourra être ajoutée.

L'objectif est d'extraire des informations structurées depuis le texte.

Exemple :

Description :

```
Distribution faite en 2025,
pneus neufs,
embrayage changé.
```

Résultat attendu :

```json
{
    "maintenance": {
        "timing_belt": true,
        "tires": true,
        "clutch": true
    }
}
```

L'intelligence artificielle ne doit pas attribuer directement les points.

Architecture :

```
Description
      |
      v
AI Analyzer
      |
      v
Vehicle Facts
      |
      v
ScoringService
      |
      v
Score
```

---

# 10. Freshness Score

L'ancienneté d'une annonce influence la probabilité qu'elle représente une bonne opportunité.

Exemple :

| Age annonce    | Score |
| -------------- | ----: |
| 0-24h          |    10 |
| 1-7 jours      |     8 |
| 1 mois         |     5 |
| 3 mois         |     2 |
| 6 mois et plus |     0 |

Une ancienne annonce n'est pas automatiquement supprimée, mais elle doit être moins prioritaire.

---

# 11. Price Evolution

Le système doit conserver l'historique des prix.

Exemple :

```
01/07 : 15000€
05/07 : 14000€
08/07 : 12000€
```

Une baisse significative peut représenter une opportunité.

Le système pourra attribuer un bonus :

```
Baisse importante du prix :
    bonus opportunité
```

---

# 12. Dynamic Recalculation

Les scores ne sont pas permanents.

Ils doivent être recalculés lorsqu'un événement important survient :

* nouvelle annonce ;
* changement de prix ;
* modification des informations ;
* nouvelle analyse de description ;
* évolution des préférences utilisateur.

Un recalcul périodique pourra également être effectué automatiquement.

Exemple :

```
Nouvelle annonce
        |
        v
Matching
        |
        v
Scoring
        |
        v
Classement utilisateur
```

---

# 13. User Personalization

Le scoring doit être conçu pour supporter une personnalisation future.

Chaque utilisateur peut avoir des priorités différentes.

Exemple :

Utilisateur A :

```
Priorité :
- prix faible
- faible kilométrage
- distance réduite
```

Utilisateur B :

```
Priorité :
- rareté
- état exceptionnel
- historique complet
```

Un futur `UserPreferenceEngine` pourra apprendre les préférences grâce aux comportements :

* recherches ;
* clics ;
* favoris ;
* annonces ignorées ;
* contacts vendeur.

---

# 14. Architecture cible

L'architecture prévue :

```
Search
  |
  v
MatchingService
  |
  v
Compatible Listings
  |
  v
ScoringService
  |
  +----------------+
  |                |
  v                v
Compatibility   Opportunity
Score           Score
  |                |
  +-------+--------+
          |
          v
 FindMyCar Score
          |
          v
 Notifications
```

---

# 15. Decision

Le système de scoring sera développé comme un moteur extensible basé sur des critères indépendants.

La première version utilisera un système de règles pondérées.

Une évolution future pourra intégrer :

* analyse IA des descriptions ;
* apprentissage des préférences utilisateur ;
* adaptation automatique des poids ;
* analyse du marché automobile.
