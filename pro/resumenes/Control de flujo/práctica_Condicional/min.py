num1 = 7
num2 = 7
num3 = 3
if num1 <= num2 and num1 <= num3:
    min = num1
elif num2 <= num3:
    min = num2
else:
    min = num3
print(min)
