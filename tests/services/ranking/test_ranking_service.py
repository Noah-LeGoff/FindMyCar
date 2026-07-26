from models.final_score import FinalScore
from models.scored_listing import ScoredListing

from services.ranking.ranking_service import RankingService

from tests.factories import make_listing


def make_scored_listing(
    total: float,
) -> ScoredListing:
    return ScoredListing(
        listing=make_listing(),
        score=FinalScore(
            total=total,
            compatibility=0,
            opportunity=0,
            compatibility_breakdowns=[],
            opportunity_breakdowns=[],
        ),
    )


def test_returns_sorted_list():
    service = RankingService()

    listings = [
        make_scored_listing(70),
        make_scored_listing(95),
        make_scored_listing(82),
    ]

    result = service.rank(listings)

    assert result[0].score.total == 95
    assert result[1].score.total == 82
    assert result[2].score.total == 70


def test_empty_list_returns_empty_list():
    service = RankingService()

    result = service.rank([])

    assert result == []


def test_single_listing_returns_same_listing():
    service = RankingService()

    listing = make_scored_listing(88)

    result = service.rank([listing])

    assert result == [listing]


def test_preserves_order_for_equal_scores():
    service = RankingService()

    first = make_scored_listing(90)
    second = make_scored_listing(90)
    third = make_scored_listing(90)

    result = service.rank(
        [
            first,
            second,
            third,
        ]
    )

    assert result == [
        first,
        second,
        third,
    ]


def test_highest_score_is_first():
    service = RankingService()

    listings = [
        make_scored_listing(25),
        make_scored_listing(100),
        make_scored_listing(50),
        make_scored_listing(80),
    ]

    result = service.rank(listings)

    assert result[0].score.total == 100


def test_lowest_score_is_last():
    service = RankingService()

    listings = [
        make_scored_listing(100),
        make_scored_listing(80),
        make_scored_listing(40),
        make_scored_listing(5),
    ]

    result = service.rank(listings)

    assert result[-1].score.total == 5