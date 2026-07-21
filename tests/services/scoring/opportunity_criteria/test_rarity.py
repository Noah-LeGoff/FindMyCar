from services.scoring.opportunity_criteria.rarity import (
    RarityCriterion,
)

from tests.factories import (
    make_listing,
    make_market,
    make_search,
)


def test_returns_zero_when_market_is_empty():
    criterion = RarityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(),
        make_market(),
    )

    assert result.points == 0


def test_returns_max_points_when_market_contains_ten_or_fewer_listings():
    criterion = RarityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(),
        make_market(
            *([10000] * 10),
        ),
    )

    assert result.points == criterion.MAX_POINTS


def test_returns_fifteen_points_when_market_contains_between_eleven_and_twenty_listings():
    criterion = RarityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(),
        make_market(
            *([10000] * 15),
        ),
    )

    assert result.points == 15


def test_returns_ten_points_when_market_contains_between_twenty_one_and_fifty_listings():
    criterion = RarityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(),
        make_market(
            *([10000] * 35),
        ),
    )

    assert result.points == 10


def test_returns_five_points_when_market_contains_between_fifty_one_and_one_hundred_listings():
    criterion = RarityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(),
        make_market(
            *([10000] * 75),
        ),
    )

    assert result.points == 5


def test_returns_zero_when_market_contains_more_than_one_hundred_listings():
    criterion = RarityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(),
        make_market(
            *([10000] * 150),
        ),
    )

    assert result.points == 0


def test_returns_reason_for_very_rare_vehicle():
    criterion = RarityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(),
        make_market(
            *([10000] * 5),
        ),
    )

    assert result.reason == "Vehicle is very rare on the market."


def test_returns_reason_for_common_vehicle():
    criterion = RarityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(),
        make_market(
            *([10000] * 150),
        ),
    )

    assert result.reason == "Vehicle is very common on the market."