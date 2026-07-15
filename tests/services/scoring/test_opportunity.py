from models.partial_score import PartialScore

from services.scoring.opportunity import OpportunityScorer

from tests.factories import make_listing, make_search


def test_compute_returns_partial_score():
    scorer = OpportunityScorer()

    result = scorer.compute(
        make_search(),
        make_listing(),
    )

    assert isinstance(result, PartialScore)


def test_empty_criteria_returns_zero_score():
    scorer = OpportunityScorer()

    result = scorer.compute(
        make_search(),
        make_listing(),
    )

    assert result.score == 0


def test_empty_criteria_returns_no_breakdowns():
    scorer = OpportunityScorer()

    result = scorer.compute(
        make_search(),
        make_listing(),
    )

    assert result.breakdowns == []