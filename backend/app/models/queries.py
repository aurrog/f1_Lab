from pydantic import BaseModel, Field


class RacesQuery(BaseModel):
    year: int = Field(default=2026, gt=0)
    
class DriversQuery(BaseModel):
    session_key: int