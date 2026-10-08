from typing import Protocol
from dataclasses import dataclass
from pathlib import Path


@dataclass
class RepositoryFileLoadError:
    message:str


class BaseRepository(Protocol):
    def get(self, id: str, data:dict) -> dict | None: ...
    def write(self, filename: Path, data: dict) -> None: ...
