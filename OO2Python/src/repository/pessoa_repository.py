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
