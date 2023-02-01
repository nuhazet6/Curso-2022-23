# ********************
# LA PALABRA MÁS LARGA
# ********************
from pathlib import Path


def run(input_path: Path) -> str:
    with open(input_path, "r") as f:
        words = f.read().strip().split()
        longest_word = ""
        banned_symbols = ",.;:()"
        for word in words:
            fixed_word = word.strip(banned_symbols)
            if len(fixed_word) >= len(longest_word):
                longest_word = fixed_word

    return longest_word


if __name__ == "__main__":
    run("data/longest_word/python.txt")
