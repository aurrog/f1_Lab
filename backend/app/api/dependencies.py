from fastapi import Request

from backend.app.core.config import get_settings
from backend.app.services.season_service import SeasonService
from backend.app.services.drivers_service import DriverService


def get_season_service(request: Request) -> SeasonService:
    return request.app.state.services.season_service


def get_drivers_service(request: Request) -> DriverService:
    return request.app.state.services.driver_service


