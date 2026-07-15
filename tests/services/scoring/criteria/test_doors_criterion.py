from services.scoring.criteria.doors import DoorsCriterion

from models.enums import FuelType

from tests.factories import make_listing, make_search


def test_missing_search_doors_returns_max_points():
    criterion = DoorsCriterion()

    result = criterion.evaluate(
        make_search(doors=None),
        make_listing(doors=4),
    )

    assert result.points == criterion.MAX_POINTS


def test_missing_listing_doors_returns_zero():
    criterion = DoorsCriterion()

    result = criterion.evaluate(
        make_search(doors=4),
        make_listing(doors=None),
    )

    assert result.points == 0


def test_matching_doors_returns_max_points():
    criterion = DoorsCriterion()

    result = criterion.evaluate(
        make_search(doors=4),
        make_listing(doors=4),
    )

    assert result.points == criterion.MAX_POINTS


def test_different_doors_returns_zero():
    criterion = DoorsCriterion()

    result = criterion.evaluate(
        make_search(doors=4),
        make_listing(doors=2),
    )

    assert result.points == 0