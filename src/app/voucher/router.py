from fastapi import APIRouter, Depends
from src.app.voucher.schemas.voucher_schema import FinancialData
from src.common.helper.score_calculator import calculate_truescore
from src.app.authentication.service import get_current_user

router = APIRouter(
    prefix="/vouchers",
    tags=["Vouchers"],
)

@router.post("/truescore")
def get_truescore(data: FinancialData, current_user: dict = Depends(get_current_user)):
    score = calculate_truescore(data)
    return {"truescore": score}
