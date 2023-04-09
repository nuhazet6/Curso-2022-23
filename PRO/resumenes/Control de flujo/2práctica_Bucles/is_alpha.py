ALPHABET = "abcdefghijklmnopqrstuvwxyz"
text = "hello world"
for char in text:
    if char not in ALPHABET:
        print("Se han encontrado caracteres no alfabéticos")
        break
else:
    print("Todo correcto")
