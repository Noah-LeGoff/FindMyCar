from models.search import Search
from models.listing import Listing
from providers.provider_manager import ProviderManager


class FakeProvider:
    """
    Fake provider used for testing.
    """

    def __init__(self, listings):
        self.listings = listings

    def search(self, search):
        return self.listings


def create_listing(title):
    """
    Creates a simple listing.
    """

    return Listing(
        source="test",
        title=title,
        brand="BMW",
        model="E36",
        price=8000,
        url=title
    )


def test_provider_manager_returns_provider_results():
    """
    ProviderManager should return listings from providers.
    """

    provider = FakeProvider(
        [
            create_listing("car1"),
            create_listing("car2")
        ]
    )

    manager = ProviderManager()

    manager.register(provider)

    search = Search(
        id=None,
        user_id=1
    )

    results = manager.search(search)

    assert len(results) == 2


def test_provider_manager_supports_multiple_providers():
    """
    ProviderManager should aggregate multiple providers.
    """

    provider_one = FakeProvider(
        [
            create_listing("car1")
        ]
    )

    provider_two = FakeProvider(
        [
            create_listing("car2")
        ]
    )

    manager = ProviderManager()

    manager.register(provider_one)
    manager.register(provider_two)

    search = Search(
        id=None,
        user_id=1
    )

    results = manager.search(search)

    assert len(results) == 2