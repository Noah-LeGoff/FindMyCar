from services.scoring.criteria.fuel import FuelCriterion

from models.enums import FuelType

from tests.factories import make_listing, make_search


def test_missing_search_fuel_returns_max_points():
    criterion = FuelCriterion()

    result = criterion.evaluate(
        make_search(fuel=None),
        make_listing(fuel=FuelType.GASOLINE),
    )

    assert result.points == criterion.MAX_POINTS


def test_missing_listing_fuel_returns_zero():
    criterion = FuelCriterion()

    result = criterion.evaluate(
        make_search(fuel=FuelType.GASOLINE),
        make_listing(fuel=None),
    )

    assert result.points == 0


def test_matching_fuel_returns_max_points():
    criterion = FuelCriterion()

    result = criterion.evaluate(
        make_search(fuel=FuelType.GASOLINE),
        make_listing(fuel=FuelType.GASOLINE),
    )

    assert result.points == criterion.MAX_POINTS


def test_different_fuel_returns_zero():
    criterion = FuelCriterion()

    result = criterion.evaluate(
        make_search(fuel=FuelType.GASOLINE),
        make_listing(fuel=FuelType.DIESEL),
    )

    assert result.points == 0