from services.scoring.criteria.price import PriceCriterion

from models.listing import Listing
from models.search import Search


def make_search(**kwargs) -> Search:
    data = {
        "id": 1,
        "user_id": 1,
        "max_price": 15_000,
    }

    data.update(kwargs)

    return Search(**data)


def make_listing(**kwargs) -> Listing:
    data = {
        "source": "Leboncoin",
        "title": "BMW E36",
        "brand": "BMW",
        "model": "E36",
        "price": 14_000,
    }

    data.update(kwargs)

    return Listing(**data)


def test_invalid_price_returns_zero():
    criterion = PriceCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(price=1),
    )

    assert result.points == 0


def test_missing_price_returns_zero():
    criterion = PriceCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(price=None),
    )

    assert result.points == 0


def test_without_budget_returns_max_points():
    criterion = PriceCriterion()

    result = criterion.evaluate(
        make_search(max_price=None),
        make_listing(price=14_000),
    )

    assert result.points == criterion.MAX_POINTS


def test_price_within_budget_returns_max_points():
    criterion = PriceCriterion()

    result = criterion.evaluate(
        make_search(max_price=15_000),
        make_listing(price=14_500),
    )

    assert result.points == criterion.MAX_POINTS


def test_price_within_tolerance_returns_max_points():
    criterion = PriceCriterion()

    result = criterion.evaluate(
        make_search(max_price=15_000),
        make_listing(price=15_700),  # +4.67 %
    )

    assert result.points == criterion.MAX_POINTS


def test_price_above_tolerance_is_penalized():
    criterion = PriceCriterion()

    result = criterion.evaluate(
        make_search(max_price=15_000),
        make_listing(price=16_500),  # +10 %
    )

    assert 0 < result.points < criterion.MAX_POINTS


def test_price_above_thirty_percent_returns_zero():
    criterion = PriceCriterion()

    result = criterion.evaluate(
        make_search(max_price=15_000),
        make_listing(price=20_000),  # +33 %
    )

    assert result.points == 0


def test_price_exactly_at_tolerance_returns_max_points():
    criterion = PriceCriterion()

    result = criterion.evaluate(
        make_search(max_price=15_000),
        make_listing(price=15_750),  # +5 %
    )

    assert result.points == criterion.MAX_POINTS


def test_price_exactly_at_max_over_budget_returns_zero():
    criterion = PriceCriterion()

    result = criterion.evaluate(
        make_search(max_price=15_000),
        make_listing(price=19_500),  # +30 %
    )

    assert result.points == 0