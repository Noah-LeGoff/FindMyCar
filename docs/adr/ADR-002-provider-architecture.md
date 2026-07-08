# ADR-002 - Architecture des Providers

## Statut

Acceptée

## Date

2026-07-08

## Contexte

Le projet devra récupérer des annonces provenant de plusieurs sources (Leboncoin, AutoScout24, La Centrale, etc.).

## Décision

Chaque source implémentera une interface commune `BaseProvider`.

## Alternatives étudiées

- Un unique scraper géant
- Une classe différente sans interface commune

## Conséquences positives

- Ajout simple de nouveaux providers
- Architecture modulaire
- Faible couplage

## Conséquences négatives

- Quelques classes supplémentaires

## Justification

Cette approche respecte le principe Open/Closed et facilite l'évolution du projet.