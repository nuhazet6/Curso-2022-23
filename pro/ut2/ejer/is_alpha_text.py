text = "hello-world"

for i in text:
    if not i.isalpha():
        print("Se han encontrado caracteres no alfabéticos")
        break
else:
    print("No se han encontrado caracteres no alfabéticos")
