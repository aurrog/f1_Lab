from fastapi import APIRouter
from backend.app.api.routes import drivers, races, health


router=APIRouter(tags=['API'])

router.include_router(drivers.router, prefix='/drivers', tags=['drivers'])
router.include_router(health.router, prefix='/health', tags=['health'])
router.include_router(races.router, prefix='/races', tags=['races'])
