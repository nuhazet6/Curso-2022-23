import re

regex = r"\b(?:\d+\.\d*)|(?:\d*\.\d+)\b"

text = "213.213 .32 323. 12,32"

output = re.findall(regex, text)

print(output)
