import re
text = 'Estaré disponible en el +34755142009 el lunes por la tarde +34755142003'
regex = r'\+?\d{2}\d{9}'

m = re.search(regex, text)
print(m[0])