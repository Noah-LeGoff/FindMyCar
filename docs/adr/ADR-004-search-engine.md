# ADR-004 - SearchEngine comme orchestrateur

## Statut

Acceptée

## Date

2026-07-08

## Contexte

Le moteur doit coordonner plusieurs traitements (providers, déduplication, matching, scoring, notifications).

## Décision

Le SearchEngine orchestre les traitements sans contenir leur logique métier.

## Alternatives étudiées

- Centraliser toute la logique dans le SearchEngine

## Conséquences positives

- Respect du principe de responsabilité unique
- Services indépendants
- Tests plus simples

## Conséquences négatives

- Plus de classes

## Justification

Chaque traitement évoluera indépendamment au fil du projet.