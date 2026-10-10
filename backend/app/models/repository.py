from dataclasses import dataclass
import hashlib


@dataclass
class RepositoryQuery:
    query_type:str | None = None
    year: int | None = None
    session_key: int | None = None
    driver_number: int | None = None

    def get_id(self):
        normalized=f'{self.query_type} {self.year} {self.session_key} {self.driver_number}'.encode()

        return hashlib.sha256(normalized).hexdigest()
