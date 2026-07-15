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


def test_compute_returns_zero_score_when_no_points_are_awarded():
    scorer = OpportunityScorer()

    result = scorer.compute(
        make_search(),
        make_listing(),
    )

    assert result.score == 0


def test_compute_returns_all_criterion_breakdowns():
    scorer = OpportunityScorer()

    result = scorer.compute(
        make_search(),
        make_listing(),
    )

    names = [
        breakdown.criterion
        for breakdown in result.breakdowns
    ]

    assert names == [
        "Freshness",
        "Price Opportunity",
    ]