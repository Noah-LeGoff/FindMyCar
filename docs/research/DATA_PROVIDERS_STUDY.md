# Data Providers Study

## Introduction

L'objectif de ce document est d'identifier, d'analyser et de comparer les différentes sources de données pouvant enrichir les analyses réalisées par FindMyCar.

Contrairement aux marketplaces, qui fournissent principalement des annonces, les data providers apportent des informations complémentaires permettant d'améliorer la compréhension d'un véhicule, d'évaluer son état, sa valeur ou encore les risques associés à son achat.

Chaque fournisseur sera étudié selon les critères suivants :

- présentation du fournisseur ;
- type de données disponibles ;
- qualité des données ;
- mode d'accès (API, open data, partenariat...) ;
- contraintes juridiques ;
- coût ;
- difficulté d'intégration ;
- avantages ;
- limites ;
- pertinence pour FindMyCar ;
- verdict.

---

# Philosophie

FindMyCar ne cherche pas à accumuler le plus grand nombre de données possible.

Notre objectif est d'utiliser uniquement des données fiables, pertinentes et compréhensibles afin d'aider les utilisateurs à prendre une meilleure décision.

Chaque nouvelle source de données devra apporter une réelle valeur ajoutée.

---

# Les besoins de FindMyCar

Avant d'étudier les fournisseurs, il est nécessaire de définir précisément les données recherchées.

## 1. Informations techniques 🔴

Objectif :

Comprendre précisément les caractéristiques d'un véhicule.

Exemples :

- VIN
- constructeur
- modèle
- génération
- finition
- motorisation
- puissance
- couple
- cylindrée
- carburant
- boîte de vitesses
- transmission
- consommation
- émissions CO₂
- Crit'Air
- dimensions
- poids
- capacité du coffre
- équipements

---

## 2. Historique du véhicule 🔴

Objectif :

Évaluer le passé administratif et technique d'un véhicule.

Exemples :

- nombre de propriétaires
- historique du kilométrage
- contrôles techniques
- sinistres
- véhicule gagé
- opposition administrative
- historique d'entretien
- importation
- utilisation professionnelle

---

## 3. Fiabilité 🔴

Objectif :

Identifier les problèmes connus d'un modèle avant l'achat.

Exemples :

- fiabilité moteur
- fiabilité boîte de vitesses
- défauts connus
- problèmes récurrents
- campagnes de rappel
- fréquence des pannes
- coût moyen des réparations
- disponibilité des pièces

---

## 4. Analyse financière 🟠

Objectif :

Évaluer si le prix demandé est cohérent.

Exemples :

- cote
- estimation de marché
- décote
- coût annuel estimé
- coût carburant
- coût assurance
- coût d'entretien

---

## 5. Sécurité 🟠

Objectif :

Mieux évaluer le niveau de sécurité d'un véhicule.

Exemples :

- note Euro NCAP
- équipements de sécurité
- aides à la conduite
- rappels liés à la sécurité

---

## 6. Analyse par intelligence artificielle 🟠

Objectif :

Compléter les analyses classiques grâce à l'IA.

Exemples :

- analyse de la description
- détection d'incohérences
- qualité de l'annonce
- analyse des photographies
- estimation de l'état général
- détection d'éléments suspects

---

## 7. Données communautaires 🟡

Objectif :

Capitaliser sur l'expérience des propriétaires.

Exemples :

- avis
- consommation réelle
- coût réel d'entretien
- fréquence des réparations
- satisfaction globale

Ces données ne constituent pas une priorité pour le MVP mais représentent une évolution intéressante à long terme.

---

# Priorités

| Domaine | Priorité |
|----------|-----------|
| Informations techniques | 🔴 Critique |
| Historique du véhicule | 🔴 Critique |
| Fiabilité | 🔴 Critique |
| Analyse financière | 🟠 Haute |
| Sécurité | 🟠 Haute |
| Intelligence artificielle | 🟠 Haute |
| Données communautaires | 🟡 Long terme |

