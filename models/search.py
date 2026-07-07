from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from models.enums import FuelType, GearboxType


@dataclass(slots=True)
class Search:

    id: Optional[int]

    user_id: int

    brand: Optional[str] = None
    model: Optional[str] = None
    version: Optional[str] = None

    min_price: Optional[int] = None
    max_price: Optional[int] = None

    min_year: Optional[int] = None
    max_year: Optional[int] = None

    max_mileage: Optional[int] = None

    fuel: Optional[FuelType] = None

    gearbox: Optional[GearboxType] = None

    doors: Optional[int] = None

    latitude: Optional[float] = None
    longitude: Optional[float] = None

    radius_km: Optional[int] = None

    include_keywords: tuple[str, ...] = ()

    exclude_keywords: tuple[str, ...] = ()

    created_at: Optional[datetime] = None