# ut1-pop0-ej1
seconds = 31256
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓
seconds_remain = seconds % 3600
hours = seconds // 3600
minutes = seconds_remain // 60
seconds = seconds_remain % 60

# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert hours == 8
assert minutes == 40
assert seconds == 56
