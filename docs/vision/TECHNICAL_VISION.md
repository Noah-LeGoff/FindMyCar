# Technical Vision — FindMyCar

## Introduction

La technologie est un moyen, jamais une finalité.

FindMyCar n'a pas vocation à utiliser les technologies les plus récentes simplement parce qu'elles sont populaires.

Chaque choix technique doit répondre à une seule question :

> Cette décision améliore-t-elle durablement la qualité, la maintenabilité ou l'évolutivité du produit ?

Ce document définit les principes techniques qui guideront l'ensemble du développement de FindMyCar.

Ces principes sont indépendants des langages, des frameworks ou des outils utilisés.

---

# Notre philosophie technique

Nous considérons que la qualité d'une architecture ne dépend pas du nombre de technologies utilisées.

Elle dépend de sa capacité à évoluer sans remettre en cause les fondations du produit.

Chaque décision technique doit favoriser :

- la simplicité ;
- la lisibilité ;
- la robustesse ;
- la maintenabilité ;
- l'évolutivité.

Nous privilégions toujours les solutions simples, compréhensibles et testables.

---

# Le domaine métier avant tout

Le domaine métier constitue le cœur de FindMyCar.

Toutes les autres couches techniques gravitent autour de lui.

La logique métier ne doit jamais dépendre :

- d'une base de données ;
- d'un framework ;
- d'une API externe ;
- d'un fournisseur de données ;
- d'un modèle d'intelligence artificielle.

Les technologies servent le métier.

Jamais l'inverse.

---

# Une architecture modulaire

FindMyCar est conçu comme une plateforme modulaire.

Chaque composant possède une responsabilité clairement définie.

Chaque module doit pouvoir évoluer indépendamment des autres.

L'objectif est de permettre au projet de grandir sans provoquer de régressions importantes.

Les dépendances entre modules doivent rester limitées et explicites.

---

# Les abstractions avant les implémentations

Les composants communiquent au travers d'interfaces clairement définies.

Les implémentations peuvent évoluer ou être remplacées sans modifier le reste du système.

Cette approche permet notamment de remplacer facilement :

- un MarketplaceProvider ;
- un DataProvider ;
- un fournisseur d'intelligence artificielle ;
- un système de notifications ;
- un moteur de stockage.

Le projet dépend des contrats définis par les interfaces et non des implémentations concrètes.

---

# Les tests comme fondation

Les tests font partie intégrante du développement.

Ils ne constituent pas une étape finale.

Chaque nouvelle fonctionnalité doit pouvoir être validée automatiquement.

Les tests permettent de :

- garantir le bon fonctionnement du produit ;
- faciliter les évolutions ;
- prévenir les régressions ;
- documenter implicitement le comportement attendu.

Une fonctionnalité difficile à tester est souvent le signe d'une conception perfectible.

---

# Construire pour durer

Chaque décision technique doit être évaluée selon trois critères fondamentaux :

- Est-elle maintenable ?
- Est-elle testable ?
- Est-elle évolutive ?

Si la réponse est négative à l'un de ces critères, la décision doit être reconsidérée.

Nous privilégions les solutions pérennes plutôt que les optimisations à court terme.

---

# La simplicité comme principe

La simplicité est une force.

Nous évitons les abstractions inutiles et les architectures excessivement complexes.

La meilleure solution est celle qui répond correctement au besoin avec le minimum de complexité nécessaire.

Chaque ligne de code doit avoir une raison d'exister.

---

# Les performances

Les performances sont importantes.

Cependant, elles ne doivent jamais compromettre la qualité du produit.

Nous privilégions d'abord :

- la justesse ;
- la lisibilité ;
- la fiabilité.

Les optimisations seront réalisées lorsqu'elles seront justifiées par des mesures concrètes.

Nous refusons les optimisations prématurées.

---

# Les données

Les données constituent le cœur des analyses réalisées par FindMyCar.

Nous cherchons à produire des modèles :

- cohérents ;
- prévisibles ;
- fiables.

Nous privilégions autant que possible des objets immuables afin de limiter les effets de bord et de rendre le comportement du système plus facilement compréhensible.

---

# L'intelligence artificielle

L'intelligence artificielle est un outil.

Elle ne constitue pas le cœur du produit.

Les analyses produites par l'IA doivent pouvoir être remplacées, améliorées ou complétées sans modifier l'architecture générale.

FindMyCar ne doit jamais dépendre d'un fournisseur unique d'intelligence artificielle.

Les composants IA doivent rester interchangeables.

---

# Les dépendances externes

Chaque dépendance externe représente un risque potentiel.

Nous cherchons à limiter les dépendances inutiles.

Lorsque nous adoptons une bibliothèque, un service ou une API, nous évaluons notamment :

- sa pérennité ;
- sa documentation ;
- sa communauté ;
- sa licence ;
- sa stabilité.

Les dépendances doivent rester un choix réfléchi.

---

# L'observabilité

Un système complexe doit être observable.

Nous souhaitons que FindMyCar permette de comprendre facilement :

- pourquoi une erreur s'est produite ;
- pourquoi une analyse a été générée ;
- pourquoi un score a évolué ;
- pourquoi un fournisseur de données a échoué.

Les journaux, les métriques et la traçabilité font partie intégrante de la qualité technique.

---

# L'évolution continue

L'architecture doit faciliter l'évolution du produit.

L'ajout :

- d'une nouvelle marketplace ;
- d'un nouveau fournisseur de données ;
- d'un nouveau modèle d'intelligence artificielle ;
- d'un nouveau moteur de scoring ;

ne doit jamais nécessiter une refonte complète du système.

Chaque évolution doit s'intégrer naturellement à l'architecture existante.

---

# Les technologies

Les technologies utilisées aujourd'hui ne définissent pas FindMyCar.

Elles constituent uniquement les outils permettant de concrétiser notre vision.

Le projet doit pouvoir évoluer vers de nouveaux langages, frameworks ou infrastructures sans remettre en cause ses principes fondamentaux.

Notre vision technique est indépendante des choix technologiques.

---

# Notre définition de la qualité

Nous considérons qu'une architecture est de qualité lorsqu'elle est :

- simple à comprendre ;
- simple à tester ;
- simple à maintenir ;
- simple à faire évoluer.

Une architecture n'a pas besoin d'être complexe pour être robuste.

Au contraire, la simplicité est souvent le meilleur indicateur d'une bonne conception.

---

# Conclusion

La technologie n'est pas l'objectif de FindMyCar.

Elle est le moyen de construire un produit fiable, durable et évolutif.

Chaque décision technique devra toujours être guidée par les principes définis dans ce document.

Notre ambition est de construire une architecture capable d'accompagner le développement de FindMyCar pendant de nombreuses années sans compromettre sa qualité.

Une bonne architecture ne se mesure pas au nombre de technologies utilisées.

Elle se mesure à sa capacité à évoluer sans remettre en cause les fondations du produit.