# ********************
# DESCIFRANDO CIUDADES
# ********************


def run(cinfo: str) -> dict:
    cinfo = cinfo.replace(";", ":").split(":")
    cities = {}
    print(cinfo)
    for key_index in range(0, len(cinfo), 2):
        print(key_index)
        cities[cinfo[key_index]] = int(cinfo[key_index + 1])
    return cities


if __name__ == "__main__":
    run("Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;Mumbai:21_357_000")
