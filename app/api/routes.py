from fastapi import APIRouter
from app.model.models import ScoreStats
from app.service.stats import compute_statistics

router = APIRouter()

@router.get("/stats",response_model=ScoreStats)
def get_stats():
    result = compute_statistics("../advance_py/data/students.csv")
    return result