---

# Fournisseurs étudiés

Les fournisseurs seront ajoutés progressivement au cours de cette étude.

## Sources publiques

- Histovec
- Euro NCAP
- Base Crit'Air
- Open Data gouvernemental

## Fournisseurs privés

- Services VIN
- Bases de données de fiabilité
- Fournisseurs de cotes automobiles
- Fournisseurs d'historique de véhicules

## Partenaires potentiels

À compléter au fur et à mesure des recherches.

---

# Conclusion

Cette étude servira de référence lors du développement des futurs Data Providers de FindMyCar.

Chaque intégration devra respecter les principes définis dans :

- PRODUCT_VISION.md
- BUSINESS_VISION.md
- TECHNICAL_VISION.md

L'objectif n'est pas de connecter le plus grand nombre de fournisseurs possible, mais de sélectionner ceux qui apportent la meilleure valeur aux utilisateurs dans un cadre légal, durable et maintenable.

---

# Histovec

## Présentation

Histovec est un service officiel développé par le ministère de l'Intérieur français.

Son objectif est de permettre aux propriétaires de partager avec un acheteur potentiel certaines informations administratives concernant leur véhicule.

Le service vise à renforcer la transparence lors des ventes de véhicules d'occasion.

---

# Type de fournisseur

Service public

---

# Pays

France

---

# Site officiel

https://histovec.interieur.gouv.fr

---

# Type de données fournies

Histovec permet notamment d'obtenir :

- date de première mise en circulation ;
- caractéristiques administratives du véhicule ;
- changements de propriétaire ;
- situation administrative (gage ou opposition) ;
- déclarations de sinistre ayant conduit à une procédure de véhicule endommagé lorsqu'elles sont enregistrées ;
- informations issues de l'administration française selon les données disponibles au propriétaire.

Ces informations sont fournies sous la responsabilité des services publics concernés.

---

# Cas d'utilisation dans FindMyCar

Les données Histovec pourraient enrichir une analyse en affichant par exemple :

- ✔ Véhicule non gagé
- ✔ Aucune opposition administrative connue
- ✔ Première mise en circulation cohérente
- ✔ Historique administratif vérifié

Ces informations augmenteraient la confiance de l'utilisateur avant de contacter le vendeur.

---

# Qualité des données

⭐⭐⭐⭐⭐

Les données proviennent de sources administratives officielles.

Elles constituent l'une des références les plus fiables concernant la situation administrative d'un véhicule immatriculé en France.

---

# Mode d'accès

À étudier.

À ce jour, Histovec est principalement conçu comme un service consulté par le propriétaire du véhicule, qui choisit ensuite de partager un rapport avec un acheteur.

Aucune API publique destinée à des intégrations commerciales n'a été retenue à ce stade de notre étude.

---

# Contraintes juridiques

Point particulièrement important.

Les données Histovec concernent un véhicule identifié et impliquent des informations administratives.

Toute intégration devra respecter :

- les conditions d'utilisation du service ;
- la réglementation applicable, notamment en matière de protection des données ;
- un éventuel partenariat ou mode d'accès officiellement prévu.

FindMyCar n'a pas vocation à contourner ces mécanismes.

---

# Coût

Inconnu.

Le service est gratuit pour les particuliers.

Les modalités d'un éventuel accès professionnel restent à étudier.

---

# Difficulté d'intégration

⭐⭐⭐☆☆

Technique :

Faible à moyenne.

Juridique :

Potentiellement élevée.

La principale difficulté n'est probablement pas technique mais liée au mode d'accès autorisé.

---

# Avantages

- Source officielle.
- Très forte crédibilité.
- Informations administratives utiles.
- Renforce la confiance des utilisateurs.
- Cohérent avec la philosophie de transparence de FindMyCar.

---

# Limites

