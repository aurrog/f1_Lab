from fastapi import APIRouter
from backend.app.api.routes import drivers, races, health, telemetry, laps


router=APIRouter()

router.include_router(health.router)

router.include_router(races.router)
router.include_router(drivers.router)

router.include_router(telemetry.router)
router.include_router(laps.router)
