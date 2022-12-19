endereco = " Rua mato grosso 100, Centro, Campo Grande, MS, 79010-200"

import re # Regex

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) # match

if busca:
    cep = busca.group()
    print(cep)