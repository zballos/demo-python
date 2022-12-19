import sqlite3


class SQliteDbContext:
    def __init__(self):
        self.__conn = sqlite3.connect("local.db")

    @property
    def commit(self):
        self.__conn.commit()

    @property
    def cursor(self):
        return self.__conn.cursor()



