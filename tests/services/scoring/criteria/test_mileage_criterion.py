from services.scoring.criteria.mileage import MileageCriterion

from models.listing import Listing
from models.search import Search


def make_search(**kwargs) -> Search:
    data = {
        "id": 1,
        "user_id": 1,
        "max_mileage": 120_000,
    }

    data.update(kwargs)

    return Search(**data)


def make_listing(**kwargs) -> Listing:
    data = {
        "source": "Leboncoin",
        "title": "BMW E36",
        "brand": "BMW",
        "model": "E36",
        "mileage": 110_000,
    }

    data.update(kwargs)

    return Listing(**data)


def test_missing_mileage_returns_zero():
    criterion = MileageCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(mileage=None),
    )

    assert result.points == 0


def test_without_max_mileage_returns_max_points():
    criterion = MileageCriterion()

    result = criterion.evaluate(
        make_search(max_mileage=None),
        make_listing(mileage=110_000),
    )

    assert result.points == criterion.MAX_POINTS


def test_mileage_within_limit_returns_max_points():
    criterion = MileageCriterion()

    result = criterion.evaluate(
        make_search(max_mileage=120_000),
        make_listing(mileage=115_000),
    )

    assert result.points == criterion.MAX_POINTS


def test_mileage_within_tolerance_returns_max_points():
    criterion = MileageCriterion()

    result = criterion.evaluate(
        make_search(max_mileage=120_000),
        make_listing(mileage=125_000),  # +4.17 %
    )

    assert result.points == criterion.MAX_POINTS


def test_mileage_above_tolerance_is_penalized():
    criterion = MileageCriterion()

    result = criterion.evaluate(
        make_search(max_mileage=120_000),
        make_listing(mileage=132_000),  # +10 %
    )

    assert 0 < result.points < criterion.MAX_POINTS


def test_mileage_above_thirty_percent_returns_zero():
    criterion = MileageCriterion()

    result = criterion.evaluate(
        make_search(max_mileage=120_000),
        make_listing(mileage=160_000),  # +33 %
    )

    assert result.points == 0


def test_mileage_exactly_at_tolerance_returns_max_points():
    criterion = MileageCriterion()

    result = criterion.evaluate(
        make_search(max_mileage=120_000),
        make_listing(mileage=126_000),  # +5 %
    )

    assert result.points == criterion.MAX_POINTS


def test_mileage_exactly_at_max_over_limit_returns_zero():
    criterion = MileageCriterion()

    result = criterion.evaluate(
        make_search(max_mileage=120_000),
        make_listing(mileage=156_000),  # +30 %
    )

    assert result.points == 0