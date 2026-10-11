import logging

from backend.app.integrations.contrant import F1Client
from backend.storage.contracts import BaseRepository
from backend.app.models.queries import DriversQuery
from backend.app.core.models import RepositoryQuery


logger=logging.getLogger(__name__)


class DriverService:
    def __init__(self, data_client:F1Client, repository: BaseRepository):
        self.data_client=data_client
        self.file_repository=repository

    def get_drivers(self, query: DriversQuery):
        logger.info('Getting drivers: session_key=%s', query.session_key)
        
        repository_query=RepositoryQuery(
            query_type='get_drivers',
            session_key=query.session_key,
        )

        cached_data=self.file_repository.get(repository_query)
        if cached_data is not None:
            logger.debug('Cache hit: session_key=%s', query.session_key)
            return cached_data

        logger.info('Cache miss: session_key=%s', query.session_key)
        data_loaded=self.data_client.get_drivers(query.session_key)
        self.file_repository.write(repository_query.get_id(), data_loaded)

        return data_loaded
    