from fastapi import APIRouter, Depends
from backend.app.api.dependencies import get_season_service
from backend.app.core.models import RepositoryQuery


router=APIRouter(prefix='/races',
                 tags=['Races'],
                 )


@router.get('/', summary='Получить список гонок')
def get_races(season_service=Depends(get_season_service), year: int =2026):

    return season_service.get_races(
        RepositoryQuery(
            year=year,
        )
    )



