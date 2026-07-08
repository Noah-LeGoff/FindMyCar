from models.search import Search
from models.listing import Listing
from services.search_engine import SearchEngine
from services.matching_service import MatchingService


class FakeProviderManager:
    """
    Fake provider manager used for tests.
    """

    def __init__(self, listings):
        self.listings = listings

    def search(self, search):
        return self.listings


def create_listing(**kwargs):
    """
    Creates a default listing.
    """

    default = {
        "source": "test",
        "title": "BMW E36",
        "brand": "BMW",
        "model": "E36",
        "year": 1995,
        "price": 8000,
        "mileage": 150000,
        "url": "https://test.com/1",
    }

    default.update(kwargs)

    return Listing(**default)


def create_engine(listings):
    """
    Creates a SearchEngine for tests.
    """

    provider_manager = FakeProviderManager(listings)

    return SearchEngine(
        provider_manager,
        MatchingService()
    )


def test_search_engine_returns_matching_listings():
    """
    SearchEngine should return matching listings.
    """

    listings = [
        create_listing(
            brand="BMW"
        ),
        create_listing(
            brand="Audi",
            url="https://test.com/2"
        )
    ]

    engine = create_engine(listings)

    search = Search(
        id=None,
        user_id=1,
        brand="BMW"
    )

    results = engine.search(search)

    assert len(results) == 1
    assert results[0].brand == "BMW"


def test_search_engine_removes_duplicates():
    """
    SearchEngine should remove duplicate listings.
    """

    listings = [
        create_listing(
            url="same-url"
        ),
        create_listing(
            url="same-url"
        )
    ]

    engine = create_engine(listings)

    search = Search(
        id=None,
        user_id=1
    )

    results = engine.search(search)

    assert len(results) == 1