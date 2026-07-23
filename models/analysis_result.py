from dataclasses import dataclass, field


@dataclass(slots=True)
class AnalysisResult:
    """
    Structured information extracted from a listing description by an AI
    provider.

    This model intentionally contains no business logic.
    It only represents the facts extracted by the AI.
    """

    maintenance_items: list[str] = field(default_factory=list)

    transparency_signals: list[str] = field(default_factory=list)

    positive_points: list[str] = field(default_factory=list)

    warning_points: list[str] = field(default_factory=list)

    extracted_facts: list[str] = field(default_factory=list)

    confidence: float = 0.0