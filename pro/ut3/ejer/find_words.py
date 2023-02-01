# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    # Lectura
    with open(data_path, "r") as f:
        #        matches = []
        #        lower_target_word = target_word.lower()
        #        target_len = len(target_word)
        #        for row, line in enumerate(f):
        #            target_text = line.lower()
        #            target_words_count = target_text.count(lower_target_word)
        #            original_index = 0
        #            for _ in range(target_words_count):
        #                word_index = target_text.index(lower_target_word)
        #                original_index += word_index
        #                no_word_before = not target_text[word_index - 1].isalpha()
        #                no_word_after = not target_text[word_index + target_len].isalpha()
        #                if no_word_before and no_word_after:
        #                    matches.append((row + 1, original_index + 1))
        #                target_text = line[original_index + target_len :]
        #                original_index += target_len

        banned_elements = ".,:;()'¡!-"
        matches = []
        lower_target = target_word.lower()
        for row, line in enumerate(f, start=1):
            general_index = 1
            for spaces, word in enumerate(line.strip().split()):
                lower_word = word.lower()
                general_index += lower_word.find(lower_target)
                if lower_word.strip(banned_elements) == lower_target:
                    matches.append((row, general_index + spaces))
                else:
                    general_index += 1
                general_index += len(word)

    return matches


if __name__ == "__main__":
    run("data/find_words/bzrp.txt", "persona")
