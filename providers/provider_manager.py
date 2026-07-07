from models.listing import Listing
from models.search import Search
from providers.base_provider import BaseProvider


class ProviderManager:
    """
    Coordonne l'ensemble des providers enregistrés.
    """

    def __init__(self):

        self._providers: list[BaseProvider] = []

    def register(self, provider: BaseProvider):

        self._providers.append(provider)

    def search(self, search: Search) -> list[Listing]:

        listings: list[Listing] = []

        for provider in self._providers:

            listings.extend(
                provider.search(search)
            )

        return listings