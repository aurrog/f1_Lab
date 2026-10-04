from typing import Protocol
from pathlib import Path


class BaseRepository(Protocol):
    def get(self, id: str, data:dict) -> dict | None: ...
    def write(self, filename: Path, data: dict) -> None: ...
