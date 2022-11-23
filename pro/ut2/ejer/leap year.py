year = int(input("Introduce un año:"))
mod_4 = year % 4
mod_400 = year % 400
mod_100 = year % 100

if ((mod_4) == 0 and div_100 != 0) or div_400 == 0:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
