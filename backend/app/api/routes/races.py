from fastapi import APIRouter, Depends
from backend.app.api.dependencies import get_season_service


router=APIRouter()


@router.get('/')
def get_races(season_service=Depends(get_season_service), year: int =2026):

    return season_service.get_races(year)



