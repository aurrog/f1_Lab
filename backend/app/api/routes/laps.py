from typing import Annotated

from fastapi import APIRouter, Depends, Query

from backend.app.api.dependencies import get_laps_service
from backend.app.models.queries import LapsQuery
from backend.app.services.laps_service import LapService


router=APIRouter(
    prefix='/laps',
    tags=['Laps'],
)


@router.get('/', summary='Получить данные о кругах пилота')
def get_laps(query: Annotated[LapsQuery, Query()], laps_service: Annotated[LapService, Depends(get_laps_service)]):
    return laps_service.get_laps(query)

