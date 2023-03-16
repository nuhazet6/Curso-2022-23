# *********************************
# SEPARANDO MAYÚSCULAS Y MINÚSCULAS
# *********************************


def split_case(words:list):
    lower_words = [word for word in words if word==word.lower()]
    upper_words = [word for word in words if word==word.upper()]
    return lower_words,upper_words
