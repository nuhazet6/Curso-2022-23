# **************************
# AQUÍ TIENE SU VUELTA (MAX)
# **************************


def run(to_give_back: float, available_currencies: dict) -> dict:

    money_back = {}
    for currency, currency_amount in sorted(available_currencies.items(), reverse=True):
        if to_give_back > 0:
            quotient = to_give_back // currency
            currency_amount_output = min(quotient, currency_amount)
            money_back[currency] = currency_amount_output
            to_give_back -= currency_amount_output * currency
        else:
            break
    if to_give_back > 0:
        return None
    return money_back


if __name__ == "__main__":
    run(20, {5: 3, 2: 7, 1: 3})
