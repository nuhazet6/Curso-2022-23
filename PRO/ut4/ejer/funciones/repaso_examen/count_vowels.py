# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************


def count_vowels(text:str):
    VOWELS = 'aeiou'
    if len(text) == 0:
        return 0
    if text[0] in VOWELS:
        return 1 + count_vowels(text[1:])
    return 0 + count_vowels(text[1:])