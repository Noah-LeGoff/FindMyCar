# FindMyCar Modules

## Introduction

FindMyCar est conçu comme une plateforme modulaire.

Chaque module possède une responsabilité clairement définie et peut évoluer indépendamment des autres.

Cette approche permet de faire évoluer progressivement le produit sans remettre en cause son architecture générale.

Ce document présente l'ensemble des modules existants ainsi que ceux envisagés à long terme.

---

# Légende

| Statut | Signification |
|----------|---------------|
| ✅ | Disponible |
| 🚧 | En développement |
| 📋 | Planifié |
| 💡 | Idée / Vision long terme |

---

# Priorité stratégique

| Priorité | Signification |
|-----------|---------------|
| 🔴 | Critique – Indispensable au fonctionnement du MVP. |
| 🟠 | Haute – Très importante après le MVP. |
| 🟡 | Moyenne – Apporte une forte valeur mais peut être développée plus tard. |
| 🔵 | Long terme – Vision d'évolution du produit. |

---

# Les quatre piliers

| Pilier | Description |
|----------|-------------|
| 🏗️ Engineering | Architecture, backend, IA, providers, scoring, infrastructure. |
| 📦 Product | Fonctionnalités, expérience utilisateur, interface, ergonomie. |
| 🤝 Business | Partenariats, monétisation, marketplaces, stratégie commerciale. |
| 📚 Knowledge | Données automobiles, études, fiabilité, documentation métier. |

---

# Core Modules

Les modules cœur constituent les fondations de FindMyCar.

Ils sont indispensables au fonctionnement du produit.

| Module | Statut | Priorité | Pilier | Sprint | Description |
|---------|---------|----------|---------|---------|-------------|
| Search Engine | ✅ | 🔴 | 🏗️ Engineering | S1 | Recherche de véhicules selon les critères de l'utilisateur. |
| Compatibility Engine | ✅ | 🔴 | 🏗️ Engineering | S1 | Calcul de la compatibilité entre une annonce et une recherche. |
| Opportunity Engine | ✅ | 🔴 | 🏗️ Engineering | S1 | Détection des bonnes affaires grâce à l'analyse du marché. |
| Scoring Engine | ✅ | 🔴 | 🏗️ Engineering | S1 | Agrégation des différents scores du système. |

---

# Marketplace Modules

Ces modules permettent à FindMyCar de récupérer des annonces provenant de différentes plateformes.

| Module | Statut | Priorité | Pilier | Sprint | Description |
|---------|---------|----------|---------|---------|-------------|
| Marketplace Provider | 🚧 | 🔴 | 🏗️ Engineering | S2 | Interface commune pour toutes les marketplaces. |
| AutoScout24 Provider | 📋 | 🟠 | 🏗️ Engineering | S3 | Intégration d'AutoScout24. |
| La Centrale Provider | 📋 | 🟠 | 🏗️ Engineering | S3 | Intégration de La Centrale. |
| Spoticar Provider | 💡 | 🟡 | 🏗️ Engineering | V2 | Intégration de Spoticar. |
| Leboncoin Provider | 💡 | 🔵 | 🤝 Business | V2 | Intégration uniquement dans le cadre d'un partenariat officiel. |

---

# Data Provider Modules

Ces modules enrichissent les analyses grâce à des données externes.

| Module | Statut | Priorité | Pilier | Sprint | Description |
|---------|---------|----------|---------|---------|-------------|
| VIN Provider | 📋 | 🟠 | 📚 Knowledge | S3 | Informations techniques du véhicule. |
| Reliability Provider | 📋 | 🟠 | 📚 Knowledge | S3 | Fiabilité des moteurs et modèles. |
| Vehicle History Provider | 💡 | 🟡 | 📚 Knowledge | V2 | Historique du véhicule. |
| Recall Provider | 💡 | 🟡 | 📚 Knowledge | V2 | Campagnes de rappel constructeur. |
| Price Estimation Provider | 💡 | 🟠 | 📚 Knowledge | V2 | Estimation de la valeur du véhicule. |

---

# Artificial Intelligence Modules

Ces modules utilisent l'intelligence artificielle pour enrichir les analyses.

