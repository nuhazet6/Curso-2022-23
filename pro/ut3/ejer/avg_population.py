# ******************
# POBLACIÓN PROMEDIO
# ******************


def run(pdata: dict) -> dict:
    total_population = sum(pdata.values())
    avg_data = {}
    for city, pop in pdata.items():
        percentage = pop / total_population * 100
        avg_data[city] = round(percentage, 3)
    lista = list(pdata.values())
    print(lista.pop())
    return avg_data


if __name__ == "__main__":
    run(
        {"Tokyo": 38140000, "Delhi": 26454000, "Shanghai": 24484000, "Mumbai": 21357000}
    )
