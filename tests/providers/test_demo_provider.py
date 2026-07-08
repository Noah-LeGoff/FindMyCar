from models.search import Search
from models.listing import Listing
from providers.demo_provider import DemoProvider


def test_demo_provider_returns_listings():
    """
    DemoProvider should return listings.
    """

    provider = DemoProvider()

    search = Search(
        id=None,
        user_id=1
    )

    results = provider.search(search)

    assert isinstance(results, list)

    assert len(results) > 0


def test_demo_provider_returns_listing_objects():
    """
    DemoProvider should return Listing instances.
    """

    provider = DemoProvider()

    search = Search(
        id=None,
        user_id=1
    )

    results = provider.search(search)

    for listing in results:
        assert isinstance(listing, Listing)


def test_demo_provider_respects_brand_filter():
    """
    DemoProvider should filter by brand.
    """

    provider = DemoProvider()

    search = Search(
        id=None,
        user_id=1,
        brand="BMW"
    )

    results = provider.search(search)

    for listing in results:
        assert listing.brand == "BMW"