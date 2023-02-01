# **********************
# FRECUENCIA DE PALABRAS
# **********************
from pathlib import Path


def run(input_path: Path, lower_bound: int) -> dict:
    with open(input_path, "r") as f:
        full_text = f.read()
        words = full_text.lower().split()
        uniq_words = set(words)
        freq = {}
        for word in uniq_words:
            count_word = words.count(word)
            if count_word >= lower_bound:
                freq[word] = count_word

    return freq


if __name__ == "__main__":
    run("data/word_freq/cistercian.txt", 9)
