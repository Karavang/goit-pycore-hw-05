from collections import defaultdict


def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return counts
