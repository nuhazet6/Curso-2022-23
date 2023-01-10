word = "ordenador"
VOWELS = "AEIOU"
total_vowels = 0
for vowel in VOWELS:
    total_vowels += word.upper().count(vowel)
metric = total_vowels * len(word)
print(metric)
