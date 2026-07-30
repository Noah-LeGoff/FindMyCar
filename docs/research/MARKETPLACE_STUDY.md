# Marketplace Study

## Objectif

L'objectif de ce document est d'identifier les marketplaces automobiles pouvant être intégrées à FindMyCar dans un contexte commercial.

Pour chaque plateforme, nous évaluerons :

- la disponibilité d'une API officielle ;
- les conditions d'utilisation ;
- les possibilités de partenariat ;
- la qualité des données disponibles ;
- la facilité d'intégration technique ;
- les contraintes juridiques ;
- la priorité pour FindMyCar.

Ce document est vivant et sera mis à jour tout au long du développement du projet.

---

# Marketplace Inventory

| Marketplace | Pays | Type | API officielle | Partenariat | Priorité | Statut |
|--------------|------|------|----------------|-------------|----------|--------|
| Leboncoin | 🇫🇷 France | Généraliste | 🔍 À étudier | 🔍 À étudier | ⭐⭐⭐⭐☆ | En cours |
| AutoScout24 | 🇪🇺 Europe | Automobile | 🔍 À étudier | 🔍 À étudier | ⭐⭐⭐⭐⭐ | En cours |
| La Centrale | 🇫🇷 France | Automobile | 🔍 À étudier | 🔍 À étudier | ⭐⭐⭐⭐⭐ | En cours |
| ParuVendu Auto | 🇫🇷 France | Automobile | 🔍 À étudier | 🔍 À étudier | ⭐⭐⭐☆☆ | À étudier |
| AutoVisual | 🇫🇷 France | Agrégateur | 🔍 À étudier | 🔍 À étudier | ⭐⭐⭐☆☆ | À étudier |
| Ouest France Auto | 🇫🇷 France | Automobile | 🔍 À étudier | 🔍 À étudier | ⭐⭐⭐☆☆ | À étudier |
| L'Argus | 🇫🇷 France | Automobile | 🔍 À étudier | 🔍 À étudier | ⭐⭐⭐⭐☆ | À étudier |
| Spoticar | 🇪🇺 Europe | Réseau constructeur | 🔍 À étudier | 🔍 À étudier | ⭐⭐⭐⭐☆ | À étudier |
| Aramisauto | 🇫🇷 France | Distributeur | 🔍 À étudier | 🔍 À étudier | ⭐⭐⭐☆☆ | À étudier |
| Autosphere | 🇫🇷 France | Réseau de concessions | 🔍 À étudier | 🔍 À étudier | ⭐⭐⭐⭐☆ | À étudier |

---

# Critères d'évaluation

Chaque marketplace sera évaluée selon les critères suivants.

| Critère | Note |
|----------|------|
| API officielle | /5 |
| Facilité d'intégration | /5 |
| Qualité des données | /5 |
| Richesse des annonces | /5 |
| Volume d'annonces | /5 |
| Conditions d'utilisation | /5 |
| Potentiel commercial | /5 |

Score total :

/35

---

# Légende

Statut :

- À étudier
- En cours
- Validé
- Refusé

Priorité :

⭐☆☆☆☆ Faible

⭐⭐☆☆☆ Moyenne

⭐⭐⭐☆☆ Intéressante

⭐⭐⭐⭐☆ Très intéressante

⭐⭐⭐⭐⭐ Prioritaire

---

# Marketplace Analysis Template

## Nom de la marketplace

### Présentation

Description rapide de la plateforme.

---

### API

API officielle :
- Oui / Non

Documentation :
- Oui / Non

Lien :
- ...

Authentification :
- API Key
- OAuth
- JWT
- Session
- Aucune

---

### Fonctionnalités disponibles

| Fonction | Disponible |
|----------|------------|
| Recherche d'annonces | ✅ / ❌ |
| Consultation d'une annonce | ✅ / ❌ |
| Publication d'une annonce | ✅ / ❌ |
| Mise à jour d'une annonce | ✅ / ❌ |
| Suppression d'une annonce | ✅ / ❌ |

---

### Données disponibles

