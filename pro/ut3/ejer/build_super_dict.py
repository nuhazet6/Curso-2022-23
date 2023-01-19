# ***************************
# DICCIONARIO EN CONSTRUCCIÓN
# ***************************


def run(items: list) -> dict:
    # Original: unpack_items = {item_list[0]: item_list[1:] for item_list in items}
    unpack_items = {key: values for key, *values in items}
    return unpack_items


if __name__ == "__main__":
    run(
        [
            ["Episode IV - A New Hope", "May 25", 1977, "George Lucas"],
            ["Episode V - The Empire Strikes Back", "May 21", 1980],
            ["Episode VI - Return of the Jedi", "May 25", 1983],
        ]
    )
