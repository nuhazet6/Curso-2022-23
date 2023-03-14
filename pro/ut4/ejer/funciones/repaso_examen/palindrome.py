# **********
# PALÍNDROMO
# **********


def is_palindrome(text:str):
    without_spaces = text.replace(" ","").lower()
    return without_spaces == without_spaces[::-1]
