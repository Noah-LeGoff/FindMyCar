from datetime import date, datetime, timedelta

from services.scoring.opportunity_criteria.freshness import FreshnessCriterion

from tests.factories import make_listing, make_search


TODAY = date(2026, 7, 15)


def test_missing_publication_date_returns_zero():
    criterion = FreshnessCriterion(today=TODAY)

    result = criterion.evaluate(
        make_search(),
        make_listing(published_at=None),
    )

    assert result.points == 0


def test_listing_published_today_returns_max_points():
    criterion = FreshnessCriterion(today=TODAY)

    result = criterion.evaluate(
        make_search(),
        make_listing(
            published_at=datetime.combine(
                TODAY,
                datetime.min.time(),
            )
        ),
    )

    assert result.points == criterion.MAX_POINTS


def test_old_listing_returns_zero():
    criterion = FreshnessCriterion(today=TODAY)

    result = criterion.evaluate(
        make_search(),
        make_listing(
            published_at=datetime.combine(
                TODAY - timedelta(days=90),
                datetime.min.time(),
            )
        ),
    )

    assert result.points == 0


def test_recent_listing_returns_partial_points():
    criterion = FreshnessCriterion(today=TODAY)

    result = criterion.evaluate(
        make_search(),
        make_listing(
            published_at=datetime.combine(
                TODAY - timedelta(days=30),
                datetime.min.time(),
            )
        ),
    )

    assert 0 < result.points < criterion.MAX_POINTS