| Donnée | Disponible |
|---------|------------|
| Prix | |
| Marque | |
| Modèle | |
| Version | |
| Kilométrage | |
| Année | |
| Carburant | |
| Boîte | |
| Puissance | |
| Description | |
| Photos | |
| Localisation | |
| VIN | |
| Vendeur | |

---

### Limites techniques

- Pagination
- Limite de requêtes
- Rate limiting
- Quotas
- Temps de réponse

---

### Difficulté d'intégration

⭐⭐⭐⭐☆

---

### Conclusion

...

---

# AutoScout24

## Présentation

AutoScout24 est l'une des plus importantes marketplaces automobiles européennes. La plateforme est présente dans plusieurs pays et s'adresse aussi bien aux particuliers qu'aux professionnels.

Pour FindMyCar, AutoScout24 représente une source de données particulièrement intéressante grâce à son volume d'annonces et à son écosystème développeur.

---

## Documentation officielle

Documentation développeur : Oui

Documentation API : Oui

Documentation publique :

- https://listing-creation.api.autoscout24.com/docs
- https://developers.autoscout24.ch/api-docs/api-reference.html

Documentation claire et maintenue.

---

## APIs disponibles

### Listing Creation API

API REST officielle permettant de gérer les annonces d'un professionnel.

Fonctionnalités :

- création d'annonces
- modification
- suppression
- upload des photos
- récupération des statistiques
- récupération des marques et modèles
- évaluation du prix

Cette API est principalement destinée aux professionnels qui souhaitent publier leur propre stock de véhicules sur AutoScout24. :contentReference[oaicite:0]{index=0}

---

### Partner API

AutoScout24 propose également une API partenaire nécessitant :

- Client ID
- Client Secret
- OAuth 2.0
- Autorisation préalable

L'accès est réservé aux partenaires autorisés. :contentReference[oaicite:1]{index=1}

---

## Authentification

Méthodes rencontrées :

- Basic Auth (Listing Creation API)
- OAuth 2.0 / OpenID Connect (Partner API)

L'authentification suit les standards modernes de l'industrie. :contentReference[oaicite:2]{index=2}

---

## Fonctionnalités disponibles

| Fonction | Disponible |
|----------|------------|
| Recherche publique de toutes les annonces | ❓ Non documentée publiquement |
| Consultation d'une annonce spécifique | ✅ |
| Création d'annonces | ✅ |
| Modification d'annonces | ✅ |
| Suppression d'annonces | ✅ |
| Upload d'images | ✅ |
| Statistiques | ✅ |
| Marques / Modèles | ✅ |
| Évaluation du prix | ✅ |

---

## Données disponibles

Les APIs officielles permettent notamment de manipuler :

- marque
- modèle
- version
- prix
- kilométrage
- carburant
- boîte de vitesses
- photos
- équipements
- consommation
- émissions
- références constructeur

Le modèle de données est riche et bien structuré. :contentReference[oaicite:3]{index=3}

---

## Recherche d'annonces

À ce jour, aucune documentation publique consultée ne décrit une API permettant à un développeur externe de rechercher librement l'ensemble des annonces AutoScout24.

Les APIs publiques sont orientées vers la gestion du stock d'un vendeur ou d'un partenaire autorisé. :contentReference[oaicite:4]{index=4}

Cette question devra être clarifiée directement auprès d'AutoScout24 si FindMyCar souhaite devenir partenaire.

---

## Conditions d'utilisation

Les conditions d'utilisation protègent explicitement la base de données AutoScout24.

Les requêtes automatisées contournant les interfaces prévues et l'exploitation commerciale des données sans autorisation ne sont pas autorisées. :contentReference[oaicite:5]{index=5}

En conséquence :

- utiliser l'API officielle est conforme au cadre prévu ;
- contourner les protections ou constituer sa propre base de données à partir du site ne constitue pas une stratégie adaptée pour FindMyCar. :contentReference[oaicite:6]{index=6}

---

## Faisabilité technique

★★★★★ (9/10)

Points positifs :

- API REST moderne
- documentation de qualité
- OAuth 2.0
- JSON
- OpenAPI
- modèles de données propres
- documentation régulièrement maintenue

