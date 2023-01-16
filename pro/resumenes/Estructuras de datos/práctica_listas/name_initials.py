# **********************
# INICIALES DE UN NOMBRE
# **********************


def run(fullname: str) -> str:
    splitted_fullname = fullname.upper().split(", ")
    name = splitted_fullname[1]
    surname = splitted_fullname[0].split(" ")
    initials = name[0] + "." + surname[0][0] + "."
    if len(surname) == 2:
        initials += surname[1][0] + "."
    return initials


if __name__ == "__main__":
    run("Delgado Quintero, sergio")
