# ********
# PANGRAMA
# ********


def is_pangram(text:str):
    ALPHABET = set('abcdefghijklmnopqrstiuvwxyz ')
    uniq_letters = set(text.lower())
    return uniq_letters == ALPHABET

