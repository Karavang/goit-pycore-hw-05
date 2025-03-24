def parse_log_line(line: str) -> dict:
    return {
        "date": line.split(" ")[0],
        "time": line.split(" ")[1],
        "level": line.split(" ")[2],
        "message": " ".join(line.split()[3:]),
    }
