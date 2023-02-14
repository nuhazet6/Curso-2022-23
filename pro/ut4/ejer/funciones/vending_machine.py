with open("stock.dat", "r") as f:
    product = {}
    for line in f:
        info_product = line.strip().split()
        code = info_product[0]
        stock = int(info_product[1])
        price = int(info_product[2])
        product[code] = {"stock": stock, "price": price}
print(product)


def price(*, code=""):
    info = products.get(code, 0)
    if info is None:
        return None
    return info.values()[0]


def have_stock(*, code=""):
    info = products.get(code, 0)
