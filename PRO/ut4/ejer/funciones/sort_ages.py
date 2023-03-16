# ********************
# ORDENANDO POR EDADES
# ********************


def run(people: list) -> list:
    # TU CÓDIGO AQUÍ
    speople = sorted(people, key=lambda p: p["age"])

    return speople


if __name__ == "__main__":
    run(
        [
            {"name": "DeRozan", "age": 33},
            {"name": "Lonzo", "age": 25},
            {"name": "Beverly", "age": 34},
            {"name": "Dragic", "age": 36},
            {"name": "Williams", "age": 21},
        ]
    )
