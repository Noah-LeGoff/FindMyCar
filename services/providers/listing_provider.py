from abc import ABC, abstractmethod

from models.listing import Listing
from models.search import Search


class ListingProvider(ABC):
    """
    Contract for all listing providers.

    A listing provider retrieves listings matching a user search
    from a specific marketplace.
    """

    @abstractmethod
    def search(
        self,
        search: Search,
    ) -> list[Listing]:
        """
        Retrieves listings matching the given search.

        Args:
            search: User search criteria.

        Returns:
            A list of normalized listings.
        """
        raise NotImplementedError