- Limité aux véhicules immatriculés en France.
- Ne couvre pas l'état mécanique réel du véhicule.
- Ne remplace pas une expertise automobile.
- Les informations disponibles dépendent du fonctionnement et des modalités du service.

---

# Pertinence pour FindMyCar

⭐⭐⭐⭐⭐

Histovec constitue l'une des sources de données les plus pertinentes pour le marché français.

Même si son intégration nécessite une étude juridique et technique approfondie, il représente un fournisseur stratégique.

---

# Verdict

🔴 Priorité : Critique

Histovec est un candidat prioritaire pour enrichir les analyses de FindMyCar destinées au marché français.

Toutefois, son intégration devra impérativement reposer sur une solution conforme aux conditions d'utilisation du service et à la réglementation applicable.

---

# Décision

Décision actuelle :

🟡 À approfondir.

Actions futures :

- Étudier précisément les modalités d'accès proposées par Histovec.
- Vérifier l'existence de solutions officielles destinées aux professionnels.
- Évaluer la faisabilité d'une intégration dans le respect du cadre juridique.

---

# Euro NCAP

## Présentation

Euro NCAP (European New Car Assessment Programme) est un organisme indépendant créé en 1997 afin d'évaluer la sécurité des véhicules commercialisés en Europe.

Ses essais sont devenus la référence européenne en matière de sécurité automobile.

Les constructeurs utilisent souvent leurs résultats pour démonorer la qualité de leurs véhicules.

---

# Type de fournisseur

Organisme indépendant

---

# Pays

Europe

---

# Site officiel

https://www.euroncap.com

---

# Type de données fournies

Euro NCAP publie notamment :

- note globale du véhicule (0 à 5 étoiles) ;
- protection des adultes ;
- protection des enfants ;
- protection des usagers vulnérables (piétons, cyclistes...) ;
- efficacité des aides à la conduite ;
- résultats détaillés des crash-tests ;
- vidéos des essais ;
- rapports techniques.

---

# Cas d'utilisation dans FindMyCar

FindMyCar pourrait afficher :

- la note Euro NCAP du véhicule ;
- un résumé des résultats ;
- les principaux points forts ;
- les éventuels points faibles.

Exemple :

✔ Sécurité : ★★★★★

Excellente protection des occupants.

Très bonnes aides à la conduite.

Crash-tests parmi les meilleurs de sa catégorie.

Ces informations permettraient aux utilisateurs d'intégrer la sécurité dans leur décision d'achat.

---

# Qualité des données

⭐⭐⭐⭐⭐

Euro NCAP constitue la référence européenne en matière d'évaluation de la sécurité automobile.

Les essais sont réalisés selon des protocoles publics, régulièrement mis à jour afin de suivre les évolutions technologiques.

---

# Mode d'accès

À étudier.

Les résultats sont publiquement consultables sur le site officiel.

En revanche, les modalités de réutilisation des données dans un produit commercial devront être vérifiées.

Une API publique n'a pas été retenue à ce stade de notre étude.

---

# Contraintes juridiques

Les notes, rapports et contenus publiés par Euro NCAP sont protégés.

Toute intégration devra respecter :

- les conditions d'utilisation ;
- les droits de propriété intellectuelle ;
- les éventuelles licences de réutilisation.

FindMyCar privilégiera toujours une solution officielle ou conforme aux autorisations accordées.

---

# Coût

Inconnu.

À déterminer selon les possibilités de partenariat ou de licence.

---

# Difficulté d'intégration

⭐⭐☆☆☆

Technique :

Faible.

Juridique :

Moyenne.

Le principal enjeu sera de déterminer dans quelles conditions les données peuvent être réutilisées.

---

# Avantages

- Référence européenne reconnue.
- Source indépendante.
- Données objectives.
- Améliore la qualité des analyses.
- Renforce la confiance des utilisateurs.
- Facilement compréhensible grâce au système de notation.

