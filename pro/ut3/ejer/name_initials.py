"""
Dado un nombre y apellidos en formato "apellidos, nombre", obtenga las iniciales de dicha
persona pasadas a mayúsculas y con punto al final.
"""


def run(fullname: str) -> str:
    fullname = fullname.upper().split(", ")
    initials = fullname[1][0] + "."
    surname = fullname[0].split(" ")
    first_surname = surname[0][0] + "."
    if len(surname) == 1:
        initials += first_surname
    else:
        initials += first_surname + surname[1][0] + "."
    return initials


if __name__ == "__main__":
    run("Delgado Quintero, sergio")
