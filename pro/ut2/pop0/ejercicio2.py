import sys

import pycheck


def run(word: str) -> float:
    char_sum = 0
    for char in word:
        char_sum += ord(char)
    char_avg = char_sum / len(word)
    return char_avg


if __name__ == "__main__":
    pycheck.check("pro.ut2.pop0.ej2", sys.argv, run)