---

# Limites

- Tous les véhicules n'ont pas été testés.
- Les protocoles évoluent au fil des années, ce qui rend certaines comparaisons délicates.
- Les résultats concernent principalement la sécurité passive et active lors des essais, sans refléter l'état réel d'un véhicule d'occasion.

---

# Pertinence pour FindMyCar

⭐⭐⭐⭐☆

Euro NCAP constitue une excellente source pour enrichir les analyses de sécurité des véhicules.

Cette donnée apporte une forte valeur ajoutée aux utilisateurs tout en restant simple à comprendre.

---

# Verdict

🟠 Priorité : Haute

Euro NCAP représente un fournisseur particulièrement pertinent pour compléter les analyses de FindMyCar.

Son intégration devra toutefois respecter les conditions de réutilisation des données publiées.

---

# Décision

Décision actuelle :

🟡 À approfondir.

Actions futures :

- Étudier les conditions de réutilisation des données Euro NCAP.
- Vérifier l'existence d'une API ou d'un partenariat officiel.
- Déterminer la meilleure manière de présenter les résultats aux utilisateurs sans induire de comparaisons trompeuses entre des véhicules évalués selon des protocoles différents.

---

# Services VIN

## Présentation

Les services VIN (Vehicle Identification Number) permettent de décoder le numéro d'identification unique d'un véhicule afin d'obtenir des informations techniques extrêmement précises.

Contrairement aux informations présentes dans une annonce, qui peuvent être incomplètes ou erronées, les données issues du VIN correspondent aux caractéristiques d'origine du véhicule telles qu'elles ont été enregistrées lors de sa fabrication.

Le VIN constitue ainsi l'identifiant technique le plus fiable d'un véhicule.

---

# Type de fournisseur

Fournisseurs privés de données automobiles

---

# Couverture

Internationale

La majorité des fournisseurs couvrent plusieurs dizaines de marques automobiles et plusieurs millions de véhicules.

---

# Principaux fournisseurs

- JATO Dynamics
- DataOne Software
- EpicVIN
- Vindecoder
- CARFAX (certaines données selon les pays)
- TecDoc (complémentaire pour certaines informations techniques)

Le fournisseur retenu sera choisi ultérieurement après une étude plus approfondie.

---

# Type de données fournies

Selon les fournisseurs, un décodage VIN peut permettre d'obtenir :

- constructeur
- modèle
- génération
- année de production
- usine de fabrication
- motorisation exacte
- puissance
- cylindrée
- type de carburant
- boîte de vitesses
- transmission
- finition
- couleur d'origine
- équipements d'origine
- options installées
- code moteur
- code boîte
- informations techniques diverses

Certains fournisseurs proposent également :

- historique du véhicule
- rappels constructeur
- données de maintenance
- photos historiques
- estimation de valeur

---

# Cas d'utilisation dans FindMyCar

Le VIN pourrait devenir la base de nombreuses analyses.

Exemples :

- identification exacte du véhicule ;
- vérification de la cohérence entre l'annonce et le véhicule réel ;
- récupération automatique des caractéristiques techniques ;
- détection des options d'origine ;
- alimentation des modules de fiabilité ;
- alimentation des modules de maintenance ;
- alimentation des modules d'analyse IA.

Le VIN pourrait également servir d'identifiant principal pour relier plusieurs sources de données concernant un même véhicule.

---

# Qualité des données

⭐⭐⭐⭐⭐

Les données proviennent généralement de bases de données professionnelles utilisées par l'industrie automobile.

La qualité dépendra du fournisseur retenu.

---

# Mode d'accès

Principalement via :

- API REST
- licences professionnelles
- partenariats commerciaux

Les modalités varient fortement selon les fournisseurs.

---

# Contraintes juridiques

Les données sont généralement protégées par des licences commerciales.

Chaque fournisseur possède ses propres conditions d'utilisation.

