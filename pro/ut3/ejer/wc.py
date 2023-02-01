# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path


def run(input_path: Path) -> tuple:
    # El número de bytes que ocupa un string "s" se puede calcular con:len(s.encode('utf-8'))
    with open(input_path) as f:
        text = f.read()
        num_bytes = len(text.encode("utf-8"))
        text = text.strip()
        num_lines = text.count("\n") + 1
        num_words = len(text.split())

    return num_lines, num_words, num_bytes


if __name__ == "__main__":
    run("data/wc/lorem.txt")
