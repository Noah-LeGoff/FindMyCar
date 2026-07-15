from models.enums import GearboxType

from services.scoring.criteria.gearbox import GearboxCriterion

from tests.factories import make_listing, make_search


def test_missing_search_gearbox_returns_max_points():
    criterion = GearboxCriterion()

    result = criterion.evaluate(
        make_search(gearbox=None),
        make_listing(gearbox=GearboxType.MANUAL),
    )

    assert result.points == criterion.MAX_POINTS


def test_missing_listing_gearbox_returns_zero():
    criterion = GearboxCriterion()

    result = criterion.evaluate(
        make_search(gearbox=GearboxType.MANUAL),
        make_listing(gearbox=None),
    )

    assert result.points == 0


def test_matching_gearbox_returns_max_points():
    criterion = GearboxCriterion()

    result = criterion.evaluate(
        make_search(gearbox=GearboxType.MANUAL),
        make_listing(gearbox=GearboxType.MANUAL),
    )

    assert result.points == criterion.MAX_POINTS


def test_different_gearbox_returns_zero():
    criterion = GearboxCriterion()

    result = criterion.evaluate(
        make_search(gearbox=GearboxType.MANUAL),
        make_listing(gearbox=GearboxType.AUTOMATIC),
    )

    assert result.points == 0