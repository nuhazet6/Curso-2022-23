# ****************
# EL CUADRADO ROJO
# ****************


def run(arc_A: float) -> float:
    PI = 3.14
    lado = arc_A * 2.0 / PI
    area = round(lado**2.0, 17)
    return area


if __name__ == "__main__":
    run(1)
