from src.database.sqlite_db_context import SQliteDbContext


class BaseRepository:
    def __init__(self):
        self.__context = SQliteDbContext()

    def create_table(self, table: str, columns: str):
        sql = f"CREATE TABLE IF NOT EXISTS {table}({columns})"
        self.__context.cursor.execute(sql)

    def insert(self, sql: str, *args):
        self.__context.cursor.execute(sql, *args)

    def query(self, sql):
        return self.__context.cursor.execute(sql)
