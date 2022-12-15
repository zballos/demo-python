from src.models.pessoa import Pessoa
from src.repository.base_repository import BaseRepository


class PessoaRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.__initialize()

    def __initialize(self):
        self.create_table(
            "pessoa",
            "id INTEGER PRIMARY KEY, nome VARCHAR, data_nascimento DATETIME"
        )

    def add(self, pessoa: Pessoa):
        self.insert(self.__sql_insert(), (pessoa.nome, pessoa.data_nascimento))

    def get_all(self):
        sql = "SELECT * FROM pessoa"
        return self.query(sql)

    @staticmethod
    def __sql_insert():
        return "INSERT INTO pessoa(nome, data_nascimento) VALUES (?, ?)"

from datetime import datetime
p1 = Pessoa("Zballos", datetime.strptime("10/10/2010", "%d/%m/%Y"))
p2 = Pessoa("Jon", datetime.strptime("10/11/2012", "%d/%m/%Y"))
p3 = Pessoa("MMa", datetime.strptime("12/12/2010", "%d/%m/%Y"))

repo = PessoaRepository()
repo.add(p1)
repo.add(p2)
repo.add(p3)

r = repo.get_all()
print(r.fetchall())