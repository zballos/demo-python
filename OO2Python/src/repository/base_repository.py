from src.database.sqlite_db_context import SQliteDbContext


class BaseRepository:
    def __init__(self):
        self.__context = SQliteDbContext()

    def create_table(self, table: str, columns: str):
        sql = f"CREATE TABLE IF NOT EXISTS {table}({columns})"
        self.__context.execute(sql, None)

    def insert(self, sql: str, **kwargs):
        result = self.__context.execute(sql, **kwargs)
        print(result)
        self.__context.commit()

    def query(self, sql):
        return self.__context.execute(sql)
