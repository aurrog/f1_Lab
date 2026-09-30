from functools import lru_cache

from backend.app.core.config import get_settings
from backend.app.services.season_service import SeasonService
from backend.app.services.drivers_service import DriverService


@lru_cache
def get_season_service() -> SeasonService:
    settings=get_settings()
    return SeasonService(settings)


@lru_cache
def get_drivers_service() -> DriverService:
    settings=get_settings()
    return DriverService(settings)


