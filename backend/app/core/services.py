from dataclasses import dataclass

from backend.app.services.season_service import SeasonService
from backend.app.services.drivers_service import DriverService

from backend.app.integrations.openf1.client import OpenF1Client
from backend.app.db.connection import DataBase
from backend.app.db.connection import SQLite3DataBase
from backend.storage.repository import Repository

from backend.app.core.config import Settings


def init_schema(database: DataBase):
    # database.connect()

    database.execute('''
        CREATE TABLE IF NOT EXISTS cached_responses (
            id_generated VARCHAR(64) PRIMARY KEY,
            file_path VARCHAR(512) NOT NULL
        );
    
    ''')
    


@dataclass(frozen=True)
class Services:
    season_service: SeasonService
    driver_service: DriverService


def build_services(settings: Settings) -> Services:
    database=SQLite3DataBase(settings.database_url)
    init_schema(database)

    data_client=OpenF1Client(settings.openf1_api_url, settings.timeout_seconds)
    repository=Repository(database, settings.cache_data_dir)

    return Services(
        season_service=SeasonService(data_client, repository),
        driver_service=DriverService(data_client, repository),
    )

