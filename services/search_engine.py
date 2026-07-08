from models.listing import Listing
from models.search import Search
from providers.provider_manager import ProviderManager
from services.matching_service import MatchingService



class SearchEngine:
    """
    Orchestre une recherche de véhicules.
    """

    def __init__(
        self,
        provider_manager: ProviderManager,
        matching_service: MatchingService
    ):
        self._provider_manager = provider_manager
        self._matching_service = matching_service

    def search(self, search: Search) -> list[Listing]:
        """
        Exécute une recherche complète.
        """

        listings = self._provider_manager.search(search)

        listings = self._remove_duplicates(listings)

        listings = [
            listing
            for listing in listings
            if self._matching_service.matches(search, listing)
        ]

        listings = self._post_process(listings)

        return listings

    def _remove_duplicates(
        self,
        listings: list[Listing]
    ) -> list[Listing]:
        """
        Supprime les annonces en double.
        """

        unique: dict[str, Listing] = {}

        for listing in listings:
            unique[listing.url] = listing

        return list(unique.values())
    
    def _post_process(self, listings: list[Listing]) -> list[Listing]:
        """
        Applique les traitements finaux aux annonces.
        """
        return listings