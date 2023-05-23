import re

# Escriba un programa en Python que encuentre todas las palabras que comiencen por vocal en un texto dado.
regex = r"\b[aeiou]\S*\b"
text = "asdf uasdf iasdf oasdf esdf fasdf hgtd .sdf asd. efasd, "
output = re.findall(regex, text)
print(output)
