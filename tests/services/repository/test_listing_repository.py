from services.providers.fake_listing_provider import FakeListingProvider
from services.repository.listing_repository import ListingRepository

from tests.factories import make_listing, make_search


def test_returns_provider_results():
    listings = [
        make_listing(),
        make_listing(price=8_000),
        make_listing(price=12_000),
    ]

    provider = FakeListingProvider(
        listings,
    )

    repository = ListingRepository(
        provider,
    )

    result = repository.search(
        make_search(),
    )

    assert result == listings


def test_returns_empty_list():
    provider = FakeListingProvider([])

    repository = ListingRepository(
        provider,
    )

    result = repository.search(
        make_search(),
    )

    assert result == []


def test_provider_is_not_modified():
    listings = [
        make_listing(),
    ]

    provider = FakeListingProvider(
        listings,
    )

    repository = ListingRepository(
        provider,
    )

    result = repository.search(
        make_search(),
    )

    result.pop()

    assert len(
        repository.search(
            make_search(),
        )
    ) == 1