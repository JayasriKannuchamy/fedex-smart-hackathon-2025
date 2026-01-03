from pipeline.assign_dca import assign_dca

tests = [
    (150000, 90),   # High priority
    (60000, 40),    # Medium priority
    (20000, 10)     # Low priority
]

for amount, days in tests:
    priority, dca = assign_dca(amount, days)
    print(
        f"Amount: {amount}, Days: {days} -> "
        f"Priority: {priority}, Assigned DCA: {dca}"
    )