FindMyCar privilégiera une intégration officielle dans le respect des licences.

---

# Coût

Variable.

La plupart des fournisseurs proposent :

- abonnement mensuel ;
- paiement à la requête ;
- licences professionnelles ;
- contrats personnalisés.

Le coût devra être évalué lors du choix du fournisseur.

---

# Difficulté d'intégration

⭐⭐⭐☆☆

Technique :

Moyenne.

Les API sont généralement bien documentées.

Business :

Moyenne à élevée selon les conditions commerciales.

---

# Avantages

- Identification précise du véhicule.
- Données techniques fiables.
- Réduction des erreurs présentes dans les annonces.
- Base idéale pour enrichir tous les autres modules.
- Compatible avec une architecture modulaire.

---

# Limites

- Données généralement payantes.
- Le VIN n'est pas toujours communiqué dans les annonces.
- Certaines informations peuvent varier selon les fournisseurs.
- L'accès dépend souvent d'accords commerciaux.

---

# Pertinence pour FindMyCar

⭐⭐⭐⭐⭐

Les services VIN constituent l'un des piliers techniques de FindMyCar.

Ils permettront de transformer une simple annonce en une fiche technique complète et fiable.

---

# Verdict

🔴 Priorité : Critique

L'intégration d'un service VIN représente une priorité stratégique pour FindMyCar.

Le choix du fournisseur devra faire l'objet d'une étude spécifique afin d'identifier la solution offrant le meilleur équilibre entre qualité, couverture, coût et facilité d'intégration.

---

# Décision

Décision actuelle :

🟢 Retenu comme composant stratégique.

Actions futures :

- Comparer les principaux fournisseurs.
- Évaluer les coûts et les modèles de licence.
- Concevoir un module `VINProvider` indépendant de tout fournisseur.
- Rédiger une ADR définissant le VIN comme identifiant métier principal des véhicules dans FindMyCar.

---

# Fournisseurs de fiabilité automobile

## Présentation

Contrairement aux autres catégories de fournisseurs étudiées dans ce document, il n'existe pas de base de données universelle recensant l'ensemble des problèmes de fiabilité des véhicules.

Les informations sont aujourd'hui réparties entre plusieurs acteurs :

- constructeurs automobiles ;
- organismes spécialisés ;
- presse automobile ;
- ateliers de réparation ;
- campagnes de rappel ;
- experts indépendants ;
- communautés de propriétaires.

L'objectif de FindMyCar sera de centraliser ces connaissances afin de proposer une analyse fiable, compréhensible et objective.

---

# Type de fournisseur

Catégorie de fournisseurs spécialisés.

---

# Couverture

Internationale.

La couverture dépendra des partenaires retenus.

---

# Sources potentielles

## Constructeurs

- Campagnes de rappel
- Bulletins techniques

---

## Organismes publics

- Campagnes officielles de rappel
- Organismes nationaux de sécurité

---

## Presse spécialisée

- Essais longue durée
- Études de fiabilité
- Analyses techniques

---

## Professionnels

- Réseaux de garages
- Experts automobiles
- Concessions partenaires

---

## Communautés

- Clubs automobiles
- Forums spécialisés
- Associations de propriétaires

Ces données devront toujours être utilisées avec prudence et recoupées lorsqu'elles influencent une recommandation.

---

# Type de données fournies

Les informations recherchées concernent notamment :

- moteurs réputés fiables ;
- moteurs présentant des défauts connus ;
- boîtes de vitesses fragiles ;
- problèmes électroniques fréquents ;
- campagnes de rappel ;
- coûts moyens des réparations ;
- disponibilité des pièces ;
- durée de vie moyenne des principaux organes ;
- opérations d'entretien importantes.

---

# Cas d'utilisation dans FindMyCar

Ces données permettront notamment :

