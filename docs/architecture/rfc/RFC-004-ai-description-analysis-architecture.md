# RFC-004 - AI Description Analysis Architecture

## Status

Accepted

---

## Context

FindMyCar currently relies on deterministic scoring criteria to evaluate vehicle listings.
These criteria include compatibility and opportunity analysis such as price, mileage,
freshness, rarity and maintenance information.

While deterministic rules provide predictable and explainable results, many valuable
signals remain hidden inside natural language descriptions.

Examples include:

- maintenance history written in free text;
- seller transparency;
- implicit information;
- inconsistencies;
- contextual explanations.

Simple keyword matching cannot reliably extract this information.

This RFC defines the architecture allowing AI models to analyse listing descriptions
while preserving the deterministic nature of the scoring engine.

---

## Goals

The AI analysis system must:

- understand natural language descriptions;
- extract structured information;
- remain independent from any AI provider;
- allow multiple providers to coexist;
- produce explainable results;
- integrate seamlessly with the scoring engine;
- minimise API costs through caching;
- remain fully testable.

---

## Non-goals

The AI system must **not**:

- assign scores directly;
- make business decisions;
- replace deterministic scoring criteria;
- become mandatory for FindMyCar to operate;
- expose provider-specific implementations to the scoring engine.

The scoring engine always remains the single source of truth.

---

## Design Principles

The AI architecture follows the same principles as the rest of FindMyCar.

- Business logic always remains deterministic.
- External services provide information, never decisions.
- Components communicate through explicit contracts.
- Every component should be independently testable.
- AI is optional, never mandatory.

These principles are intended to guide future AI integrations and maintain a
consistent architecture across the project.

---

## High-level Architecture

```
services/
└── ai/
    ├── description_analyzer.py
    ├── prompt_builder.py
    ├── analysis_result.py
    ├── cache.py
    └── providers/
        ├── base.py
        ├── openai.py
        ├── mistral.py
        └── ollama.py
```

### Responsibilities

- `PromptBuilder` builds prompts.
- `Providers` communicate with external AI services.
- `DescriptionAnalyzer` orchestrates the complete workflow.
- `AnalysisResult` stores structured outputs.
- `Cache` avoids unnecessary analyses.

---

## AI Provider Abstraction

The scoring engine must never depend on a specific AI provider.

Instead, every provider implements a common interface.

Example:

```python
class AIProvider(ABC):

    @abstractmethod
    def analyze(
        self,
        prompt: str,
    ) -> AnalysisResult:
        ...
```

This abstraction allows changing providers without modifying business logic.

---

## AnalysisResult

AI providers must return structured information rather than scores.

Example:

```python
@dataclass(slots=True)
class AnalysisResult:

    maintenance_items: list[str]

    transparency_signals: list[str]

    positive_points: list[str]

    warning_points: list[str]

    extracted_facts: list[str]

    confidence: float
```

The scoring engine remains responsible for converting these findings into
Opportunity points.

---

## Prompt Strategy

Prompt generation is centralised inside `PromptBuilder`.

Providers receive fully prepared prompts and never construct prompts
themselves.

Workflow:

```
Listing Description
        │
        ▼
PromptBuilder
        │
        ▼
AI Provider
        │
        ▼
AnalysisResult
        │
        ▼
Scoring Engine
```

This separation guarantees consistent prompts across all providers.

---

## Caching

AI analysis may become expensive.

Repeated analysis of an unchanged description should be avoided.

The cache key should depend on:

- listing identifier;
- description content;
- prompt version;
- provider.

Changing any of these values invalidates the cache.

---

## Error Handling

AI analysis is considered optional.

Possible failures include:

- network failure;
- timeout;
- provider unavailable;
- invalid response.

In these situations:

- no AI opportunity score is assigned;
- deterministic scoring continues normally;
- failures are logged.

The application must never fail because AI analysis is unavailable.

---

## Future Extensions

Possible future capabilities include:

- maintenance detection using semantic analysis;
- seller credibility estimation;
- modification detection;
- contradiction detection;
- vehicle history extraction;
- automatic strengths and weaknesses summary;
- photo analysis;
- advertisement quality evaluation.

These extensions should reuse the same architecture whenever possible.

---

## Consequences

### Advantages

- provider independence;
- deterministic business logic;
- explainable scoring;
- easy unit testing;
- modular architecture;
- scalable AI integration;
- future-proof design.

### Drawbacks

- additional abstraction layer;
- more components to maintain;
- AI responses require validation before use.

These drawbacks are considered acceptable given the long-term flexibility
provided by the architecture.

---

## Guiding Principle

> **AI assists the scoring engine.**
>
> **AI never replaces the scoring engine.**
>
> **Business decisions always remain under the control of FindMyCar.**