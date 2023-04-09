import sys

import pycheck


def run(text: str) -> str:
    # TU CÓDIGO AQUÍ
    VOWELS = "aeiou"
    output = ""
    for char in text:
        is_vowel = char.lower() not in VOWELS
        if is_vowel:
            output += char

    return output


if __name__ == "__main__":
    pycheck.check("pro.ut2.pop0.ej1", sys.argv, run)
