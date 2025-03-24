from func.parse_log_line import parse_log_line


def load_logs(file_path: str) -> list:
    with open(file_path, "r") as file:
        return [parse_log_line(line) for line in file.readlines()]
