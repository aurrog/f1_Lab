from typing import Annotated

from fastapi import APIRouter, Depends, Query

from backend.app.api.dependencies import get_season_service
from backend.app.core.models import RepositoryQuery
from backend.app.models.queries import RacesQuery
from backend.app.services.season_service import SeasonService


router=APIRouter(
    prefix='/races',
    tags=['Races'],
)


@router.get('/', summary='Получить список гонок')
def get_races(query: Annotated[RacesQuery, Query()], season_service:Annotated[SeasonService, Depends(get_season_service)]):
    return season_service.get_races(query)

