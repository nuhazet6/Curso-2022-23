year = 2007
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
