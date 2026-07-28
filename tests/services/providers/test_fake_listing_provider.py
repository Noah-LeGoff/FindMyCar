from services.providers.fake_listing_provider import FakeListingProvider

from tests.factories import make_listing, make_search


def test_returns_all_listings():
    listings = [
        make_listing(),
        make_listing(price=8000),
        make_listing(price=12000),
    ]

    provider = FakeListingProvider(
        listings,
    )

    result = provider.search(
        make_search(),
    )

    assert result == listings


def test_returns_empty_list():
    provider = FakeListingProvider([])

    result = provider.search(
        make_search(),
    )

    assert result == []


def test_returns_copy():
    listings = [
        make_listing(),
    ]

    provider = FakeListingProvider(
        listings,
    )

    result = provider.search(
        make_search(),
    )

    result.pop()

    assert len(provider.search(make_search())) == 1