from models.search import Search
from models.listing import Listing


class MatchingService:
    """
    Determines whether a listing matches a user's search criteria.
    """

    def matches(self, search: Search, listing: Listing) -> bool:
        """
        Returns True if the listing matches all search criteria.
        """

        checks = (
            self._match_brand,
            self._match_model,
            self._match_version,
            self._match_price,
            self._match_mileage,
            self._match_year,
            self._match_fuel,
            self._match_gearbox,
            self._match_doors,
            self._match_location,
        )

        return all(check(search, listing) for check in checks)

    def _normalize(self, value: str | None) -> str | None:
        """
        Normalizes a string for comparison.
        """

        if value is None:
            return None

        return value.strip().lower()

    def _match_brand(self, search: Search, listing: Listing) -> bool:
        """
        Checks the vehicle brand.
        """

        if search.brand is None:
            return True

        return self._normalize(search.brand) == self._normalize(listing.brand)

    def _match_model(self, search: Search, listing: Listing) -> bool:
        """
        Checks the vehicle model.
        """

        if search.model is None:
            return True

        return self._normalize(search.model) == self._normalize(listing.model)

    def _match_version(self, search: Search, listing: Listing) -> bool:
        """
        Checks the vehicle version.
        """

        if search.version is None:
            return True

        return self._normalize(search.version) == self._normalize(listing.version)

    def _match_price(self, search: Search, listing: Listing) -> bool:
        """
        Checks the vehicle price.
        """

        if search.min_price is not None:
            if listing.price < search.min_price:
                return False

        if search.max_price is not None:
            if listing.price > search.max_price:
                return False

        return True

    def _match_mileage(self, search: Search, listing: Listing) -> bool:
        """
        Checks vehicle mileage.
        """

        if search.max_mileage is None:
            return True

        if listing.mileage is None:
            return False

        return listing.mileage <= search.max_mileage

    def _match_year(self, search: Search, listing: Listing) -> bool:
        """
        Checks the vehicle year range.
        """

        if search.min_year is not None:
            if listing.year is None:
                return False

            if listing.year < search.min_year:
                return False

        if search.max_year is not None:
            if listing.year is None:
                return False

            if listing.year > search.max_year:
                return False

        return True

    def _match_fuel(self, search: Search, listing: Listing) -> bool:
        """
        Checks the vehicle fuel type.
        """

        if search.fuel is None:
            return True

        return search.fuel == listing.fuel

    def _match_gearbox(self, search: Search, listing: Listing) -> bool:
        """
        Checks the vehicle gearbox.
        """

        if search.gearbox is None:
            return True

        return search.gearbox == listing.gearbox

    def _match_doors(self, search: Search, listing: Listing) -> bool:
        """
        Checks the number of doors.
        """

        if search.doors is None:
            return True

        return search.doors == listing.doors

    def _match_location(self, search: Search, listing: Listing) -> bool:
        """
        Checks vehicle location.

        Radius calculation will be implemented later.
        """

        if (
            search.latitude is None
            or search.longitude is None
            or search.radius_km is None
        ):
            return True

        if (
            listing.latitude is None
            or listing.longitude is None
        ):
            return False

        # TODO:
        # Calculate distance between coordinates

        return True