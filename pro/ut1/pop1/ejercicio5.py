# ut1-pop1-ej5
text = "El Sistema Operativo que funcionará Libre y Gratuito"
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓

lower_text = text.lower()
hyphen_text = lower_text.replace(" ", "-")
slug = (
    hyphen_text.replace("í", "i")
    .replace("é", "e")
    .replace("á", "a")
    .replace("ó", "o")
    .replace("ú", "u")
)

# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert slug == "el-sistema-operativo-que-funcionara-libre-y-gratuito"
