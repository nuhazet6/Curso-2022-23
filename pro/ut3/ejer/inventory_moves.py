# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:
    items_list = imoves.split(",")
    inventory = {}
    for item in items_list:
        key = item[0]
        amount = int(item[1:])
        inventory[key] = inventory.get(key, 0) + amount
        # if key not in inventory:
        #    inventory[key] = amount
        # else:
        #    inventory[key] += amount
    return inventory


if __name__ == "__main__":
    run("A1,B4,A-2,A7,B1,C4")
