from unittest.mock import Mock, patch

from models.analysis.analysis_bundle import AnalysisBundle
from models.score.factor_score import FactorScore
from models.score.score import Score

from services.scoring.scoring_engine import ScoringEngine
from services.scoring.factors.score_factor import ScoreFactor


def make_factor(name: str):
    factor = Mock(spec=ScoreFactor)
    factor.compute.return_value = FactorScore(
        name=name,
        score=50.0,
        explanation="Test",
    )
    return factor


def test_calls_every_factor():
    bundle = Mock(spec=AnalysisBundle)

    factors = (
        make_factor("Price"),
        make_factor("Reliability"),
        make_factor("Maintenance"),
        make_factor("Safety"),
        make_factor("AI"),
    )

    engine = ScoringEngine(factors)

    with patch.object(
        Score,
        "from_factors",
        return_value=Mock(spec=Score),
    ):
        engine.compute(bundle)

    for factor in factors:
        factor.compute.assert_called_once_with(bundle)


def test_builds_score_from_factor_scores():
    bundle = Mock(spec=AnalysisBundle)

    factors = (
        make_factor("Price"),
        make_factor("Reliability"),
        make_factor("Maintenance"),
        make_factor("Safety"),
        make_factor("AI"),
    )

    expected_scores = [
        factor.compute.return_value
        for factor in factors
    ]

    engine = ScoringEngine(factors)

    with patch.object(
        Score,
        "from_factors",
        return_value=Mock(spec=Score),
    ) as from_factors:
        engine.compute(bundle)

    from_factors.assert_called_once_with(expected_scores)


def test_returns_score():
    bundle = Mock(spec=AnalysisBundle)

    expected_score = Mock(spec=Score)

    engine = ScoringEngine(())

    with patch.object(
        Score,
        "from_factors",
        return_value=expected_score,
    ):
        result = engine.compute(bundle)

    assert result is expected_score


def test_supports_empty_factor_collection():
    bundle = Mock(spec=AnalysisBundle)

    engine = ScoringEngine(())

    with patch.object(
        Score,
        "from_factors",
        return_value=Mock(spec=Score),
    ) as from_factors:
        engine.compute(bundle)

    from_factors.assert_called_once_with([])