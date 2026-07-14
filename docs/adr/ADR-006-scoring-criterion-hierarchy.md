# ADR-006 — Introduce a NumericCriterion hierarchy

## Status

Accepted

---

## Context

The scoring system is built around independent criteria, each responsible for evaluating one aspect of a vehicle listing.

The first implemented criteria were:

* PriceCriterion
* MileageCriterion

During implementation, it became clear that both classes shared almost the same evaluation algorithm:

* Missing listing value handling
* Missing user limit handling
* Value comparison
* Tolerance management
* Progressive score decrease
* Score clamping
* ScoreBreakdown generation

The only differences were:

* the evaluated field (`price`, `mileage`, etc.)
* the maximum number of points
* the displayed messages
* the comparison direction (minimum or maximum accepted value)

Duplicating this algorithm in every numeric criterion would increase maintenance cost and the risk of inconsistencies.

---

## Decision

A new abstract class named `NumericCriterion` will be introduced.

`NumericCriterion` will contain the complete evaluation algorithm shared by every numeric criterion.

Concrete criteria such as `PriceCriterion`, `MileageCriterion` and `YearCriterion` will only provide:

* the value extracted from the listing
* the value extracted from the search
* the criterion display name
* the maximum number of points
* the user-facing messages

The comparison behavior will be configurable through a comparison mode rather than hardcoded logic.

Example:

* `ComparisonMode.MAXIMUM`
* `ComparisonMode.MINIMUM`

This allows the same evaluation algorithm to support different business rules without code duplication.

---

## Consequences

### Advantages

* Single implementation of the numeric scoring algorithm.
* Consistent behavior across all numeric criteria.
* Easier maintenance.
* Easier testing.
* Reduced duplication.
* Future numeric criteria become very small and focused.

Examples of future reusable criteria include:

* Year
* Mileage
* Price
* Engine power
* CO₂ emissions
* Electric range
* Fuel consumption
* Distance

---

### Drawbacks

The hierarchy introduces one additional abstraction.

However, this abstraction is justified because multiple implemented criteria already share the same behavior.

---

## Alternatives considered

### Duplicate the algorithm

Rejected.

Although initially simpler, duplicated implementations would become harder to maintain as more numeric criteria are introduced.

### Use a boolean flag (`HIGHER_IS_BETTER`)

Rejected.

While functional, this approach describes the result of the comparison rather than the business rule itself.

Using comparison modes such as `MAXIMUM` and `MINIMUM` better represents how users express their search criteria and leaves room for future extensions, such as range-based comparisons.

---

## Future evolution

`NumericCriterion` may later support additional comparison modes, including:

* `RANGE`
* `EXACT_VALUE`

without requiring changes to existing criteria.

This design keeps the scoring engine open for extension while remaining closed for modification, following the Open/Closed Principle.
