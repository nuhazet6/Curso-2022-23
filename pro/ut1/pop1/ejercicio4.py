# ut1-pop1-ej4
hexcolor = "A131F7"
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓

red_color = int(hexcolor[:2], 16)
green_color = int(hexcolor[2:4], 16)
blue_color = int(hexcolor[4:], 16)
rgb_color = f"({red_color},{green_color},{blue_color})"

# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert rgb_color == "(161,49,247)"
