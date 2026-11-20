from pydantic import BaseModel


class Race(BaseModel):
    session_key: int
    session_type: str
    session_name: str

    country_name: str
    location: str

    date_start: str
    date_end: str

    year: int
