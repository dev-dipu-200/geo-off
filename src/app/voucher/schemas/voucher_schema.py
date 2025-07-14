from pydantic import BaseModel
from typing import List, Optional

class FinancialData(BaseModel):
    monthly_income: List[float]  # last 6 months
    income_sources: int
    monthly_expenses: List[float]
    overdrafts: int
    emergency_buffer: float
    monthly_savings: float
    debt_repayment: float
    total_income: float
    missed_payments: int
    caught_up_in_30_days: bool
    payments: dict  # rent, utilities, phone, subscriptions with on-time status
    transaction_descriptions: List[str]  # for gambling detection
    early_repayment: bool
    
