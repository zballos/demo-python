# "https://ge.globo.com/busca/?q=flamengo"

import re

url = "https://ge.globo.com/busca/?q=flamengo"

padrao_url = re.compile('(https://)?(www.)?ge.globo.com(.br)?/busca/')
match = padrao_url.match(url)

if not match:
    raise ValueError("URL inválida")

print("URL válida")