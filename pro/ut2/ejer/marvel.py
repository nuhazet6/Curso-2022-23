can_fly = input("¿Puede volar?[s/n] ") == "s"
is_human = input("¿Es humano?[s/n] ") == "s"
has_mask = input("¿Tiene máscara?[s/n] ") == "s"
if can_fly:
    if is_human:
        if has_mask:
            print("Ironman")
        else:
            print("Captain Marvel")
    else:
        if has_mask:
            print("Ronan Accuser")
        else:
            print("Vision")
else:
    if is_human:
        if has_mask:
            print("Spiderman")
        else:
            print("Hulk")
    else:
        if has_mask:
            print("Black Bolt")
        else:
            print("Thanos")
