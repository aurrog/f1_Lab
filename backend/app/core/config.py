from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    database_url: str = 'base.db'
    openf1_api_url: str = 'https://api.openf1.org/v1'
    timeout_seconds: int = 20
    cache_data_dir: str = 'data/openf1'

    class Config:
        env_file = '.env'



@lru_cache
def get_settings() -> Settings:
    return Settings()