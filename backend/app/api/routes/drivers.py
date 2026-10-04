from fastapi import APIRouter, Depends
from backend.app.api.dependencies import get_drivers_service
from backend.app.core.models import RepositoryQuery
# from backend.app.services import 

router=APIRouter(
    prefix='/drivers',
    tags=['Drivers']
)


@router.get('/', summary='Получить список пилотов')
def get_drivers(session_key:int, drivers_service=Depends(get_drivers_service)):

    return drivers_service.get_drivers(
        RepositoryQuery(
            session_key=session_key,
        )
        )


