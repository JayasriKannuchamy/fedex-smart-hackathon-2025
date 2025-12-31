from model.priority_logic import calculate_priority

def assign_dca(amount, overdue_days):
    priority = calculate_priority(amount, overdue_days)

    if priority == "High":
        return priority, "DCA_A"
    elif priority == "Medium":
        return priority, "DCA_B"
    else:
        return priority, "DCA_C"
