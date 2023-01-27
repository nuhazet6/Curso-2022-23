# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path


def run(input_path: Path) -> tuple:
    # El número de bytes que ocupa un string "s" se puede calcular con:len(s.encode('utf-8')) 
    with open(input_path) as f:
        num_lines = len(f.readlines())
        num_words = len(f.read)
        num_bytes = 0
        for lane in f.readlines():
            

    return num_lines, num_words, num_bytes


if __name__ == "__main__":
    run("data/wc/lorem.txt")
