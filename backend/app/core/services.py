from dataclasses import dataclass
from backend.app.services.season_service import SeasonService
from backend.app.core.config import Settings


@dataclass(frozen=True)
class Services:
    season_service: SeasonService


def build_services(settings) -> Settings:
    return Services(
        season_service=SeasonService(settings),
    )

