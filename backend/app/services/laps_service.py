import logging

from backend.app.core.models import RepositoryQuery
from backend.app.integrations.contrant import F1Client
from backend.app.models.queries import LapsQuery
from backend.storage.contracts import BaseRepository


logger=logging.getLogger(__name__)


class LapService:
    def __init__(self, data_client: F1Client, repository: BaseRepository):
        self.data_client=data_client
        self.file_repository=repository

    def get_laps(self, query: LapsQuery):
        logger.info('Getting laps: session_key=%s driver_number=%s', query.session_key, query.driver_number)

        repository_query=RepositoryQuery(
            query_type='get_laps',
            session_key=query.session_key,
            driver_number=query.driver_number,
        )

        cached_data=self.file_repository.get(repository_query)
        if cached_data is not None:
            logger.debug('Cache hit: session_key=%s driver_number=%s', query.session_key, query.driver_number)
            return cached_data

        logger.info('Cache miss: session_key=%s driver_number=%s', query.session_key, query.driver_number)
        data_loaded=self.data_client.get_laps(query.session_key, query.driver_number)
        self.file_repository.write(repository_query.get_id(), data_loaded)

        return data_loaded
