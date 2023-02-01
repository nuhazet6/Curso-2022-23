# **********
# HISTOGRAMA
# **********
import filecmp
from pathlib import Path


def run(data_path: Path) -> bool:
    # Lectura
    with open(data_path, "r") as f:
        full_text = f.read()
        uniq_letters = sorted(set(full_text))
        output_text = ""
        CHAR = "█"
        for letter in uniq_letters:
            count_letter = full_text.count(letter)
            output_text += f"{letter} {CHAR*count_letter} {count_letter}\n"
    # Escritura
    histogram_path = "data/histogram/histogram.txt"
    with open(histogram_path, "w") as f:
        f.writelines(output_text)

    return filecmp.cmp(histogram_path, "data/histogram/.expected", shallow=False)


if __name__ == "__main__":
    run("data/histogram/data.txt")
