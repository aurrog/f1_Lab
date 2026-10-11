from pydantic_settings import BaseSettings
# from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


PROJECT_ROOT=Path(__file__).resolve().parents[3]

class Settings(BaseSettings):
    database_url: Path = PROJECT_ROOT / 'data/base.db'
    openf1_api_url: str = 'https://api.openf1.org/v1'
    timeout_seconds: int = 20
    cache_data_dir: Path = Path('data/openf1')

    # class Config:
    #     env_file = '.env'



@lru_cache
def get_settings() -> Settings:
    return Settings()