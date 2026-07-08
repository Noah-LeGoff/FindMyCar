# ADR-005 - Workflow Git

## Statut

Acceptée

## Date

2026-07-08

## Contexte

Le projet est destiné à évoluer sur le long terme.

## Décision

Adopter un workflow simple avec deux branches :

- main
- dev

Le développement quotidien est réalisé sur `dev`. La branche `main` ne contient que des versions stables.

## Alternatives étudiées

- Développer directement sur main
- GitFlow complet

## Conséquences positives

- Historique plus propre
- Réduction des risques
- Déploiements plus simples

## Conséquences négatives

- Gestion d'une branche supplémentaire

## Justification

Ce workflow est suffisamment simple pour un projet personnel tout en restant proche des pratiques professionnelles.