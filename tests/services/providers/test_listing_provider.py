import pytest

from services.providers.listing_provider import ListingProvider


def test_listing_provider_is_abstract():
    with pytest.raises(TypeError):
        ListingProvider()