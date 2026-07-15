import pytest

from services.scoring.opportunity_criteria.price_opportunity import (
    PriceOpportunityCriterion,
)

from tests.factories import (
    make_listing,
    make_market,
    make_search,
)


def test_returns_zero_when_market_is_empty():
    criterion = PriceOpportunityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(price=9000),
        make_market(),
    )

    assert result.points == 0


def test_returns_zero_when_sample_size_is_too_small():
    criterion = PriceOpportunityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(price=9000),
        make_market(
            9000,
            9100,
            9200,
        ),
    )

    assert result.points == 0


def test_returns_zero_when_price_is_above_market():
    criterion = PriceOpportunityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(price=11000),
        make_market(
            9000,
            9100,
            9200,
            9300,
            9400,
            9500,
            9600,
            9700,
            9800,
            9900,
        ),
    )

    assert result.points == 0


def test_returns_half_points_when_listing_is_ten_percent_below_market():
    criterion = PriceOpportunityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(price=9000),
        make_market(
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
        ),
    )

    assert result.points == pytest.approx(
        criterion.MAX_POINTS / 2
    )


def test_returns_max_points_when_listing_is_twenty_percent_below_market():
    criterion = PriceOpportunityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(price=8000),
        make_market(
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
        ),
    )

    assert result.points == criterion.MAX_POINTS


def test_score_is_capped_above_twenty_percent_difference():
    criterion = PriceOpportunityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(price=6000),
        make_market(
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
        ),
    )

    assert result.points == criterion.MAX_POINTS


def test_invalid_market_prices_are_ignored():
    criterion = PriceOpportunityCriterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(price=9000),
        make_market(
            1,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
        ),
    )

    assert result.points == pytest.approx(
        criterion.MAX_POINTS / 2
    )