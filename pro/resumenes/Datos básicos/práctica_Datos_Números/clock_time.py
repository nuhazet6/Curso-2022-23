# *********************
# CONTANDO MILISEGUNDOS
# *********************


def run(hours: int, minutes: int, seconds: int) -> float:
    seconds += hours * 3600 + minutes * 60
    time_since_midnight = seconds * 1000
    return time_since_midnight


if __name__ == "__main__":
    run(0, 1, 1)
