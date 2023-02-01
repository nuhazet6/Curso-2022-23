# ***********************
# REEMPLAZO DE CARACTERES
# ***********************
import filecmp
from pathlib import Path


def run(input_path: Path, replacements: str) -> bool:
    # Lectura
    with open(input_path, "r") as f:
        text = f.read()
        replacement_list = replacements.split("|")
        for old_char, new_char in replacement_list:
            text = text.replace(old_char, new_char)
    # Escritura
    output_path = "data/replace_chars/r_noticia.txt"
    with open(output_path, "w") as f:
        f.writelines(text)

    # TU CÓDIGO AQUÍ

    return filecmp.cmp(output_path, "data/replace_chars/.expected", shallow=False)


if __name__ == "__main__":
    run("data/replace_chars/noticia.txt", "áa|ée|íi|óo|úu")
