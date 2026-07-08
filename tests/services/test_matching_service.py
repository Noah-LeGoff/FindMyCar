from models.search import Search
from models.listing import Listing
from services.matching_service import MatchingService


def create_listing(**kwargs):
    """
    Creates a default listing for tests.
    """

    default = {
        "source": "test",
        "title": "BMW E36",
        "brand": "BMW",
        "model": "E36",
        "version": "325i",
        "year": 1995,
        "price": 8000,
        "mileage": 150000,
    }

    default.update(kwargs)

    return Listing(**default)


def test_empty_search_matches_everything():
    """
    A search without filters should match any listing.
    """

    search = Search(
        id=None,
        user_id=1
    )

    listing = create_listing()

    service = MatchingService()

    assert service.matches(search, listing)


def test_matching_brand():
    """
    Same brand should match.
    """

    search = Search(
        id=None,
        user_id=1,
        brand="BMW"
    )

    listing = create_listing(
        brand="BMW"
    )

    service = MatchingService()

    assert service.matches(search, listing)


def test_wrong_brand_does_not_match():
    """
    Different brand should not match.
    """

    search = Search(
        id=None,
        user_id=1,
        brand="Audi"
    )

    listing = create_listing(
        brand="BMW"
    )

    service = MatchingService()

    assert not service.matches(search, listing)


def test_price_range():
    """
    Price outside range should fail.
    """

    search = Search(
        id=None,
        user_id=1,
        max_price=5000
    )

    listing = create_listing(
        price=8000
    )

    service = MatchingService()

    assert not service.matches(search, listing)


def test_year_range():
    """
    Year outside range should fail.
    """

    search = Search(
        id=None,
        user_id=1,
        min_year=2000
    )

    listing = create_listing(
        year=1995
    )

    service = MatchingService()

    assert not service.matches(search, listing)