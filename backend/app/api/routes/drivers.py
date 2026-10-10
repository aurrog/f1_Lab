from typing import Annotated

from fastapi import APIRouter, Depends, Query

from backend.app.api.dependencies import get_drivers_service
from backend.app.services.drivers_service import DriverService
from backend.app.models.queries import DriversQuery


router=APIRouter(
    prefix='/drivers',
    tags=['Drivers']
)


@router.get('/', summary='Получить список пилотов')
def get_drivers(query:Annotated[DriversQuery, Query()], drivers_service: Annotated[DriverService, Depends(get_drivers_service)]):

    return drivers_service.get_drivers(query)
