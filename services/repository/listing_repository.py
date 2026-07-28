from models.listing import Listing
from models.search import Search

from services.providers.listing_provider import ListingProvider


class ListingRepository:
    """
    Retrieves listings using a configured ListingProvider.
    """

    def __init__(
        self,
        provider: ListingProvider,
    ):
        self._provider = provider

    def search(
        self,
        search: Search,
    ) -> list[Listing]:
        """
        Retrieves listings matching the given search.
        """

        return self._provider.search(search)