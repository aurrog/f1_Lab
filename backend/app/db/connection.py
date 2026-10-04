from pathlib import Path
from typing import Protocol, Sequence, Any, Optional
import sqlite3


class DataBase(Protocol):
    def __init__(self, db_path) -> None: ...
    # def connect(self) -> None: ...
    # def disconnect(self) -> None: ...
    def execute(self, query:str, params: Sequence[Any] | None = None) -> Any: ...
    def fetch_one(self, query: str, params: Sequence[Any] | None = None) -> Optional[Any]: ...
    def fetch_all(self, query: str, params: Sequence[Any] | None = None) -> Any: ...



class SQLite3DataBase:
    def __init__(self, db_path):
        self.db_path = db_path

    def execute(self, query, params=None):
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute(query, params or ())
            conn.commit()
        finally:
            conn.close()

    def fetch_one(self, query, params=None):
        conn = sqlite3.connect(self.db_path)
        try:
            conn.row_factory = sqlite3.Row
            row = conn.execute(query, params or ()).fetchone()
            return dict(row) if row is not None else None
        finally:
            conn.close()