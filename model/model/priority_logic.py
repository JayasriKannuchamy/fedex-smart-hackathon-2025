def calculate_priority(amount, overdue_days):
    if amount > 100000 or overdue_days > 60:
        return "High"
    elif amount > 50000 or overdue_days > 30:
        return "Medium"
    else:
        return "Low"
