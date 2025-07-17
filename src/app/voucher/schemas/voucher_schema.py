from pydantic import BaseModel, Field
from typing import List, Optional


class FinancialData(BaseModel):
    monthly_income: List[float] = Field(
        min_items=6,
        description="Last 6 months of monthly income",
        default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    )  # last 6 months
    income_sources: int = Field(description="Number of income sources", default=0)
    monthly_expenses: List[float] = Field(
        min_items=6,
        description="Last 6 months of monthly expenses",
        default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    )
    overdrafts: int = Field(description="Number of overdrafts", default=0)
    emergency_buffer: float = Field(description="Emergency buffer amount", default=0.0)
    monthly_savings: float = Field(description="Monthly savings", default=0.0)
    debt_repayment: float = Field(description="Debt repayment", default=0.0)
    total_income: float = Field(description="Total income", default=0.0)
    missed_payments: int = Field(description="Number of missed payments", default=0)
    caught_up_in_30_days: bool = Field(
        description="Flag to indicate if caught up in 30 days", default=False
    )
    payments: dict = Field(
        description="List of payments", default={}
    )  # rent, utilities, phone, subscriptions with on-time status
    transaction_descriptions: List[str] = Field(
        description="List of transaction descriptions", default=[]
    )  # for gambling detection
    early_repayment: bool = Field(
        description="Flag to indicate early repayment", default=False
    )