| Module | Statut | Priorité | Pilier | Sprint | Description |
|---------|---------|----------|---------|---------|-------------|
| Description Analyzer | 📋 | 🟠 | 🏗️ Engineering | S3 | Analyse intelligente des descriptions. |
| Recommendation Engine | 💡 | 🟡 | 📦 Product | V2 | Recommandations personnalisées. |
| Risk Analyzer | 💡 | 🟠 | 📚 Knowledge | V2 | Détection des points de vigilance. |
| Image Analyzer | 💡 | 🟡 | 🏗️ Engineering | V2 | Analyse automatique des photographies. |

---

# User Experience Modules

Ces modules améliorent l'expérience utilisateur.

| Module | Statut | Priorité | Pilier | Sprint | Description |
|---------|---------|----------|---------|---------|-------------|
| Saved Searches | 💡 | 🟠 | 📦 Product | V2 | Sauvegarde des recherches. |
| Favorites | 💡 | 🟠 | 📦 Product | V2 | Gestion des favoris. |
| Alerts | 💡 | 🟠 | 📦 Product | V2 | Notifications de nouvelles annonces. |
| Comparison Tool | 💡 | 🟡 | 📦 Product | V2 | Comparaison de plusieurs véhicules. |
| Purchase Report | 💡 | 🟠 | 📦 Product | V2 | Rapport complet avant achat. |

---

# Import Modules

Ces modules permettent d'analyser des véhicules provenant de différentes sources.

| Module | Statut | Priorité | Pilier | Sprint | Description |
|---------|---------|----------|---------|---------|-------------|
| URL Import | 💡 | 🟠 | 📦 Product | V2 | Analyse via une URL. |
| Manual Import | 💡 | 🟠 | 📦 Product | V2 | Analyse d'une annonce saisie manuellement. |
| Browser Extension | 💡 | 🟡 | 📦 Product | V2 | Extension Chrome/Firefox/Edge permettant l'analyse directement sur les marketplaces. |

---

# Professional Modules

Modules destinés aux professionnels.

| Module | Statut | Priorité | Pilier | Sprint | Description |
|---------|---------|----------|---------|---------|-------------|
| Dealer Portal | 💡 | 🔵 | 🤝 Business | V3 | Interface dédiée aux concessionnaires. |
| Professional Dashboard | 💡 | 🔵 | 🤝 Business | V3 | Tableau de bord professionnel. |
| Fleet Analysis | 💡 | 🔵 | 🤝 Business | V3 | Analyse de flottes automobiles. |

---

# Platform Modules

Évolutions majeures du produit.

| Module | Statut | Priorité | Pilier | Sprint | Description |
|---------|---------|----------|---------|---------|-------------|
| FindMyCar Marketplace | 💡 | 🔵 | 🤝 Business | V3 | Marketplace propriétaire FindMyCar. |
| Public API | 💡 | 🟡 | 🏗️ Engineering | V2 | API publique destinée aux partenaires. |
| Partner Portal | 💡 | 🔵 | 🤝 Business | V3 | Portail de gestion des partenaires. |

---

# Guiding Principles

Chaque module doit respecter les principes définis dans :

- PRODUCT_VISION.md
- BUSINESS_VISION.md
- TECHNICAL_VISION.md

Tous les modules doivent être :

- indépendants ;
- testables ;
- documentés ;
- évolutifs ;
- cohérents avec la vision globale de FindMyCar.

L'ajout d'un nouveau module ne doit jamais remettre en cause l'architecture existante.

---

# Evolution Strategy

Le développement de FindMyCar est progressif.

Tous les modules n'ont pas vocation à être développés immédiatement.

Les priorités évolueront selon :

- les besoins des utilisateurs ;
- les opportunités business ;
- les partenariats disponibles ;
- les contraintes techniques ;
- les retours des utilisateurs.

Chaque nouveau module devra démontrer qu'il apporte une réelle valeur avant d'être intégré.

---

# Conclusion

FindMyCar est conçu comme une plateforme évolutive.

Chaque module contribue à une mission commune :

> Aider les utilisateurs à prendre de meilleures décisions avant l'achat d'un véhicule.

Cette architecture modulaire permet au produit d'évoluer durablement tout en conservant une base technique robuste, une vision produit cohérente et une stratégie business claire.

MODULES.md constitue le tableau de bord fonctionnel de FindMyCar et sera mis à jour à chaque évolution majeure du projet.