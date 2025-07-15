from fastapi import APIRouter
from src.app.voucher.schemas.voucher_schema import FinancialData
from src.common.helper.score_calculator import calculate_truescore

router = APIRouter(
    prefix="/vouchers",
    tags=["Vouchers"],
)

@router.post("/truescore")
def get_truescore(data: FinancialData):
    score = calculate_truescore(data)
    return {"truescore": score}
