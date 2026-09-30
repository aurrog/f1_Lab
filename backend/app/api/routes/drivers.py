from fastapi import APIRouter, Depends
from backend.app.api.dependencies import get_season_service
# from 

router=APIRouter()


@router.get('/')
def get_drivers(session_key:int, season_service=Depends(get_season_service)):

    return {}


