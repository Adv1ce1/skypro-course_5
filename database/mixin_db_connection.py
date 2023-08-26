import psycopg2

from config import DB_CONNECTION_STRING


class MixinDBConnection:
  
    def connect(self) -> None:
        try:
            self.connection = psycopg2.connect(DB_CONNECTION_STRING)
            print("Connected to the database.")
        except Exception as e:
            print("Error connecting to the database:", e)

    def disconnect(self) -> None:
        if self.connection:
            self.connection.close()
            print("Disconnected from the database.")
