# **********************
# ANIMALES SUPER RÁPIDOS
# **********************


def run(speed_km_h: float) -> float:
    speed_cm_s = (speed_km_h * 100_000) // 3600
    return speed_cm_s


if __name__ == "__main__":
    run(1.08)
