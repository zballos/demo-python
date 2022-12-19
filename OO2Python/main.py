from datetime import datetime
from src.models.pessoa import Pessoa
from src.repository.pessoa_repository import PessoaRepository

def pessoa_repository():
    first = Pessoa("Zballos", datetime.strptime("10/10/2010", "%d/%m/%Y"))
    second = Pessoa("Jon", datetime.strptime("10/11/2012", "%d/%m/%Y"))
    third = Pessoa("MMa", datetime.strptime("12/12/2010", "%d/%m/%Y"))

    repo = PessoaRepository()
    repo.add(first)
    repo.add(second)
    repo.add(third)

    r = repo.get_all()
    print(r.fetchall())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pessoa_repository()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
