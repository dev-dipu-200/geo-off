from fastapi import APIRouter
from src.models.schemas import FinancialData
from src.common.helper.score_calculator import calculate_truescore

router = APIRouter()

@router.post("/truescore")
def get_truescore(data: FinancialData):
    score = calculate_truescore(data)
    return {"truescore": score}
