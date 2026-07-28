import requests

from core.exceptions import ProviderError

from models.listing import Listing
from models.search import Search

from services.providers.listing_provider import ListingProvider


class LeboncoinProvider(ListingProvider):
    """
    Listing provider for Leboncoin.
    """
    
    REQUEST_TIMEOUT = 10

    def search(
        self,
        search: Search,
    ) -> list[Listing]:
        """
        Retrieves listings from Leboncoin.

        The implementation is intentionally incremental.
        """

        raise NotImplementedError

    def _build_payload(
        self,
        search: Search,
    ) -> dict:
        """
        Builds the payload sent to the Leboncoin API.

        The implementation is intentionally incremental.
        """

        payload = {}

        if search.brand is not None:
            payload["brand"] = search.brand

        if search.model is not None:
            payload["model"] = search.model

        if search.min_price is not None:
            payload["min_price"] = search.min_price

        if search.max_price is not None:
            payload["max_price"] = search.max_price

        if search.min_year is not None:
            payload["min_year"] = search.min_year

        if search.max_year is not None:
            payload["max_year"] = search.max_year

        if search.max_mileage is not None:
            payload["max_mileage"] = search.max_mileage

        return payload

    def _fetch_results(
        self,
        url: str,
        payload: dict,
        headers: dict | None = None,
    ) -> dict:
        """
        Sends a request to the marketplace API.
        """

        try:
            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=self.REQUEST_TIMEOUT,
            )

            response.raise_for_status()

            return response.json()

        except requests.RequestException as exc:
            raise ProviderError(
                "Unable to retrieve listings from Leboncoin."
            ) from exc