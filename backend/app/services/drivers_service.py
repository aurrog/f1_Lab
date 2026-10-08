from backend.app.integrations.contrant import F1Client
from backend.storage.contracts import BaseRepository
from backend.app.core.models import RepositoryQuery



class DriverService:
    def __init__(self, data_client:F1Client, repository: BaseRepository):
        self.data_client=data_client
        self.file_repository=repository

    def get_drivers(self, query: RepositoryQuery):
        # TODO in-cache condition and in-prefilled condition

        cached_data=self.file_repository.get(query)
        if cached_data is not None:
            print('FROM_CACHe')
            return cached_data
        else:
            data_loaded=self.data_client.get_drivers(query.session_key)
            self.file_repository.write(query.get_id(), data_loaded)

            return data_loaded
    