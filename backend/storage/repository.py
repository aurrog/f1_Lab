from pathlib import Path
from backend.app.core.models import RepositoryQuery
from backend.app.db.connection import DataBase
import json

# def get_id(params):
#     normalized=[]


class Repository:
    def __init__(self, database: DataBase, dir_path: Path):
        self.dir_path=dir_path
        self.database=database


    # def get(self, query: RepositoryQuery)->int:

    def get(self, query: RepositoryQuery):
        query_id=query.get_id()

        cached_data_path = self.database.fetch_one('SELECT file_path FROM cached_responses WHERE id_generated = ?', (query_id,))
        if cached_data_path is not None:
            filename=f'{self.dir_path}/{query_id}.json'
            return self.get_from_storage(filename)


    def write(self, query_id:str, data:dict) -> None:

        filename=f'{self.dir_path}/{query_id}.json'
        with open(filename, 'w') as f:
            json.dump(data,f,indent=4)

        self.database.execute('''
            INSERT INTO cached_responses (id_generated, file_path)
            VALUES (?, ?)
        ''', (query_id, f'{query_id}.json'))


    def get_from_storage(self, file_path: Path) -> dict:

        with open(file_path, 'r') as f:
            return json.load(f)