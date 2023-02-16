with open("envios.dat", "r") as f:
    coins = [int(coin)for coin in f.readline().strip().split()]
    clients = []
    codes = set()
    for line, client in enumerate(f):
        info_envio = line.strip().split()
        code = info_envio[0]
        amount = int(info_envio[1])
        money = int(info_envio[2])
        clients.append((code, amount, money))
with open("stock.dat", "r") as f:
    products = {}
    for line in f:
        info_product = line.strip().split()
        code = info_product[0]
        stock = int(info_product[1])
        price = int(info_product[2])
        products[code] = {"stock": stock, "price": price}
print(products)


def price(code):
    info = products.get(code, {'ERROR':-1})
    price = list(info.items()[0])
    return price


def stock(code):
    info = products.get(code, {None:None,'ERROR':-2})
    stock = list(info.items())[1]
    return stock

stock = stock('a1')

def buy(*,code,amount,money):
    total_price = price(code) * 

    if price(code = code)