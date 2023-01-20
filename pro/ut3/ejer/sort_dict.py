# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> dict:
    values_list = sorted(unsorted_items.values())
    for tuple in unsorted_items.items():
        
    #    values_first_list_sorted = sorted(
    #        [(values, key) for key, values in unsorted_items.items()]
    #    )
    #    sorted_items = [(key, values) for values, key in values_first_list_sorted]

    sorted_items = "2"
    return sorted_items


if __name__ == "__main__":
    run({"a": "two", "b": "one", "c": "three"})
