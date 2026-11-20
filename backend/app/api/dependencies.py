from fastapi import Request

from backend.app.core.config import get_settings
from backend.app.services.races_service import RacesService
from backend.app.services.drivers_service import DriverService
from backend.app.services.laps_service import LapService


def get_races_service(request: Request) -> RacesService:
    return request.app.state.services.races_service


def get_drivers_service(request: Request) -> DriverService:
    return request.app.state.services.driver_service


def get_laps_service(request: Request) -> LapService:
    return request.app.state.services.laps_service
