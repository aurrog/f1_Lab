import logging

from backend.app.models.queries import RacesQuery
from backend.app.core.models import RepositoryQuery
from backend.app.integrations.contrant import F1Client
from backend.storage.contracts import BaseRepository


logger=logging.getLogger(__name__)


class SeasonService():
    def __init__(self, data_client: F1Client, repository: BaseRepository):
        self.data_client=data_client
        self.file_repository=repository


    def get_races(self, query: RacesQuery):
        logger.info('Getting races: year=%s', query.year)

        repository_query=RepositoryQuery(
            query_type='get_races',
            year=query.year
        )

        cached_data = self.file_repository.get(repository_query)
        if cached_data is not None:
            logger.debug('Cache hit: year=%s', query.year)
            return cached_data

        logger.info('Cache miss: year=%s', query.year)
        data_loaded=self.data_client.get_races(query.year)
        self.file_repository.write(repository_query.get_id(), data_loaded)

        return data_loaded
