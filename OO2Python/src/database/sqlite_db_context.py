import sqlite3


class SQliteDbContext:
    def __init__(self):
        self.__db = sqlite3.connect("local.db")

    def execute(self, *sql: str, **kwargs):
        cursor = self.__db.cursor()
        return cursor.execute(*sql, **kwargs)

    def execute_many(self, sql: str, data: [dict]):
        cursor = self.__db.cursor()
        return cursor.executemany(sql, data)

    def commit(self):
        self.__db.commit()


