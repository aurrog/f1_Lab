from pydantic import BaseModel, Field


class RacesQuery(BaseModel):
    year: int = Field(default=2026, gt=0)
    
class DriversQuery(BaseModel):
    session_key: int = Field(gt=0)

class TelemetryQuery(BaseModel):
    session_key: int = Field(gt=0)
    driver_number: int = Field(gt=0)
    