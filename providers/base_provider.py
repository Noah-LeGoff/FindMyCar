from abc import ABC, abstractmethod

from models.search import Search
from models.listing import Listing


class BaseProvider(ABC):
    """
    Interface que tous les providers doivent implémenter.
    """

    @abstractmethod
    def search(self, search: Search) -> list[Listing]:
        """
        Recherche des annonces correspondant aux critères.
        """
        raise NotImplementedError