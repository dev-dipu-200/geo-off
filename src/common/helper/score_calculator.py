from typing import List, Dict
from src.common.utils.validation import contains_gambling_activity


def weighted_score(scores: List[float], weights: List[float]) -> float:
    total_weight = sum(weights)
    return sum(score * weight for score, weight in zip(scores, weights)) / total_weight if total_weight else 0


def calculate_truescore(data) -> int:
    # Unpack data
    income = data.monthly_income
    income_sources = data.income_sources
    expenses = data.monthly_expenses
    overdrafts = data.overdrafts
    buffer_amount = data.emergency_buffer
    savings = data.monthly_savings
    debt_repayment = data.debt_repayment
    total_income = data.total_income
    missed_payments = data.missed_payments
    caught_up = data.caught_up_in_30_days
    payments = data.payments
    descriptions = data.transaction_descriptions
    early_repayment = data.early_repayment

    # === Income Stability (20%) ===
    # 1.1 Consistency of Income (13%)
    income_variation = (max(income) - min(income)) / max(income) * 100 if max(income) > 0 else 0
    if income_variation <= 20:
        consistency_score = 100
    elif income_variation <= 30:
        consistency_score = 75
    elif income_variation <= 40:
        consistency_score = 50
    elif income_variation <= 50:
        consistency_score = 25
    else:
        consistency_score = 0

    # 1.2 Trend of Income Growth (3.5%)
    if income[-1] > income[0]:
        trend_score = 100
    elif income[-1] == income[0]:
        trend_score = 50
    else:
        trend_score = 0

    # 1.3 Diversified Sources (3.5%)
    source_score = 100 if income_sources >= 2 else 0

    income_scores = [consistency_score, trend_score, source_score]
    income_weights = [13, 3.5, 3.5]
    income_stability = weighted_score(income_scores, income_weights)

    # === Expense Management (25%) ===
    # 2.1 Expense-to-Income Ratio (13%)
    avg_income = sum(income) / len(income)
    avg_expense = sum(expenses) / len(expenses)
    ratio = (avg_expense / avg_income) * 100 if avg_income > 0 else 0
    if ratio <= 80:
        ratio_score = 100
    elif ratio <= 90:
        ratio_score = 75
    elif ratio <= 100:
        ratio_score = 50
    elif ratio <= 110:
        ratio_score = 25
    else:
        ratio_score = 0

    # 2.2 Expense Volatility (4%)
    expense_variation = (max(expenses) - min(expenses)) / max(expenses) * 100 if max(expenses) > 0 else 0
    if expense_variation <= 15:
        volatility_score = 100
    elif expense_variation <= 25:
        volatility_score = 75
    elif expense_variation <= 35:
        volatility_score = 50
    else:
        volatility_score = 0

    # 2.3 Overdraft Usage (8%)
    if overdrafts == 0:
        overdraft_score = 100
    elif overdrafts == 1:
        overdraft_score = 75
    elif overdrafts == 2:
        overdraft_score = 50
    else:
        overdraft_score = 0

    expense_scores = [ratio_score, volatility_score, overdraft_score]
    expense_weights = [13, 4, 8]
    expense_management = weighted_score(expense_scores, expense_weights)

    # === Savings/Buffer (20%) ===
    # 3.1 Emergency Buffer (13%)
    buffer_ratio = buffer_amount / avg_expense if avg_expense > 0 else 0
    if buffer_ratio >= 2:
        buffer_score = 100
    elif buffer_ratio >= 1.5:
        buffer_score = 75
    elif buffer_ratio >= 1:
        buffer_score = 50
    else:
        buffer_score = 0

    # 3.2 Net Savings Rate (7%)
    savings_ratio = (savings / avg_income) * 100 if avg_income > 0 else 0
    if savings_ratio >= 10:
        savings_score = 100
    elif savings_ratio >= 5:
        savings_score = 50
    else:
        savings_score = 0

    savings_scores = [buffer_score, savings_score]
    savings_weights = [13, 7]
    savings_buffer = weighted_score(savings_scores, savings_weights)

    # === Debt Management (16%) ===
    # 4.1 Debt-to-Income Ratio (8%)
    debt_ratio = (debt_repayment / avg_income) * 100 if avg_income > 0 else 0
    if debt_ratio < 35:
        debt_ratio_score = 100
    elif debt_ratio <= 50:
        debt_ratio_score = 50
    else:
        debt_ratio_score = 0

    # 4.2 Missed Payments (8%)
    if missed_payments == 0:
        missed_score = 100
    elif missed_payments == 1:
        missed_score = 70
    elif missed_payments == 2:
        missed_score = 40
    else:
        missed_score = 0
    if caught_up:
        missed_score = min(missed_score + 20, 100)

    debt_scores = [debt_ratio_score, missed_score]
    debt_weights = [8, 8]
    debt_management = weighted_score(debt_scores, debt_weights)

    # === Real World Payments (12%) ===
    def payment_score(status):
        if status == "on_time":
            return 100
        elif status == "one_late":
            return 50
        else:
            return 0

    rent_score = payment_score(payments.get("rent", "unknown"))
    utility_score = payment_score(payments.get("utilities", "unknown"))
    phone_score = payment_score(payments.get("phone", "unknown"))
    sub_score = payment_score(payments.get("subscriptions", "unknown"))

    real_world_scores = [rent_score, utility_score, phone_score, sub_score]
    real_world_weights = [4, 4, 2.5, 1.5]
    real_world_payments = weighted_score(real_world_scores, real_world_weights)

    # === Positive Financial Behaviours (7%) ===
    savings_rate_score = 100 if savings_ratio > 10 else 0
    early_repay_score = 100 if early_repayment else 0

    positive_scores = [savings_rate_score, early_repay_score]
    positive_weights = [4.5, 2.5]
    positive_behaviour = weighted_score(positive_scores, positive_weights)

    # === Final Aggregation ===
    true_score = (
        income_stability * 0.20 +
        expense_management * 0.25 +
        savings_buffer * 0.20 +
        debt_management * 0.16 +
        real_world_payments * 0.12 +
        positive_behaviour * 0.07
    )

    # Gambling Penalty
    if contains_gambling_activity(descriptions):
        true_score = max(0, true_score - 10)

    return round(true_score)
