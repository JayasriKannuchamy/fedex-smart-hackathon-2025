from model.model.priority_logic import calculate_priority
from model.dca_profile import DCA_PROFILES


def assign_dca(amount, overdue_days):
    priority = calculate_priority(amount, overdue_days)

    best_dca = None
    best_score = -1

    for dca, details in DCA_PROFILES.items():

        # 1️⃣ Skill match score
        priority_score = 1 if details["skill"] == priority else 0.5

        # 2️⃣ Load penalty (less load = better)
        load_score = 1 / (details["current_load"] + 1)

        # 3️⃣ Final weighted score
        final_score = (
            priority_score * 0.5 +
            details["success_rate"] * 0.3 +
            load_score * 0.2
        )

        if final_score > best_score:
            best_score = final_score
            best_dca = dca

    return priority, best_dca
