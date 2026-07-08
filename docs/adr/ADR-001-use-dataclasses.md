# ADR-001 - Utilisation des dataclasses

## Statut

Acceptée

## Date

2026-07-08

## Contexte

FindMyCar manipule plusieurs modèles métier (User, Search, Listing). Nous souhaitons représenter ces données de manière claire, typée et maintenable.

## Décision

Utiliser les dataclasses Python pour représenter les modèles métier.

## Alternatives étudiées

- Dictionnaires (`dict`)
- Classes Python classiques

## Conséquences positives

- Typage fort
- Meilleure lisibilité
- Autocomplétion dans les IDE
- Moins d'erreurs
- Modèles explicites

## Conséquences négatives

- Légèrement plus verbeux qu'un dictionnaire.

## Justification

Les modèles représentent le cœur du domaine métier. Leur clarté est prioritaire.