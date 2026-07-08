# Directives de développement

## Objectif

Ce document définit les principes d'ingénierie appliqués tout au long du projet FindMyCar.

Toute décision relative à l’architecture et à la mise en œuvre doit respecter ces directives.

---

# 1. L’architecture avant tout

Nous privilégions une architecture claire et facile à maintenir plutôt que la rapidité d’écriture du code.

Le code peut être réécrit.
L’architecture doit rester stable.

---

# 2. Principe de responsabilité unique

Chaque classe doit avoir une seule responsabilité.

Exemples :

- SearchEngine orchestre les recherches.
- MatchingService vérifie si une annonce correspond à une recherche.
- ScoringService évalue la qualité des annonces.
- NotificationService envoie des notifications.

---

# 3. Injection de dépendances

Une classe doit recevoir ses dépendances via son constructeur.

Bon :

SearchEngine(provider_manager, matching_service)

Mauvais :

SearchEngine crée son propre ProviderManager.

Cela améliore les tests, la flexibilité et la maintenabilité.

---

# 4. Isolation du domaine

Les modèles de domaine ne doivent pas dépendre de :

- Telegram
- SQLite
- Fournisseurs
- API
- Interface utilisateur

Les modèles ne représentent que des concepts métier.

---

# 5. API publique réduite

Les classes doivent exposer le moins de méthodes publiques possible.

La logique complexe doit être décomposée en petites méthodes privées.

Exemple :

matches()

↓

_match_brand()

_match_model()

_match_price()

---

# 6. Code explicite

Le code doit être facile à comprendre sans explications supplémentaires.

Évitez le code « astucieux ».

Privilégiez un code lisible.

---

# 7. Documentation

Chaque classe publique doit comporter une chaîne de documentation (docstring).

Les décisions architecturales importantes doivent être documentées à l'aide d'ADR.

Les propositions de conception d’envergure doivent faire l’objet de discussions via des RFC avant leur mise en œuvre.

---

# 8. Workflow Git

Le développement s’effectue sur la branche « dev ».

La branche principale reste toujours stable.

Chaque commit doit correspondre à un changement logique.

Les messages de commit respectent les conventions de Conventional Commits.

---

# 9. Tests

La logique métier doit être testable.

Dans la mesure du possible :

- tests unitaires
- tests d’intégration

Les tests manuels doivent être évités lorsque des tests automatisés sont possibles.

---

# 10. Extensibilité

Lors de l’ajout d’une nouvelle fonctionnalité, posez-vous la question suivante :

« Combien de fichiers existants doivent être modifiés ? »

L’objectif est de minimiser les modifications apportées au code existant.

Ouvert à l’extension.

Fermé à la modification.

---

# 11. Performances

On évite l’optimisation prématurée.

Les optimisations de performances ne sont introduites que lorsqu’elles sont justifiées par des mesures ou des besoins réels.

---

# 12. Gestion des erreurs

Les erreurs doivent être explicites.

Privilégiez les exceptions personnalisées aux exceptions génériques.

Les situations inattendues ne doivent jamais entraîner d’échec silencieux.

---

# 13. Simplicité

On privilégie les solutions simples.

La complexité doit toujours être justifiée.

---

# 14. Amélioration continue

L’architecture est censée évoluer.

La refactorisation est encouragée lorsqu’elle améliore la lisibilité ou la maintenabilité.

La dette technique doit être suivie et traitée.

---

# Principe final

Chaque contribution doit laisser le projet dans un meilleur état qu’auparavant.