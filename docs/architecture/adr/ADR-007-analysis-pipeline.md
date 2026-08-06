# ADR-007 — Analysis Pipeline Architecture

**Status:** Accepted

**Date:** 2026-08-03

---

# Context

Sprint 3 introduces the core intelligence of FindMyCar.

Initially, the project considered implementing a single `AnalysisEngine` responsible for:

* executing all analyses;
* computing the global score;
* generating recommendations;
* producing the final analysis object.

Although functional, this approach would quickly violate the Single Responsibility Principle (SRP).

As the project grows, new analysis modules will be introduced:

* VIN analysis
* Histovec analysis
* Euro NCAP analysis
* Reliability analysis
* Maintenance analysis
* Price analysis
* Environmental analysis
* Insurance analysis
* Ownership analysis
* Recall analysis
* AI analysis
* and many others.

Keeping all responsibilities inside one engine would create a large, difficult-to-maintain component.

---

# Decision

The analysis process is divided into independent stages forming a processing pipeline.

```text
Search
        │
        ▼
Listing
        │
        ▼
AnalysisEngine
        │
        ▼
AnalysisBundle
        │
        ▼
ScoringEngine
        │
        ▼
Score
        │
        ▼
RecommendationEngine
        │
        ▼
CompleteAnalysis
```

Each stage has a single responsibility.

---

# Responsibilities

## AnalysisEngine

Responsible for orchestrating every analyzer.

Inputs:

* Search
* Listing

Output:

* AnalysisBundle

Responsibilities:

* Execute all registered analyzers.
* Collect their results.
* Build an immutable AnalysisBundle.

It must **not** calculate scores.

It must **not** generate recommendations.

It must **not** contain business rules.

---

## AnalysisBundle

Immutable object containing every analysis result.

Example:

* TechnicalAnalysis
* ReliabilityAnalysis
* PriceAnalysis
* MaintenanceAnalysis
* SafetyAnalysis
* AIAnalysis

This object represents the complete analysis state before scoring.

---

## ScoringEngine

Responsible for transforming an AnalysisBundle into a Score.

Responsibilities:

* Compute compatibility score.
* Compute opportunity score.
* Produce the final Score object.

The scoring algorithm is completely isolated from the analysis process.

Future scoring strategies can therefore evolve independently.

---

## RecommendationEngine

Responsible for producing user recommendations.

Inputs:

* AnalysisBundle
* Score

Outputs:

* Recommendations

Recommendations may include:

* maintenance advice;
* buying warnings;
* positive highlights;
* inspection checklist;
* negotiation opportunities.

---

## CompleteAnalysis

Final immutable object returned by the application.

Contains:

* Listing
* AnalysisBundle
* Score
* Recommendations

This object represents the complete evaluation of a vehicle.

It contains data only.

No business logic.

---

# Architectural Principles

The pipeline follows several architectural principles.

## Single Responsibility Principle

Each engine performs exactly one task.

---

## Open / Closed Principle

New analysis modules can be added without modifying existing engines.

Example:

* VINAnalysis
* EnvironmentalAnalysis
* RecallAnalysis

These modules only extend AnalysisBundle and register a new Analyzer.

---

## Separation of Concerns

Analysis, scoring and recommendations are completely independent.

Each component can evolve without impacting the others.

---

## Immutability

All analysis models are immutable dataclasses.

Business logic belongs exclusively to services.

---

## Testability

Each engine can be tested independently.

* AnalysisEngine tests orchestration.
* ScoringEngine tests scoring algorithms.
* RecommendationEngine tests recommendation generation.

No engine depends on the internal implementation of another.

---

# Consequences

Advantages:

* Highly modular architecture.
* Easy to extend.
* Easy to test.
* Easy to maintain.
* Future-proof design.
* Supports multiple scoring strategies.
* Supports multiple recommendation strategies.
* Facilitates future plugins and external providers.

Trade-offs:

* More classes.
* More services.
* More objects exchanged.

This additional complexity is intentional and acceptable considering the long-term ambitions of FindMyCar.

---

# Rationale

FindMyCar is not designed as a simple classifieds aggregator.

Its primary value lies in analyzing, interpreting and explaining vehicle information.

The project therefore adopts a pipeline architecture where each stage transforms information into higher-value knowledge.

This decision establishes the long-term architecture of the intelligence layer and serves as the foundation for future analysis modules.
