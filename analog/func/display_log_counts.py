def display_log_counts(counts: dict):
    res = "Рівень логування | Кількість\n-----------------|----------\n"
    for level, count in counts.items():
        res += f"{level:<16} | {count}\n"
    return res
