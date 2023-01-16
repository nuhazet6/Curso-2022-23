str1 = "abc"
str2 = "123"
output = ""
for i in str1:
    for j in str2:
        output += f"{i}{j} "
print(output)
