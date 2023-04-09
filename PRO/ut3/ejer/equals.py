entr = [1, 0, 1, 1, 1, 1]
first_value = entr[0]
for i in entr[1:]:
    if i != first_value:
        print("Distintos")
        break
else:
    print("Iguales")
