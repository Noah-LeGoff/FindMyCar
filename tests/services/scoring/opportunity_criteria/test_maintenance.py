from services.scoring.opportunity_criteria.maintenance import (
    MaintenanceCriterion,
)

from tests.factories import (
    make_listing,
    make_market,
    make_search,
)


def test_returns_zero_when_description_is_missing():
    criterion = MaintenanceCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(description=None),
        make_market(),
    )

    assert result.points == 0


def test_returns_zero_when_description_is_empty():
    criterion = MaintenanceCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(description=""),
        make_market(),
    )

    assert result.points == 0


def test_returns_zero_when_no_keyword_is_found():
    criterion = MaintenanceCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(
            description="Vehicle in good overall condition.",
        ),
        make_market(),
    )

    assert result.points == 0


def test_detects_distribution_keyword():
    criterion = MaintenanceCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(
            description="Distribution replaced recently.",
        ),
        make_market(),
    )

    assert result.points == 8


def test_detects_distribution_synonym():
    criterion = MaintenanceCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(
            description="Timing belt replaced.",
        ),
        make_market(),
    )

    assert result.points == 8


def test_detects_multiple_maintenance_items():
    criterion = MaintenanceCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(
            description=(
                "Distribution replaced. "
                "Recent oil change. "
                "Maintenance invoices available."
            ),
        ),
        make_market(),
    )

    assert result.points == 13


def test_does_not_count_same_item_twice():
    criterion = MaintenanceCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(
            description=(
                "Distribution replaced. "
                "Timing belt replaced."
            ),
        ),
        make_market(),
    )

    assert result.points == 8


def test_score_is_capped():
    criterion = MaintenanceCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(
            description=(
                "Distribution. "
                "Clutch. "
                "Oil change. "
                "Service. "
                "Invoices. "
                "Service book. "
                "Technical inspection. "
                "New brakes. "
                "New tires."
            ),
        ),
        make_market(),
    )

    assert result.points == criterion.MAX_POINTS


def test_keyword_search_is_case_insensitive():
    criterion = MaintenanceCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(
            description="DISTRIBUTION REPLACED.",
        ),
        make_market(),
    )

    assert result.points == 8


def test_returns_reason_with_detected_items():
    criterion = MaintenanceCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(
            description="Distribution replaced.",
        ),
        make_market(),
    )

    assert result.reason == "Timing belt replaced."