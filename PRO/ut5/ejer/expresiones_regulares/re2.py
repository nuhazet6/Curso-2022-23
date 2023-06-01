import re

# Escriba un programa en Python que encuentre todas las URLs en un texto dado.
regex = r"\bhttps?://(?:\w+\.)+[^/]+(?:\/[^ ,]*)*"
# regex = r"\bhttps?:\/\/[\w\-]+(\.[\w\-]+)+[/#?]?.*\b"
text = "https://pythex.org/ http://w3.unpocodetodo.info/utiles/regex-ejemplos.php?type=mix https://aprendepython.es/stdlib/text_processing/re/#buscar"
output = re.findall(regex, text)
print(output)
