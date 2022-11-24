"""
Dado un nombre y apellidos en formato "apellidos, nombre", obtenga las iniciales de dicha
persona pasadas a mayúsculas y con punto al final.
"""


def run(fullname: str) -> str:
    fullname = fullname.upper().split(", ")
    initial_name = fullname[1][0]
    surname = fullname[0].split(" ")
    first_surname = surname[0][0]
    if len(surname) > 1:
        second_surname = surname[1][0] + "."
    else:
        second_surname = ""
    initials = f"{initial_name}.{first_surname}.{second_surname}"
    return initials


if __name__ == "__main__":
    run("Delgado Quintero, sergio")
