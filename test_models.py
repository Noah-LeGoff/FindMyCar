from models.user import User
from models.search import Search
from models.listing import Listing

from models.enums import FuelType, GearboxType


user = User(
    id=None,
    telegram_id=123456,
    username="Noah",
    first_name="Noah"
)

search = Search(
    id=None,
    user_id=1,
    brand="BMW",
    model="E36",
    max_price=8000,
    fuel=FuelType.GASOLINE,
    gearbox=GearboxType.MANUAL,
    radius_km=100,
)

listing = Listing(
    source="demo",
    title="BMW E36 325i",
    brand="BMW",
    model="E36",
    year=1995,
    price=7000,
    mileage=180000,
    location="Rennes",
    url="https://demo.fr",
    description="Très bon état"
)

print(user)
print(search)
print(listing)