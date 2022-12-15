from datetime import date


class Pessoa:
    def __init__(self, nome: str, data_nascimento: date):
        self.__id = None
        self.__nome = nome
        self.__data_nascimento = data_nascimento

    @property
    def nome(self):
        return self.__nome

    @property
    def data_nascimento(self) -> str:
        return self.__data_nascimento.strftime("%d/%m/%Y")

    @property
    def id(self):
        return self.__id

    @staticmethod
    def campo():
        pass




