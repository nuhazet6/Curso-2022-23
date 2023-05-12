# ******************
# LA PALABRA PERDIDA
# ******************


def run(text: str, target_word: str, replace_word: str) -> str:
    # TU CÓDIGO AQUÍ
    target_word_start = text.find(target_word)
    target_word_end = target_word_start + len(target_word)
    mtext = text[:target_word_start] + replace_word + text[target_word_end:]
    return mtext


if __name__ == '__main__':
    run('This is a beautiful night on the Atlantic', 'beautiful', 'terrible')