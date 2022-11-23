word = input("Introducir palabra:")
is_isogram = True
for char in word:
    if char.isalnum():
        alphanum_index = word.index(char)
        if char in word[alphanum_index:]:
            isogram = False
            break
if is_isogram:
    print(f"La palabra {word} es un isograma")
else:
    print(f"La palabra {word} no es un isograma")

word = input("Introduce una palabra:")
seen_letters = []
for char in word:
    if char.isalpha():
        if char in seen_letters:
            print(f"la palabra {word} no es un isograma")
            break
        seen_letters += char
else:
    print(f"la palabra {word} es un isograma")
