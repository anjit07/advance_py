from pydantic import BaseModel

class ScoreStats(BaseModel):
    mean: float
    std: float
    min: float
    max: float
