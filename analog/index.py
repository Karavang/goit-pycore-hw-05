from sys import argv
from os import path
from func.count_logs_by_level import count_logs_by_level
from func.display_log_counts import display_log_counts
from func.filter_logs_by_level import filter_logs_by_level
from func.load_logs import load_logs


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
