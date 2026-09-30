from functools import lru_cache

from backend.app.core.config import get_settings
from backend.app.services.season_service import SeasonService


@lru_cache
def get_season_service() -> SeasonService:
    settings=get_settings()
    return SeasonService(settings)


