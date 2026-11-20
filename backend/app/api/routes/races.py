from typing import Annotated

from fastapi import APIRouter, Depends, Query

from backend.app.api.dependencies import get_races_service
from backend.app.core.models import RepositoryQuery
from backend.app.models.queries import RacesQuery
from backend.app.services.races_service import RacesService


router=APIRouter(
    prefix='/races',
    tags=['Races'],
)


@router.get('/', summary='Получить список гонок')
def get_races(query: Annotated[RacesQuery, Query()], races_service:Annotated[RacesService, Depends(get_races_service)]):
    return races_service.get_races(query)

