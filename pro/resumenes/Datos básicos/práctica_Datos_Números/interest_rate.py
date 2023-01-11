# *****************
# INTERÉS COMPUESTO
# *****************


def run(amount: float, rate: float, years: int) -> float:
    rate_percentage = rate / 100
    future_amount = amount * (1 + rate_percentage) ** years
    return future_amount


if __name__ == "__main__":
    run(10000, 3.5, 7)
