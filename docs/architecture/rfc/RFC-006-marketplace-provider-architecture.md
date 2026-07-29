# RFC-006 — Marketplace Provider Architecture

**Status:** Accepted

**Authors:** FindMyCar

**Created:** 2026-07-27

---

# 1. Context

FindMyCar relies on vehicle listings retrieved from external marketplaces such as Leboncoin, La Centrale or AutoScout24.

These platforms expose different data formats, different field names and different technical constraints.

The application must therefore isolate all marketplace-specific logic from the business logic.

The scoring engine, ranking engine and AI analysis must never depend on a specific marketplace.

---

# 2. Problem

Without a dedicated provider architecture:

* every marketplace would require modifications throughout the application;
* business logic would become coupled to external websites;
* adding a new marketplace would become increasingly expensive;
* testing would require Internet access and external services.

The application needs a single abstraction responsible for data acquisition.

---

# 3. Decision

Every marketplace shall implement the `ListingProvider` interface.

```python
class ListingProvider(ABC):

    @abstractmethod
    def search(
        self,
        search: Search,
    ) -> list[Listing]:
        ...
```

The provider receives a `Search` object and always returns a list of normalized `Listing` objects.

No other return type is allowed.

---

# 4. Responsibilities

A provider is responsible for:

* retrieving listings from an external source;
* parsing external data;
* converting marketplace-specific fields into FindMyCar models;
* normalizing values;
* ignoring invalid listings;
* reporting provider failures.

A provider is **not** responsible for:

* compatibility scoring;
* opportunity scoring;
* ranking;
* AI analysis;
* business decisions;
* user recommendations.

Providers acquire data.

The scoring engine makes decisions.

---

# 5. Normalization

Providers always return normalized `Listing` objects.

Example:

Marketplace data

```text
Fuel: "Ess."
Gearbox: "Manuelle"
Price: "8 500 €"
```

Normalized result

```python
Listing(
    fuel=FuelType.GASOLINE,
    gearbox=GearboxType.MANUAL,
    price=8500,
)
```

No marketplace-specific values shall leave the provider layer.

---

# 6. Required fields

Some fields are mandatory.

Examples:

* price
* brand
* model

If one of these fields cannot be determined, the listing shall be ignored.

Optional information may remain `None`.

Examples:

* number of doors
* publication date
* coordinates
* version

The scoring engine already supports incomplete data.

---

# 7. Invalid listings

Invalid listings shall never stop an entire search.

Instead, providers ignore invalid listings and continue processing the remaining results.

The objective is to maximize usable listings while maintaining data quality.

---

# 8. Error handling

When a provider cannot retrieve data because of an infrastructure problem, it shall raise:

```python
ProviderError
```

Providers shall never return `None`.

Infrastructure failures must always be explicit.

---

# 9. Filtering

Providers should use marketplace filters whenever possible to reduce unnecessary traffic.

However, providers never perform business filtering.

They may return listings that do not perfectly match the requested search.

The scoring engine remains the single source of truth for evaluating listing relevance.

---

# 10. Pagination

Pagination is intentionally excluded from V1.

Providers retrieve a single page of results.

Multi-page retrieval will be introduced in a future version if required.

---

# 11. Repository integration

Providers are never used directly by the application.

All interactions go through `ListingRepository`.

```
Search
    │
    ▼
ListingRepository
    │
    ▼
ListingProvider
    │
    ▼
Marketplace
```

This abstraction allows future additions such as:

* caching;
* multiple providers;
* local storage;
* offline datasets.

Without changing the business layer.

---

# 12. Design principles

The provider layer follows these principles:

* Single Responsibility Principle.
* Dependency Inversion Principle.
* Marketplace independence.
* Infrastructure isolated from business logic.
* Normalized domain models only.

Providers translate external data.

The business layer evaluates it.

---

# 13. Consequences

Advantages:

* adding a new marketplace requires implementing only one interface;
* business logic remains completely independent of external websites;
* providers can be tested independently;
* fake providers enable deterministic tests without Internet access;
* the application remains easily extensible.

Trade-offs:

* each provider must implement its own normalization logic;
* initial implementation effort is slightly higher than direct scraping;
* providers must be maintained when marketplace structures evolve.

---

# 14. Future evolution

Potential future improvements include:

* multi-provider aggregation;
* pagination;
* asynchronous providers;
* retry policies;
* request throttling;
* caching;
* dedicated `ListingNormalizer` shared across providers;
* provider health monitoring;
* provider metrics;
* duplicate listing detection across marketplaces.

These improvements are intentionally postponed to keep V1 simple and maintainable.

---

# 15. Guiding principle

**Providers never make business decisions.**

Their responsibility is limited to acquiring external data and converting it into reliable, normalized `Listing` objects.

All business intelligence—including compatibility scoring, opportunity analysis, ranking and future recommendations—remains centralized inside the FindMyCar scoring engine.

This separation ensures that the application's intelligence stays independent of any marketplace and that new providers can be added without impacting the core domain.

Un provider peut récupérer ses données via HTML, API publique ou API interne. Le reste de l'application ne doit jamais connaître le mécanisme utilisé.