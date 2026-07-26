from models.partial_score import PartialScore

from services.scoring.score_aggregator import ScoreAggregator


def make_partial_score(
    score: float,
) -> PartialScore:
    return PartialScore(
        score=score,
        breakdowns=[],
    )


def test_returns_final_score():
    aggregator = ScoreAggregator()

    result = aggregator.aggregate(
        make_partial_score(75),
        make_partial_score(75),
    )

    assert result.total == 100
    assert result.compatibility == 75
    assert result.opportunity == 25


def test_zero_scores_return_zero():
    aggregator = ScoreAggregator()

    result = aggregator.aggregate(
        make_partial_score(0),
        make_partial_score(0),
    )

    assert result.total == 0
    assert result.compatibility == 0
    assert result.opportunity == 0


def test_preserves_breakdowns():
    aggregator = ScoreAggregator()

    compatibility = make_partial_score(75)
    opportunity = make_partial_score(75)

    result = aggregator.aggregate(
        compatibility,
        opportunity,
    )

    assert (
        result.compatibility_breakdowns
        == compatibility.breakdowns
    )

    assert (
        result.opportunity_breakdowns
        == opportunity.breakdowns
    )


def test_half_scores_are_normalized():
    aggregator = ScoreAggregator()

    result = aggregator.aggregate(
        make_partial_score(37.5),
        make_partial_score(37.5),
    )

    assert result.compatibility == 38
    assert result.opportunity == 12
    assert result.total == 50


def test_normalize_returns_zero_when_max_score_is_zero():
    assert (
        ScoreAggregator._normalize(
            10,
            0,
            75,
        )
        == 0
    )