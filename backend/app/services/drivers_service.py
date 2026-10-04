from backend.app.integrations.contrant import F1Client
from backend.storage.contracts import BaseRepository
from backend.app.core.models import RepositoryQuery



class DriverService:
    def __init__(self, data_client:F1Client, repository: BaseRepository):
        self.data_client=data_client

    def get_drivers(self, query: RepositoryQuery):
        # TODO in-cache condition and in-prefilled condition
        
        return self.data_client.get_drivers(query.session_key)
    