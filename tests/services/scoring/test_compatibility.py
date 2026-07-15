from models.partial_score import PartialScore

from services.scoring.compatibility import CompatibilityScorer
from services.scoring.criteria import COMPATIBILITY_CRITERIA
from tests.factories import make_listing, make_search


def test_score_returns_partial_score():
    scorer = CompatibilityScorer()

    result = scorer.compute(
        make_search(),
        make_listing(),
    )

    assert isinstance(result, PartialScore)


def test_score_equals_sum_of_breakdowns():
    scorer = CompatibilityScorer()

    result = scorer.compute(
        make_search(),
        make_listing(),
    )

    assert result.score == sum(
        breakdown.points
        for breakdown in result.breakdowns
    )
    assert len(result.breakdowns) == 6


def test_compatibility_contains_three_criteria():
    assert len(COMPATIBILITY_CRITERIA) == 6


def test_all_breakdowns_are_returned():
    scorer = CompatibilityScorer()

    result = scorer.compute(
        make_search(),
        make_listing(),
    )

    assert len(result.breakdowns) == len(COMPATIBILITY_CRITERIA)