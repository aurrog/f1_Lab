from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    database_url: str = ''
    openf1_api_url: str = 'https://api.openf1.org/v1'
    timeout_seconds: int = 20

    class Config:
        env_file = '.env'



@lru_cache
def get_settings() -> Settings:
    return Settings()