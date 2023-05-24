import re

regex = r"\b[\w.]+@[\w]+.[\w]+"
text = "asdf,342erf@9853.cefr sdf@asdf.cds"
output = re.findall(regex, text)
print(output)