- d'expliquer les forces et faiblesses d'un véhicule ;
- d'afficher les points de vigilance avant achat ;
- d'améliorer le score de fiabilité ;
- d'aider les utilisateurs à anticiper les coûts futurs ;
- d'alimenter le futur Knowledge Engine.

---

# Qualité des données

Variable.

Les données devront être systématiquement :

- vérifiées ;
- recoupées ;
- sourcées lorsque cela est possible.

FindMyCar ne devra jamais diffuser une information non vérifiée comme un fait établi.

---

# Mode d'accès

Très variable.

Selon les sources :

- open data ;
- API ;
- partenariats ;
- licences ;
- publications publiques.

---

# Contraintes juridiques

Les contenus rédactionnels sont protégés.

FindMyCar privilégiera :

- les partenariats ;
- les données publiques ;
- les analyses produites en interne.

---

# Coût

Très variable.

Certaines données sont publiques.

D'autres nécessiteront des partenariats ou des licences professionnelles.

---

# Difficulté d'intégration

⭐⭐⭐⭐☆

Technique : moyenne.

Métier : élevée.

La difficulté principale réside dans la validation et la structuration des connaissances.

---

# Avantages

- Très forte valeur ajoutée.
- Différenciation importante.
- Aide concrète à la décision.
- Complète parfaitement les autres fournisseurs.

---

# Limites

- Pas de source unique.
- Informations parfois contradictoires.
- Nécessite une validation continue.
- Forte maintenance.

---

# Pertinence pour FindMyCar

⭐⭐⭐⭐⭐

Cette catégorie constitue l'un des piliers stratégiques du projet.

À terme, elle alimentera le Knowledge Engine de FindMyCar.

---

# Verdict

🔴 Priorité : Critique

Le développement d'une base de connaissances fiable représente un investissement important mais constitue également l'un des principaux avantages concurrentiels de FindMyCar.

---

# Décision

Décision actuelle :

🟢 Retenu comme composant stratégique.

Actions futures :

- Identifier les meilleures sources.
- Définir un modèle de validation des informations.
- Concevoir le Knowledge Engine.
- Créer un futur `ReliabilityProvider`.

---

# Fournisseurs de cotes automobiles

## Présentation

Les fournisseurs de cotes automobiles permettent d'estimer la valeur d'un véhicule en fonction de ses caractéristiques, de son âge, de son kilométrage, de sa motorisation, de son état et des tendances du marché.

Leur objectif est de fournir une estimation réaliste de la valeur d'un véhicule afin d'aider les particuliers et les professionnels à fixer ou à évaluer un prix.

Pour FindMyCar, ces données seront essentielles afin de déterminer si une annonce est correctement positionnée par rapport au marché.

---

# Type de fournisseur

Fournisseurs privés spécialisés dans l'évaluation automobile.

---

# Couverture

Principalement nationale ou européenne selon les fournisseurs.

---

# Principaux fournisseurs

- L'Argus
- La Centrale
- AutoScout24 Market Insights
- Kelley Blue Book (États-Unis)
- DAT (Allemagne)
- autres services spécialisés

Le choix du fournisseur dépendra des pays couverts, des conditions d'accès et des possibilités de partenariat.

---

# Type de données fournies

Selon les fournisseurs, les données peuvent inclure :

- cote du véhicule ;
- estimation de la valeur de marché ;
- décote annuelle ;
- évolution des prix ;
- valeur de reprise ;
- valeur de vente entre particuliers ;
- estimation selon le kilométrage ;
- estimation selon les équipements.

---

# Cas d'utilisation dans FindMyCar

FindMyCar pourrait notamment afficher :

- estimation du juste prix ;
- écart entre le prix demandé et le prix estimé ;
- niveau d'opportunité de l'annonce ;
- historique de l'évolution du prix lorsque cette information est disponible.

Ces données viendront alimenter directement le score "Opportunity".

---

# Qualité des données

⭐⭐⭐⭐☆

La qualité dépend fortement du fournisseur retenu.

