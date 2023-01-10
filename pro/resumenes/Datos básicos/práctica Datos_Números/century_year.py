# **************************
# BUSCANDO EL SIGLO ADECUADO
# **************************


def run(year: int) -> int:
    is_next_century = (year % 100) > 0
    century = year // 100 + is_next_century
    return century


if __name__ == "__main__":
    run(1705)
