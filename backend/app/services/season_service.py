from backend.app.core.models import RepositoryQuery
from backend.app.integrations.contrant import F1Client
from backend.storage.contracts import BaseRepository



class SeasonService():
    def __init__(self, data_client: F1Client, repository: BaseRepository):
        self.data_client=data_client
        self.file_repository=repository


    def get_races(self, query: RepositoryQuery):
        # TODO: in-cache condition
        # repository.make_id(params)

        cached_data = self.file_repository.get(query)

        if cached_data is not None:
            print('FROM_CACHe')
            return cached_data

        else: 
            data_loaded=self.data_client.get_races(query.year)

            self.file_repository.write(query.get_id(), data_loaded)

            return self.data_client.get_races(query.year)