Les principaux acteurs disposent généralement d'importantes bases de données alimentées par le marché automobile.

---

# Mode d'accès

Principalement :

- API professionnelles ;
- partenariats ;
- licences commerciales.

Certaines estimations sont accessibles publiquement mais leur réutilisation commerciale devra être étudiée.

---

# Contraintes juridiques

Les cotes automobiles sont généralement protégées par des droits de propriété intellectuelle.

FindMyCar devra utiliser uniquement des données obtenues dans un cadre contractuel ou légal.

---

# Coût

Variable.

Les principaux fournisseurs fonctionnent généralement avec :

- abonnements ;
- paiement à la requête ;
- licences professionnelles ;
- contrats spécifiques.

---

# Difficulté d'intégration

⭐⭐⭐☆☆

Technique :

Faible à moyenne.

Business :

Élevée selon les conditions commerciales.

---

# Avantages

- Très forte valeur pour les utilisateurs.
- Permet d'identifier rapidement les bonnes affaires.
- Améliore le score d'opportunité.
- Complète parfaitement les analyses techniques.

---

# Limites

- Les méthodes de calcul sont souvent propriétaires.
- Les estimations restent des approximations.
- La valeur réelle dépend également de l'état du véhicule.

---

# Pertinence pour FindMyCar

⭐⭐⭐⭐⭐

L'estimation de la valeur constitue une fonctionnalité majeure de FindMyCar.

Elle permettra d'expliquer pourquoi une annonce est considérée comme intéressante ou non.

---

# Verdict

🔴 Priorité : Critique

Les fournisseurs de cotes automobiles représentent un composant essentiel pour le futur moteur d'analyse de FindMyCar.

---

# Décision

Décision actuelle :

🟢 Retenu comme composant stratégique.

Actions futures :

- Comparer les principaux fournisseurs.
- Étudier les possibilités de partenariat.
- Concevoir un `PriceProvider` indépendant.
- Définir une méthode permettant de combiner plusieurs estimations lorsque cela est pertinent.

---

# Fournisseurs de données d'entretien et de maintenance

## Présentation

Les fournisseurs de données de maintenance regroupent les bases techniques permettant de connaître les opérations d'entretien recommandées par les constructeurs ainsi que les coûts associés aux réparations courantes.

Ces données permettront à FindMyCar d'aller au-delà de la simple fiabilité en estimant le coût réel de possession d'un véhicule.

---

# Type de fournisseur

Fournisseurs techniques spécialisés.

---

# Couverture

Internationale.

Selon les fournisseurs, plusieurs milliers de modèles peuvent être couverts.

---

# Principaux fournisseurs

- TecAlliance / TecDoc
- Autodata
- HaynesPro
- ALLDATA (selon les marchés)
- Constructeurs automobiles (documentation officielle)
- Réseaux de garages partenaires

---

# Type de données fournies

Les données peuvent inclure :

- plan d'entretien constructeur ;
- périodicité des révisions ;
- intervalles de vidange ;
- remplacement de la distribution ;
- remplacement des consommables ;
- temps de réparation ;
- coût estimatif des opérations ;
- prix des pièces ;
- références des pièces ;
- procédures techniques.

---

# Cas d'utilisation dans FindMyCar

Ces données permettront notamment :

- d'estimer le coût annuel d'entretien ;
- d'anticiper les grosses réparations ;
- d'afficher les prochaines opérations importantes selon le kilométrage ;
- d'alimenter le futur score "Coût de possession".

Exemple :

✔ Distribution à prévoir dans 20 000 km

✔ Coût moyen estimé : 850 €

✔ Révision annuelle : 250 €

✔ Embrayage généralement remplacé après 220 000 km

---

# Qualité des données

⭐⭐⭐⭐☆

Les bases professionnelles sont généralement très fiables et largement utilisées par les ateliers de réparation.

---

# Mode d'accès

Principalement :

