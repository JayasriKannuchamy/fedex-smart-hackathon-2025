def calculate_priority(amount, overdue_days):
    score = (amount * 0.00001) + overdue_days

    if score > 20:
        return "High"
    elif score > 10:
        return "Medium"
    else:
        return "Low"
