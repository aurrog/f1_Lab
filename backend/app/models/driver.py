from pydantic import BaseModel

class Driver:
    session_key: int
    driver_number: int

    broadcast_name: str
    full_name: str
    name_acronym: str

    team_name: str

    first_name: str
    last_name: str
    