Points négatifs :

- accès partenaire nécessaire
- recherche globale des annonces non documentée publiquement

---

## Faisabilité business

★★★★★★★★☆☆ (8/10)

Points positifs :

- acteur majeur européen
- culture API existante
- documentation professionnelle
- partenaire crédible à long terme

Points négatifs :

- accès probablement réservé aux partenaires
- nécessité de contractualiser

---

## Avantages pour FindMyCar

- plateforme reconnue
- API officielle
- architecture moderne
- données de qualité
- partenaire crédible
- bonne stabilité technique

---

## Inconvénients

- accès non libre
- partenariat probablement obligatoire
- aucune API publique documentée pour parcourir l'ensemble des annonces

---

## Recommandation

AutoScout24 constitue aujourd'hui l'une des plateformes les plus prometteuses pour une future intégration officielle.

En revanche, le développement d'un MarketplaceProvider ne devra commencer qu'après confirmation qu'un partenaire comme FindMyCar peut accéder à une API permettant la recherche d'annonces, et pas uniquement la gestion de son propre stock.

À court terme, il est recommandé de prendre contact avec AutoScout24 afin de clarifier les possibilités offertes aux partenaires technologiques.

---

## Décision

🟡 Compatible sous conditions

Conditions :

- obtenir un partenariat ou un accès développeur adapté ;
- confirmer l'existence d'un endpoint permettant la recherche d'annonces ;
- vérifier les conditions commerciales de l'API.

---

## Synthèse

Technique : 9/10

Business : 8/10

Score global : 17/20

Verdict :

AutoScout24 est aujourd'hui la marketplace la plus prometteuse étudiée pour FindMyCar. Elle dispose d'une infrastructure technique mature et d'APIs officielles, mais l'accès aux fonctionnalités nécessaires au moteur de recherche devra être validé dans le cadre d'un partenariat officiel avant toute implémentation.

---

# La Centrale

## Présentation

La Centrale est l'une des principales marketplaces automobiles françaises. Créée en 1970, elle est spécialisée dans les véhicules d'occasion et bénéficie d'une forte notoriété auprès des particuliers comme des professionnels.

Pour FindMyCar, La Centrale représente une source potentielle de données de grande qualité grâce à son volume d'annonces et à sa spécialisation dans l'automobile.

---

## Documentation officielle

Documentation développeur : ❌ Aucune documentation publique de recherche d'annonces identifiée.

Documentation API : ❌ Aucune API publique documentée pour les développeurs.