- API professionnelles ;
- licences commerciales ;
- partenariats.

---

# Contraintes juridiques

Les données techniques sont généralement protégées.

Toute réutilisation devra respecter les licences accordées par les fournisseurs.

---

# Coût

Variable.

Le coût dépendra du fournisseur et du volume d'utilisation.

---

# Difficulté d'intégration

⭐⭐⭐☆☆

Technique :

Moyenne.

Business :

Moyenne.

---

# Avantages

- Très forte valeur pour les acheteurs.
- Permet d'estimer le coût réel de possession.
- Complète parfaitement les données de fiabilité.
- Données concrètes et facilement compréhensibles.

---

# Limites

- Les coûts peuvent varier selon les régions et les garages.
- Certaines opérations dépendent de l'état réel du véhicule.

---

# Pertinence pour FindMyCar

⭐⭐⭐⭐☆

Cette catégorie de fournisseurs permettra à FindMyCar de proposer une vision beaucoup plus complète du coût réel d'un véhicule.

---

# Verdict

🟠 Priorité : Haute

Ces données représentent un excellent complément aux analyses de fiabilité et de valeur.

---

# Décision

Décision actuelle :

🟢 Retenu comme composant stratégique.

Actions futures :

- Identifier les fournisseurs les plus adaptés.
- Concevoir un `MaintenanceProvider`.
- Étudier la possibilité d'estimer le coût total de possession (TCO).

---

# Sources Open Data

## Présentation

Les plateformes Open Data mettent gratuitement à disposition des données publiques produites par les administrations, organismes publics ou institutions.

Ces données constituent une source particulièrement intéressante pour FindMyCar car elles sont généralement fiables, documentées et réutilisables sous certaines licences.

L'objectif est de compléter les données commerciales par des informations publiques de qualité.

---

# Type de fournisseur

Organismes publics

Institutions

Open Data

---

# Couverture

Principalement nationale ou européenne.

---

# Exemples de sources

France

- data.gouv.fr
- Histovec
- Base Crit'Air
- Campagnes officielles de rappel

Europe

- Euro NCAP
- European Data Portal

International

- OpenStreetMap
- autres bases ouvertes pertinentes

---

# Type de données fournies

Selon les sources :

- données administratives
- rappels constructeurs
- sécurité
- environnement
- émissions
- Crit'Air
- localisation
- statistiques publiques
- réglementation

---

# Cas d'utilisation dans FindMyCar

Ces données permettront notamment :

- enrichissement des analyses ;
- amélioration de la transparence ;
- réduction de la dépendance aux fournisseurs privés ;
- validation de certaines informations.

---

# Qualité des données

⭐⭐⭐⭐☆

Les données publiques sont généralement fiables mais leur qualité dépend de l'organisme producteur.

---

# Mode d'accès

Principalement :

- API publiques
- téléchargements
- fichiers CSV
- fichiers JSON

---

# Contraintes juridiques

Les licences Open Data devront être respectées.

Chaque source devra être étudiée individuellement.

---

# Coût

Gratuit dans la majorité des cas.

---

# Difficulté d'intégration

⭐⭐☆☆☆

Technique :

Faible.

---

# Avantages

- Gratuit.
- Légal.
- Fiable.
- Stable.
- Facile à intégrer.

---

# Limites

- Couverture parfois limitée.
- Données parfois moins riches que les bases commerciales.

---

# Pertinence pour FindMyCar

⭐⭐⭐⭐☆

Les données Open Data constituent un excellent complément aux fournisseurs commerciaux.

---

# Verdict

🟠 Priorité : Haute

Ces données devront être utilisées chaque fois qu'elles permettent d'éviter une dépendance à un fournisseur privé.

---

# Décision

Décision actuelle :

🟢 Retenu.

Actions futures :

- Recenser les principales bases Open Data.
- Vérifier les licences.
- Développer un futur `OpenDataProvider`.