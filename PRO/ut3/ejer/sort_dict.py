# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> dict:
    #    values_first_list_sorted = sorted(
    #        [(values, key) for key, values in unsorted_items.items()]
    #    )
    #    sorted_items = [(key, values) for values, key in values_first_list_sorted]

    packed_items = sorted([f"{value}:{key}" for key, value in unsorted_items])
    sorted_items = []
    for item in packed_items:
        value, key = item.split(":")
        fixed_item = (key, value)
        sorted_items.append()
    return sorted_items


if __name__ == "__main__":
    run({"a": "two", "b": "one", "c": "three"})
