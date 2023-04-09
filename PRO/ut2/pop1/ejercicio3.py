import sys

import pycheck

CHECK_CASES = [
    [["AGTCCCAGGT"], "AGUCCCAGGU"],
    [["GCGCACTCTTCTTTGCTCTT"], "GCGCACUCUUCUUUGCUCUU"],
    [["CCGGAGATTGGCTACTGAAGATCCA"], "CCGGAGAUUGGCUACUGAAGAUCCA"],
]


def run(adn: str) -> str:
    arn = ""
    for char in adn:
        if char == "T":
            arn += "U"
        else:
            arn += char

    return arn


if __name__ == "__main__":
    pycheck.check(run, CHECK_CASES, sys.argv)
