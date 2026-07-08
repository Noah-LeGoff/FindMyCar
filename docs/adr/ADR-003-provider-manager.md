# ADR-003 - ProviderManager

## Statut

Acceptée

## Date

2026-07-08

## Contexte

Le SearchEngine doit pouvoir interroger plusieurs providers sans connaître leur implémentation.

## Décision

Créer une classe ProviderManager responsable de coordonner les providers.

## Alternatives étudiées

- Le SearchEngine appelle directement chaque provider

## Conséquences positives

- Découplage
- Ajout de nouveaux providers sans modifier le SearchEngine
- Possibilité d'ajouter plus tard du parallélisme, des retries ou des métriques

## Conséquences négatives

- Une couche supplémentaire dans l'architecture

## Justification

Le SearchEngine doit rester concentré sur son rôle d'orchestrateur.