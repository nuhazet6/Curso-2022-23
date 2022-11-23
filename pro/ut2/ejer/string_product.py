max_number = 30
spaces_amount = max_number
for i in range(1, max_number + 1):
    spaces = spaces_amount * " "
    number1 = "1" * i
    result = int(number1) * int(number1)
    print(f"{spaces}{number1}⋅{number1}{spaces} = {spaces}{result}")
    spaces_amount -= 1
