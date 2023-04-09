# Ejercicio 1
name = "Nuhazet"
surname = "Correa Torres"
print(f"{surname}, {name}")

# Ejercicio 2
path = "//1.1.1.1/eoi/python"
path = path.split("/", 3)
print(f"equipo={path[2]:s};ruta={path[3]:s}")

# Ejercicio 2.01
path = "//1.1.1.1/eoi/python"
path = path.strip("/")
path = path.split("/", 1)
print(f"equipo={path[0]:s};ruta={path[1]:s}")

# Ejercicio 2.1
path = "//1.1.1.1/eoi/python"
path = path.strip("/")
slash_index = path.find("/")
print(f"equipo={path[:slash_index]};ruta={path[(slash_index):]}")

# Ejercicio 2.1.1
path = "//1.1.1.1/eoi/python"
path = path.strip("/")
slash_index = path.find("/")
host = path[:slash_index]
host_path = path[slash_index:]
print(f"equipo={host};ruta={host_path}")

# Ejercicio 3
dni_number = "12345678"
CONTROL_LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"
control_index = int(dni_number) % 23
control_letter = CONTROL_LETTERS[control_index]
print(f"{dni_number}{control_letter}")

# Ejercicio 4
value = "5"
print(int(value) + int(value * 2) + int(value * 3))

# Ejercicio 5
word = "ordenador"
word_len = len(word)
vowels_count = (
    word.count("a")
    + word.count("e")
    + word.count("i")
    + word.count("o")
    + word.count("u")
)
print(vowels_count * word_len)
