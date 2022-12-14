from src.models.pessoa import Pessoa
from src.repository.base_repository import BaseRepository


class PessoaRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.__initialize()

    def __initialize(self):
        self.create_table(
            table=str(Pessoa).lower(),
            columns="id INTEGER PRIMARY KEY, nome VARCHAR, data_nascimento DATETIME"
        )

    def add(self, pessoa: Pessoa):
        self.insert(self.__sql_insert(), (pessoa.nome, pessoa.data_nascimento,))
        print(pessoa)

    @staticmethod
    def __sql_insert():
        return "INSERT INTO pessoa(nome, data_nascimento) VALUES (?, ?)"

p1 = Pessoa("Zballos", "10-10-2010")

repo = PessoaRepository()
repo.add(p1)
