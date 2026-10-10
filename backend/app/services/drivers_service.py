from backend.app.integrations.contrant import F1Client
from backend.storage.contracts import BaseRepository
from backend.app.models.queries import DriversQuery
from backend.app.core.models import RepositoryQuery



class DriverService:
    def __init__(self, data_client:F1Client, repository: BaseRepository):
        self.data_client=data_client
        self.file_repository=repository

    def get_drivers(self, query: DriversQuery):
        
        repository_query=RepositoryQuery(
            query_type='get_drivers',
            session_key=query.session_key,
        )

        cached_data=self.file_repository.get(repository_query)
        if cached_data is not None:
            return cached_data
        else:
            data_loaded=self.data_client.get_drivers(query.session_key)
            self.file_repository.write(repository_query.get_id(), data_loaded)

            return data_loaded
    