Documentation professionnelle : ✅ Des solutions existent pour les professionnels (diffusion d'annonces, services dédiés), mais elles ne constituent pas une API publique de consultation.

---

## APIs disponibles

À la date de cette étude, aucune API publique officielle permettant à un développeur tiers de rechercher les annonces de La Centrale n'a été identifiée.

Les services proposés sont principalement destinés aux professionnels souhaitant publier leurs annonces sur la plateforme.

---

## Authentification

Aucun mécanisme d'authentification développeur public n'a été identifié (API Key, OAuth, etc.).

L'accès aux services techniques semble réservé aux partenaires commerciaux.

---

## Fonctionnalités disponibles

| Fonction | Disponible |
|----------|------------|
| Recherche publique de toutes les annonces | ❌ Non documentée |
| Consultation d'une annonce via API | ❌ Non documentée |
| Création d'annonces | ✅ Pour les professionnels via leurs services |
| Modification d'annonces | ✅ Pour les professionnels |
| Suppression d'annonces | ✅ Pour les professionnels |
| Upload d'images | ✅ Dans le cadre des services professionnels |

---

## Données disponibles

Les annonces visibles sur le site contiennent généralement :

- marque
- modèle
- version
- année
- kilométrage
- prix
- carburant
- boîte de vitesses
- puissance
- description
- équipements
- photos
- localisation
- informations vendeur

Cependant, aucune API publique ne permet aujourd'hui d'accéder officiellement à ces données.

---

## Recherche d'annonces

Aucune documentation officielle ne décrit une API permettant à un développeur externe de rechercher librement les annonces de La Centrale.

Une telle fonctionnalité pourrait éventuellement exister dans le cadre d'un partenariat commercial, mais cela devra être confirmé directement auprès de La Centrale.

---

## Conditions d'utilisation

Les annonces et la base de données de La Centrale sont protégées par leurs conditions d'utilisation et par le droit des bases de données.

L'exploitation automatisée des annonces en dehors des interfaces prévues ne constitue pas une stratégie adaptée à un produit commercial comme FindMyCar.

---

## Faisabilité technique

★★★☆☆ (6/10)

### Points positifs

- plateforme reconnue
- annonces riches
- forte présence sur le marché français

### Points négatifs

- aucune API publique documentée
- documentation développeur inexistante
- intégration officielle peu documentée

---

## Faisabilité business

★★★★★★★☆☆☆ (7/10)

### Points positifs

- acteur majeur en France
- nombreux professionnels partenaires
- crédibilité importante

### Points négatifs

- partenariat probablement indispensable
- conditions techniques peu transparentes

---

## Avantages pour FindMyCar

- forte notoriété
- données automobiles de qualité
- nombreuses annonces professionnelles
- excellente complémentarité avec d'autres marketplaces

---

## Inconvénients

- absence d'API publique
- accès développeur non documenté
- partenariat probablement nécessaire

---

## Recommandation

La Centrale constitue une marketplace stratégique pour FindMyCar en raison de son importance sur le marché français.

Cependant, l'absence d'API publique documentée ne permet pas aujourd'hui d'envisager le développement d'un MarketplaceProvider.

La priorité est de prendre contact avec leurs équipes afin de déterminer si un accès partenaire ou une API privée existe pour des projets comme FindMyCar.

---

## Décision

🟡 Compatible sous conditions

Conditions :

- identifier un programme partenaire ;
- confirmer l'existence d'une API ou d'un accès technique dédié ;
- obtenir un accord commercial si nécessaire.

---

## Synthèse

Technique : 6/10

Business : 7/10

Score global : 13/20

Verdict :

La Centrale est une marketplace incontournable pour le marché français, mais son intégration dépendra vraisemblablement d'un partenariat officiel. En l'état actuel des informations publiques, elle ne peut pas être considérée comme une source de données directement exploitable.

---

# Leboncoin

## Présentation

Leboncoin est la plus importante marketplace généraliste française. Sa catégorie Automobile est l'une des plus consultées du pays et regroupe plusieurs centaines de milliers d'annonces provenant de particuliers et de professionnels.

Pour FindMyCar, Leboncoin représente une source de données majeure. Une intégration officielle constituerait un avantage stratégique important.

---

## Documentation officielle

Documentation développeur : ✅ Oui

Documentation API : ✅ Oui (réservée à certains usages)

Portail développeur :

- https://developer.leboncoin.auto/

La documentation publique est principalement destinée aux professionnels de l'automobile et aux partenaires.

---

## APIs disponibles

### API professionnelle

Leboncoin met à disposition des APIs officielles permettant notamment :

- publication d'annonces ;
- modification ;
- suppression ;
- gestion des stocks de véhicules ;
- synchronisation avec des logiciels métiers.

Ces APIs sont destinées aux professionnels et partenaires autorisés.

---

### API publique de recherche

À la date de cette étude, aucune API publique officielle permettant à un développeur tiers de rechercher librement l'ensemble des annonces Leboncoin n'a été identifiée.

Les appels observés depuis le site web utilisent des APIs internes qui ne sont pas documentées pour un usage externe.

---

## Authentification

Les APIs officielles nécessitent une authentification et un accès partenaire.

Les APIs internes utilisées par le site sont protégées par différents mécanismes de sécurité.

---

## Protection technique

Leboncoin met en œuvre plusieurs protections contre les accès automatisés.

Parmi celles observées :

- protection anti-bot ;
- limitation du nombre de requêtes ;
- contrôle de session ;
- protection DataDome ;
- CAPTCHA lors de comportements considérés comme automatisés.

Lors de nos essais techniques, une requête vers l'endpoint interne de recherche a conduit à un blocage temporaire avec présentation d'un CAPTCHA DataDome.

Cette protection confirme que les APIs internes ne sont pas destinées à un usage externe.

---

## Fonctionnalités disponibles

| Fonction | Disponible |
|----------|------------|
| Recherche publique de toutes les annonces | ❌ Non documentée officiellement |
| Consultation d'une annonce via API publique | ❌ |
| Publication d'annonces | ✅ Pour les partenaires autorisés |
| Modification d'annonces | ✅ |
| Suppression d'annonces | ✅ |
| Synchronisation de stock | ✅ |

---

## Données disponibles

Les annonces affichées sur Leboncoin contiennent notamment :

- prix
- marque
- modèle
- version
- année
- kilométrage
- carburant
- boîte de vitesses
- puissance
- description
- photos
- localisation
- vendeur

Cependant, ces données ne sont pas accessibles via une API publique de recherche.

---

## Recherche d'annonces

Aucune documentation officielle ne décrit une API permettant à un développeur externe de rechercher librement les annonces publiées sur Leboncoin.

Les APIs observées lors de l'utilisation du site sont des interfaces internes.

Leur utilisation n'entre pas dans le cadre des APIs publiques proposées aux développeurs.

---

## Conditions d'utilisation

Les conditions d'utilisation de Leboncoin protègent :

- les annonces ;
- la base de données ;
- les contenus publiés ;
- les interfaces techniques.

L'exploitation automatisée des données en dehors des interfaces prévues ou sans autorisation n'est pas adaptée à un projet commercial comme FindMyCar.

Une intégration officielle devra donc passer par les programmes partenaires proposés par Leboncoin.

---

## Faisabilité technique

★★★★★★★★☆☆ (8/10)

### Points positifs

- infrastructure moderne ;
- APIs officielles existantes ;
- documentation dédiée aux professionnels ;
- données riches et structurées.

### Points négatifs

- API de recherche publique absente ;
- protections anti-bot importantes ;
- accès partenaire nécessaire.

---

## Faisabilité business

★★★★★★★★★☆ (9/10)

### Points positifs

- leader du marché français ;
- très forte visibilité ;
- volume d'annonces exceptionnel ;
- acteur incontournable.

### Points négatifs

- partenariat probablement indispensable ;
- négociation commerciale nécessaire.

---

## Avantages pour FindMyCar

- plus grande base d'annonces en France ;
- excellente couverture du marché des particuliers ;
- nombreuses annonces professionnelles ;
- complément idéal avec d'autres marketplaces.

---

## Inconvénients

- aucune API publique de recherche documentée ;
- protections techniques avancées ;
- dépendance à un partenariat officiel.

---

## Recommandation

Leboncoin doit être considéré comme un partenaire stratégique de long terme.

En revanche, le développement d'un MarketplaceProvider reposant sur les APIs internes du site n'est pas recommandé.

L'approche privilégiée consiste à :

- développer FindMyCar avec des sources officiellement accessibles ;
- démontrer la valeur du produit ;
- solliciter ensuite un partenariat officiel avec Leboncoin.

---

## Actions à mener

### Court terme

- Continuer l'étude des autres marketplaces.
- Concevoir l'architecture pour supporter plusieurs providers.

### Moyen terme

- Identifier le programme partenaire le plus adapté.
- Préparer un dossier de présentation de FindMyCar.

### Long terme

- Contacter les équipes de Leboncoin.
- Négocier un partenariat officiel.
- Développer un MarketplaceProvider utilisant uniquement les interfaces autorisées.

---

## Décision

🟡 Compatible sous conditions

Conditions :

- obtention d'un partenariat officiel ;
- accès à une API adaptée à la recherche ou à un flux de données autorisé ;
- validation juridique avant toute intégration.

---

## Synthèse

Technique : 8/10

Business : 9/10

Score global : 17/20

Verdict :

Leboncoin est la marketplace la plus stratégique pour FindMyCar en France. Toutefois, son intégration devra impérativement reposer sur un partenariat officiel et des interfaces autorisées. Les protections techniques et les conditions d'utilisation conduisent à écarter toute dépendance aux APIs internes du site. L'objectif est de faire de Leboncoin un partenaire potentiel à moyen ou long terme, et non une dépendance technique de la V1.

---

# L'Argus

## Présentation

L'Argus est un acteur historique du marché automobile français. Créé en 1927, il est principalement connu pour sa cote Argus, devenue une référence pour l'estimation de la valeur des véhicules d'occasion.

Aujourd'hui, L'Argus propose également une marketplace d'annonces automobiles, ainsi que de nombreux services destinés aux particuliers et aux professionnels.

Pour FindMyCar, L'Argus présente un double intérêt :

- marketplace de véhicules d'occasion ;
- fournisseur potentiel de données d'évaluation.

---

## Documentation officielle

Documentation développeur : ❌ Non identifiée publiquement.

Documentation API : ❌ Aucune API publique documentée.

Documentation professionnelle : ✅ Plusieurs services B2B sont proposés aux professionnels de l'automobile.

---

## APIs disponibles

À la date de cette étude, aucune API publique officielle destinée aux développeurs externes n'a été identifiée.

L'Argus commercialise néanmoins plusieurs services numériques à destination des professionnels, laissant penser que des interfaces techniques privées existent dans un cadre contractuel.

---

## Authentification

Aucune méthode d'authentification développeur publique n'a été identifiée.

Les éventuelles interfaces semblent réservées aux clients professionnels.

---

## Fonctionnalités disponibles

| Fonction | Disponible |
|----------|------------|
| Recherche publique d'annonces via API | ❌ |
| Consultation d'une annonce via API | ❌ |
| Publication d'annonces | ✅ Via les services professionnels |
| Estimation / cote véhicule | ✅ |
| Services professionnels | ✅ |

---

## Données disponibles

Les annonces publiques contiennent généralement :

- marque
- modèle
- version
- prix
- kilométrage
- année
- carburant
- boîte de vitesses
- puissance
- équipements
- photos
- description
- vendeur

En complément, L'Argus dispose d'informations de valorisation particulièrement intéressantes.

---

## Recherche d'annonces

Aucune API publique documentée ne permet aujourd'hui de rechercher les annonces L'Argus.

Une intégration officielle nécessitera probablement un partenariat commercial.

---

## Conditions d'utilisation

Les annonces, la cote et les contenus proposés sont protégés par les conditions d'utilisation et par le droit des bases de données.

Toute utilisation automatisée devra s'appuyer sur des interfaces officiellement autorisées.

---

## Faisabilité technique

★★★★★★☆☆☆☆ (6/10)

### Points positifs

- acteur historique
- données fiables
- services professionnels existants

### Points négatifs

- aucune API publique documentée
- accès développeur limité

---

## Faisabilité business

★★★★★★★★★☆ (9/10)

### Points positifs

- forte crédibilité
- marque reconnue
- nombreuses opportunités de partenariat
- valeur ajoutée importante pour FindMyCar

### Points négatifs

- partenariat probablement indispensable

---

## Avantages pour FindMyCar

- acteur reconnu
- marketplace complémentaire
- expertise automobile
- potentiel d'enrichissement des analyses
- référence du marché français

---

## Inconvénients

- API publique absente
- accès technique non documenté
- intégration dépendante d'un partenariat

---

## Recommandation

L'Argus ne doit pas être considéré uniquement comme une marketplace.

Son principal intérêt réside dans sa capacité à enrichir FindMyCar avec des données de valorisation et d'expertise.

À moyen terme, un partenariat avec L'Argus pourrait permettre d'améliorer significativement le Score d'Opportunité en intégrant une estimation fiable de la valeur réelle d'un véhicule.

---

## Actions à mener

### Court terme

- Étudier les offres professionnelles de L'Argus.
- Identifier les services exploitables.

### Moyen terme

- Contacter les équipes B2B.
- Vérifier l'existence d'APIs partenaires.

### Long terme

- Intégrer les données de valorisation dans FindMyCar.
- Utiliser la cote comme critère du Score d'Opportunité.

---

## Décision

🟡 Compatible sous conditions

Conditions :

- partenariat professionnel ;
- accès aux services techniques ;
- validation des conditions d'utilisation.

---

## Synthèse

Technique : 6/10

Business : 9/10

Score global : 15/20

Verdict :

L'Argus représente un partenaire stratégique davantage pour la qualité de ses données que pour sa marketplace. À long terme, son expertise pourrait devenir un élément majeur du moteur d'analyse de FindMyCar en renforçant la pertinence du Score d'Opportunité.

---

# Spoticar

## Présentation

Spoticar est la marque officielle du groupe Stellantis dédiée aux véhicules d'occasion. Le réseau regroupe plusieurs milliers de concessionnaires en Europe proposant des véhicules contrôlés, révisés et garantis.

Pour FindMyCar, Spoticar représente une source de données qualitative, principalement composée de véhicules issus du réseau professionnel.

---

## Documentation officielle

Documentation développeur : ❌ Non identifiée publiquement.

Documentation API : ❌ Aucune API publique documentée.

Documentation professionnelle : ✅ Des services numériques existent pour les concessionnaires du réseau.

---

## APIs disponibles

À la date de cette étude, aucune API publique officielle destinée à la consultation des annonces n'a été identifiée.

Les outils disponibles semblent réservés aux concessionnaires et partenaires du réseau Spoticar.

---

## Authentification

Aucune authentification développeur publique n'a été identifiée.

Les interfaces techniques semblent être accessibles uniquement aux professionnels du réseau.

---

## Fonctionnalités disponibles

| Fonction | Disponible |
|----------|------------|
| Recherche publique d'annonces via API | ❌ |
| Consultation d'une annonce via API | ❌ |
| Publication d'annonces | ✅ Pour les concessionnaires |
| Gestion du stock | ✅ |
| Synchronisation des annonces | Probablement en interne |

---

## Données disponibles

Les annonces Spoticar comportent généralement :

- marque
- modèle
- finition
- prix
- kilométrage
- année
- carburant
- boîte de vitesses
- puissance
- équipements détaillés
- photos
- garantie
- localisation
- concessionnaire vendeur

Les données sont généralement très homogènes grâce aux standards imposés par le réseau.

---

## Recherche d'annonces

Aucune API publique documentée ne permet aujourd'hui de rechercher les annonces Spoticar.

Toute intégration nécessitera vraisemblablement un partenariat officiel avec Stellantis ou Spoticar.

---

## Conditions d'utilisation

Les contenus et la base de données sont protégés.

Toute récupération automatisée des annonces devra passer par une interface officiellement autorisée.

---

## Faisabilité technique

★★★★★☆☆☆☆☆ (5/10)

### Points positifs

- données très homogènes
- qualité élevée
- annonces professionnelles

### Points négatifs

- aucune API publique
- intégration réservée au réseau

---

## Faisabilité business

★★★★★★★★☆☆ (8/10)

### Points positifs

- acteur majeur européen
- image de confiance
- données qualitatives
- partenaire crédible

### Points négatifs

- accès probablement réservé
- dépendance à un partenariat

---

## Avantages pour FindMyCar

- annonces fiables
- véhicules garantis
- historique souvent mieux renseigné
- données homogènes
- excellente qualité des fiches véhicules

---

## Inconvénients

- volume d'annonces inférieur aux grandes marketplaces
- aucune API publique documentée
- partenariat nécessaire

---

## Recommandation

Spoticar représente une excellente source complémentaire pour FindMyCar.

Même si le volume d'annonces est plus limité que celui des grandes marketplaces, la qualité des données et des véhicules en fait un partenaire particulièrement intéressant.

---

## Actions à mener

### Court terme

- Étudier les solutions numériques proposées aux concessionnaires.

### Moyen terme

- Identifier un contact B2B chez Spoticar.

### Long terme

- Évaluer la possibilité d'un partenariat technique avec Stellantis.

---

## Décision

🟡 Compatible sous conditions

Conditions :

- partenariat officiel ;
- accès à une interface technique autorisée.

---

## Synthèse

Technique : 5/10

Business : 8/10

Score global : 13/20

Verdict :

Spoticar constitue une excellente source de données qualitatives pour compléter FindMyCar. Son intégration devra cependant s'inscrire dans un partenariat officiel avec le réseau Stellantis.

---

# Autosphere

## Présentation

Autosphere est l'un des principaux réseaux français de distribution automobile. La plateforme commercialise principalement des véhicules d'occasion issus de concessions partenaires et du groupe Emil Frey France.

Pour FindMyCar, Autosphere constitue une source de données qualitative grâce à des annonces homogènes, des véhicules contrôlés et un réseau national important.

---

## Documentation officielle

Documentation développeur : ❌ Non identifiée publiquement.

Documentation API : ❌ Aucune API publique documentée.

Documentation professionnelle : ✅ Des outils existent pour les professionnels du groupe.

---

## APIs disponibles

À la date de cette étude, aucune API publique officielle permettant la consultation des annonces n'a été identifiée.

Les interfaces techniques semblent réservées aux systèmes internes et aux partenaires.

---

## Authentification

Aucune authentification développeur publique n'a été identifiée.

Les éventuelles APIs semblent destinées exclusivement aux partenaires autorisés.

---

## Fonctionnalités disponibles

| Fonction | Disponible |
|----------|------------|
| Recherche publique d'annonces via API | ❌ |
| Consultation d'une annonce via API | ❌ |
| Publication d'annonces | ✅ Via les outils professionnels |
| Gestion de stock | ✅ |
| Synchronisation interne | Probable |

---

## Données disponibles

Les annonces comprennent généralement :

- marque
- modèle
- finition
- prix
- kilométrage
- année
- carburant
- boîte de vitesses
- puissance
- équipements détaillés
- photos
- garantie
- localisation
- concessionnaire vendeur

Les données sont homogènes et suivent des standards professionnels.

---

## Recherche d'annonces

Aucune API publique documentée ne permet aujourd'hui de rechercher les annonces Autosphere.

Une intégration nécessitera vraisemblablement un partenariat avec Autosphere ou Emil Frey France.

---

## Conditions d'utilisation

Les annonces et la base de données sont protégées.

Toute utilisation automatisée devra s'appuyer sur une interface officiellement autorisée.

---

## Faisabilité technique

★★★★★☆☆☆☆☆ (5/10)

### Points positifs

- données homogènes
- qualité des annonces
- réseau professionnel

### Points négatifs

- aucune API publique
- intégration réservée aux partenaires

---

## Faisabilité business

★★★★★★★★☆☆ (8/10)

### Points positifs

- acteur majeur français
- crédibilité importante
- réseau de concessions
- véhicules contrôlés

### Points négatifs

- partenariat nécessaire
- accès technique peu documenté

---

## Avantages pour FindMyCar

- données fiables
- véhicules professionnels
- annonces homogènes
- bonne qualité des fiches

---

## Inconvénients

- aucune API publique documentée
- partenariat indispensable
- volume inférieur aux grandes marketplaces généralistes

---

## Recommandation

Autosphere constitue un excellent partenaire potentiel pour compléter les marketplaces généralistes.

Son intérêt réside davantage dans la qualité de ses annonces que dans leur volume.

---

## Actions à mener

### Court terme

- Identifier les solutions numériques proposées aux professionnels.

### Moyen terme

- Identifier un contact B2B chez Autosphere ou Emil Frey France.

### Long terme

- Étudier un partenariat permettant un accès officiel aux données.

---

## Décision

🟡 Compatible sous conditions

Conditions :

- partenariat officiel ;
- accès à une interface technique autorisée.

---

## Synthèse

Technique : 5/10

Business : 8/10

Score global : 13/20

Verdict :

Autosphere représente une source de données qualitative pour FindMyCar. Son intégration est envisageable dans le cadre d'un partenariat avec le groupe, mais aucune API publique ne permet aujourd'hui de développer un MarketplaceProvider autonome.