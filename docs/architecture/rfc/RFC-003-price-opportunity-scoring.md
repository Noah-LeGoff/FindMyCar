# RFC-003 — Price Opportunity Scoring

- Status: Accepted
- Date: 2026-07-15

## Context

FindMyCar aims to help users identify the most interesting car listings, not only the ones matching their search criteria.

Compatibility scoring determines whether a listing matches the user's expectations.

Opportunity scoring determines whether a listing represents a good opportunity compared to similar listings currently available on the market.

This RFC defines the long-term vision of the Price Opportunity scoring system and the implementation strategy adopted for each version of the project.

---

# Decision

The opportunity engine does not attempt to estimate the intrinsic value of a vehicle.

Instead, it evaluates whether a listing offers a better value than comparable listings available at the time of the analysis.

Price opportunity is therefore a relative metric rather than an absolute vehicle valuation.

---

# Design Principles

The following principles guide every evolution of the opportunity scoring engine.

## Simplicity first

The first implementation should remain simple, understandable and easily testable.

Complexity will only be introduced when justified by real data.

---

## Incremental evolution

The scoring engine is designed to evolve progressively.

Each new version should improve the quality of the opportunity score without breaking previous implementations.

---

## Modular criteria

Each opportunity criterion evaluates exactly one aspect of a listing.

Examples include:

- Freshness
- Price Opportunity
- Price Drop
- Rarity
- Maintenance
- AI Description Analysis

Each criterion contributes independently to the final score.

---

## Positive scoring only

Opportunity criteria reward interesting listings.

They never apply negative points.

Listings that are more expensive than the market simply receive no bonus.

---

## Explainability

Every awarded point must be explainable.

Users should eventually be able to understand why a listing obtained its score through detailed score breakdowns.

Example:

- Recently published
- Price below market median
- Rare model
- Recent maintenance detected

---

# Roadmap

## Version 1

The first implementation compares listings against currently available comparable listings.

Comparison group:

- same brand
- same model

The comparison relies on the market snapshot available during scoring.

The system does not estimate vehicle value.

It only ranks currently available opportunities.

---

## Version 2

FindMyCar progressively builds its own historical database.

Historical market statistics become available:

- median prices
- yearly evolution
- mileage distribution
- engine-specific statistics
- trim-level statistics

Historical data gradually improves the opportunity score.

---

## Version 3

The scoring engine becomes market-aware.

Vehicle valuation considers multiple dimensions simultaneously:

- historical prices
- rarity
- maintenance history
- detected equipment
- AI description analysis
- historical price drops
- market trends

The engine estimates whether a vehicle is undervalued compared to similar vehicles.

---

# Market Comparison

Version 1 compares listings using:

- identical brand
- identical model

Future versions may refine comparisons using:

- engine
- trim
- production year
- mileage range
- gearbox
- fuel

---

# Minimum Sample Size

Price opportunity is only evaluated when enough comparable listings exist.

A configurable minimum sample size prevents unreliable statistics.

Example:

```python
MIN_SAMPLE_SIZE = 10
```

If the sample size is insufficient, no opportunity bonus is awarded.

---

# Statistical Metric

Median price is used instead of arithmetic mean.

Reasons:

- resistant to outliers
- robust against abnormal listings
- more representative of the real market

---

# Invalid Listings

Listings considered invalid are ignored during market statistics.

Examples include:

- price = 1 €
- exchange-only listings
- invalid prices
- missing prices

These listings may still appear in search results but never influence market statistics.

---

# Score Cap

Price opportunity awards a bounded bonus.

Very underpriced vehicles cannot dominate the complete scoring engine.

Each opportunity criterion remains balanced with compatibility criteria.

---

# Future Opportunity Criteria

The following criteria are planned independently.

- FreshnessCriterion
- PriceOpportunityCriterion
- PriceDropCriterion
- RarityCriterion
- MaintenanceCriterion
- DescriptionAICriterion

Each criterion has a single responsibility.

---

# Future Architecture

Future versions may introduce a market analysis layer.

Example:

Listing
    ↓
MarketAnalyzer
    ↓
MarketSnapshot
    ↓
PriceOpportunityCriterion

This separates market analysis from scoring while allowing multiple criteria to reuse the same market data.

---

# Consequences

Advantages

- simple V1 implementation
- scalable architecture
- explainable scoring
- modular evolution
- robust statistics
- independent opportunity criteria

Trade-offs

- V1 relies only on currently available listings
- market quality depends on sample size
- sophisticated valuation is postponed to later versions

This trade-off is intentional in order to deliver a reliable and maintainable first implementation.