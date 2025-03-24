from sys import argv
from os import path
from collections import defaultdict


def parse_log_line(line: str) -> dict:
    return {
        "date": line.split(" ")[0],
        "time": line.split(" ")[1],
        "level": line.split(" ")[2],
        "message": " ".join(line.split()[3:]),
    }


def load_logs(file_path: str) -> list:
    with open(file_path, "r") as file:
        return [parse_log_line(line) for line in file.readlines()]


def filter_logs_by_level(logs: list, level: str) -> list:
    list_logs = [log for log in logs if level in log["level"]]
    if not list_logs:
        return "Don't contains this log lvl"
    res = ""
    for log in list_logs:
        res += f"{log['date']} {log['time']} - {log['message']}\n"
    return res


def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return counts


def display_log_counts(counts: dict):
    res = "Рівень логування | Кількість\n-----------------|----------\n"
    for level, count in counts.items():
        res += f"{level:<16} | {count}\n"
    return res


def main():
    try:
        if not (
            path.exists(argv[1]) and path.isfile(argv[1]) and argv[1].endswith(".log")
        ):
            return "Path does not exist or is not a .log file"

        fh = open(argv[1], "r")
        if len(argv) >= 3:
            counts = count_logs_by_level(load_logs(argv[1]))
            res = display_log_counts(counts)
            filtered = filter_logs_by_level(load_logs(argv[1]), argv[2].upper())
            res += f"\n{filtered}"
            fh.close()
            return res
        else:
            counts = count_logs_by_level(load_logs(argv[1]))
            res = "Рівень логування | Кількість\n-----------------|----------\n"
            for level, count in counts.items():
                res += f"{level:<16} | {count}\n"
            fh.close()
            return res

    except IndexError:
        print("No arguments provided")


print(main())
