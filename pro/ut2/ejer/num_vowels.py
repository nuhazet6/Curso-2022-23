text = "Supercalifragilisticoespialidoso"
VOWELS = "aeiou"
vowels_amount = 0
for char in text:
    if char.lower() in VOWELS:
        vowels_amount += 1
print(vowels_amount)
