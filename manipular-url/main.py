def print_hi(name, url):

    # limpeza
    url = url.strip()

    # validacao url
    if not url:
        raise ValueError("URL vazia")

    print(f'Ola, {name}: {url}')

    index_parametro = url.find("?")
    size_url = len(url)
    print(url[index_parametro+1:size_url])


if __name__ == '__main__':
    print_hi('PyCharm', "https://ge.globo.com/busca/?q=flamengo")
    print_hi('PyCharm', "")

