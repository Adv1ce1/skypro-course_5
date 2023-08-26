from database.mixin_db_connection import MixinDBConnection
from database.mixin_table_creation import MixinTableCreation
from database.mixin_vacancy_operations import MixinVacancyOperations
from database.mixin_file_operations import MixinFileOperations
from utils.read_sql_queries import read_sql
import pandas as pd


class DBManager(MixinDBConnection, MixinTableCreation, MixinVacancyOperations, MixinFileOperations):
  
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    def __init__(self) -> None:
        self.connection = None
        self.sql_queries = read_sql()

    def _execute_query(self, query, params=None):
      
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    cursor.execute(query, params)
        except Exception as e:
            print("Ошибка при выполнении запроса:", e)

    def _description_query(self, query, params=None, fetch=False):
       
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                if fetch:
                    result = cursor.fetchall()
                    columns = [desc[0] for desc in cursor.description]
                    return pd.DataFrame(result, columns=columns)
        except Exception as e:
            print("Error executing query:", e)
            return None
