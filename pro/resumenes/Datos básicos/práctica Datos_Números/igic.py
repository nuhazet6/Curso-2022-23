# ***************
# PRECIO SIN IGIC
# ***************


def run(price_with_igic: float, igic: float) -> float:
    igic = 1 + igic / 100
    clean_price = round(price_with_igic / igic, 2)
    return clean_price


if __name__ == "__main__":
    run(120, 7)
