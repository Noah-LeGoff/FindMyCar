from models.listing import Listing
from models.search import Search
from providers.base_provider import BaseProvider


class DemoProvider(BaseProvider):
    """
    Provider de démonstration utilisé pendant le développement.
    """

    def search(self, search: Search) -> list[Listing]:

        return [

            Listing(
                source="demo",
                title="BMW E36 325i",
                brand="BMW",
                model="E36",
                version="325i",
                year=1995,
                price=7000,
                mileage=185000,
                location="Rennes",
                url="https://demo.fr/1",
                description="Carnet d'entretien complet."
            ),

            Listing(
                source="demo",
                title="BMW E36 320i",
                brand="BMW",
                model="E36",
                version="320i",
                year=1994,
                price=9500,
                mileage=240000,
                location="Brest",
                url="https://demo.fr/2",
                description="Quelques travaux à prévoir."
            )
        ]