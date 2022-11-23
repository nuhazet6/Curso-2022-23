VOWELS = "aeiou"
word = "Supercalifragilisticoespialidoso"
count_vowels = 0

for letter in word:
    if letter in VOWELS:
        count_vowels += 1
print(count_vowels)
