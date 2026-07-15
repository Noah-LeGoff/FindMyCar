from services.scoring.criteria.year import YearCriterion

from tests.factories import make_listing, make_search


def test_missing_year_returns_zero():
    criterion = YearCriterion()

    result = criterion.evaluate(
        make_search(min_year=2018),
        make_listing(year=None),
    )

    assert result.points == 0


def test_missing_search_year_returns_max_points():
    criterion = YearCriterion()

    result = criterion.evaluate(
        make_search(min_year=None),
        make_listing(year=2018),
    )

    assert result.points == criterion.MAX_POINTS


def test_newer_vehicle_returns_max_points():
    criterion = YearCriterion()

    result = criterion.evaluate(
        make_search(min_year=2018),
        make_listing(year=2020),
    )

    assert result.points == criterion.MAX_POINTS


def test_same_year_returns_max_points():
    criterion = YearCriterion()

    result = criterion.evaluate(
        make_search(min_year=2018),
        make_listing(year=2018),
    )

    assert result.points == criterion.MAX_POINTS


def test_year_within_tolerance_returns_max_points():
    criterion = YearCriterion()

    result = criterion.evaluate(
        make_search(min_year=2018),
        make_listing(year=2017),
    )

    assert result.points == criterion.MAX_POINTS


def test_year_slightly_too_old_returns_partial_points():
    criterion = YearCriterion()

    result = criterion.evaluate(
        make_search(min_year=2018),
        make_listing(year=2016),
    )

    assert 0 < result.points < criterion.MAX_POINTS


def test_year_too_old_returns_zero():
    criterion = YearCriterion()

    result = criterion.evaluate(
        make_search(min_year=2018),
        make_listing(year=2013),
    )

    assert result.points == 0