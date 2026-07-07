from models.search import Search
from providers.demo_provider import DemoProvider
from providers.provider_manager import ProviderManager


manager = ProviderManager()

manager.register(DemoProvider())

search = Search(
    id=None,
    user_id=1,
    brand="BMW",
    model="E36",
)

results = manager.search(search)

for listing in results:
    print(listing.title, listing.price)