from backend.app.integrations.contrant import F1Client
from backend.storage.contracts import BaseRepository


class TelemetryService:
    def __init__(self, data_client:F1Client, repository: BaseRepository):
        self.data_client=data_client
        self.repository=repository