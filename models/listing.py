from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from models.enums import FuelType, GearboxType


@dataclass(slots=True)
class Listing:
    source: str

    title: str

    brand: str
    model: str
    version: Optional[str] = None

    year: Optional[int] = None

    price: int = 0
    currency: str = "EUR"

    mileage: Optional[int] = None

    fuel: Optional[FuelType] = None
    gearbox: Optional[GearboxType] = None

    doors: Optional[int] = None

    location: str = ""

    latitude: Optional[float] = None
    longitude: Optional[float] = None

    url: str = ""
    image_url: Optional[str] = None

    description: str = ""

    published_at: datetime | None = None

    score: int = 0