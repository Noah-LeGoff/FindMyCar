from models.listing import Listing
from models.search import Search

from services.providers.listing_provider import ListingProvider


class FakeListingProvider(ListingProvider):
    """
    Fake implementation of ListingProvider used for testing.
    """

    def __init__(
        self,
        listings: list[Listing],
    ):
        self._listings = listings

    def search(
        self,
        search: Search,
    ) -> list[Listing]:
        """
        Returns the predefined listings.
        """

        return list(self._listings)