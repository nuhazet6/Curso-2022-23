# *****************
# HAN CANTADO LÍNEA
# *****************
from pathlib import Path


def run(input_path: Path, line_no: int) -> str:
    with open(input_path, "r") as f:
        lines = f.readlines()
        max_index = len(lines) - 1
        if 0 < line_no < max_index:
            line = lines[line_no - 1].strip()
        else:
            line = None

    return line


if __name__ == "__main__":
    run("data/get_line/nasdaq.txt", 20)
