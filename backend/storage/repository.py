import logging
from pathlib import Path
from backend.app.core.models import RepositoryQuery
from backend.app.db.connection import DataBase
import json

logger=logging.getLogger(__name__)



class Repository:
    def __init__(self, database: DataBase, dir_path: Path):
        self.dir_path=dir_path
        self.database=database

    # def get(self, query: RepositoryQuery)->int:

    def get(self, query: RepositoryQuery):
        cached=self.database.fetch_one(
            'SELECT file_path FROM cached_responses WHERE id_generated = ?', 
            (query.get_id(),),
        )

        if cached is None:
            return None

        file_path=self.dir_path / cached['file_path']
        try:
            return self.get_from_storage(file_path)
        except (FileNotFoundError, json.JSONDecodeError):
            logger.warning("Непригодный кеш: %s", file_path, exc_info=True)
            return None


    def write(self, query_id:str, data:dict) -> None:

        filename=f'{self.dir_path}/{query_id}.json'
        with open(filename, 'w') as f:
            json.dump(data,f,indent=4)

        self.database.execute('''
            INSERT INTO cached_responses (id_generated, file_path)
            VALUES (?, ?)
            ON CONFLICT(id_generated)
            DO UPDATE SET file_path= excluded.file_path
        ''', (query_id, f'{query_id}.json'))


    def get_from_storage(self, file_path: Path) -> dict:
        with open(file_path, 'r') as f:
            return json.load(f)
        