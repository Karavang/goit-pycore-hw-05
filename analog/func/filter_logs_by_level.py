def filter_logs_by_level(logs: list, level: str) -> list:
    list_logs = [log for log in logs if level in log["level"]]
    if not list_logs:
        return "Don't contains this log lvl"
    res = ""
    for log in list_logs:
        res += f"{log['date']} {log['time']} - {log['message']}\n"
    return res
