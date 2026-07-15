from models.listing import Listing
from models.partial_score import PartialScore
from models.search import Search

from services.scoring.compatibility import CompatibilityScorer
from services.scoring.criteria import COMPATIBILITY_CRITERIA


def test_score_returns_partial_score():
    scorer = CompatibilityScorer()

    search = Search(
        id=1,
        user_id=1,
    )

    listing = Listing(
        source="Leboncoin",
        title="BMW",
        brand="BMW",
        model="E36",
    )

    result = scorer.compute(search, listing)

    assert isinstance(result, PartialScore)


def test_score_equals_sum_of_breakdowns():
    scorer = CompatibilityScorer()

    search = Search(
        id=1,
        user_id=1,
    )

    listing = Listing(
        source="Leboncoin",
        title="BMW",
        brand="BMW",
        model="E36",
    )

    result = scorer.compute(search, listing)

    assert result.score == sum(
        breakdown.points
        for breakdown in result.breakdowns
    )
    assert len(result.breakdowns) == 4


def test_compatibility_contains_three_criteria():
    assert len(COMPATIBILITY_CRITERIA) == 4


def test_all_breakdowns_are_returned():
    scorer = CompatibilityScorer()

    search = Search(
        id=1,
        user_id=1,
    )

    listing = Listing(
        source="Leboncoin",
        title="BMW",
        brand="BMW",
        model="E36",
    )

    result = scorer.compute(search, listing)

    assert len(result.breakdowns) == len(COMPATIBILITY_CRITERIA)