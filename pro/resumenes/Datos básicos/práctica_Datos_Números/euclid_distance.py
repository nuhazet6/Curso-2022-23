# ******************
# DISTANCIA EUCLÍDEA
# ******************


def run(x1: float, y1: float, x2: float, y2: float) -> float:
    x_hick = x2 - x1
    y_hick = y2 - y1
    distance = (x_hick**2 + y_hick**2) ** 0.5
    return distance


if __name__ == "__main__":
    run(3, 5, -7, -4)
