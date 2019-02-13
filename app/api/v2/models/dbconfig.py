'''psycopg is a database adapter it helps
create a connection using a cursor. . Extras is a library in psycopg
that converts lists to dictionaries'''
from psycopg2.extras import RealDictCursor
import psycopg2
import os


class Database:
    '''Base class to setup DB'''

    def __init__(self):
        self.db_name = os.getenv('DB_NAME')
        self.db_host = os.getenv('DB_HOST')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.conn = psycopg2.connect(database=self.db_name, host=self.db_host,
                                     user=self.db_user,
                                     password=self.db_password)
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)

    def create_tables(self):
        queries = [
            """
             CREATE TABLE IF NOT EXISTS users(
                firstname VARCHAR (24) NOT NULL,
                lastname VARCHAR (24) NOT NULL,
                othername VARCHAR (24),
                email VARCHAR (30) NOT NULL UNIQUE,
                password VARCHAR (128) NOT NULL,
                passportUrl VARCHAR (200)
        )"""
        ]
        try:
            for query in queries:
                self.curr.execute(query)
            self.conn.commit()
            self.curr.close()
        except Exception as e:
            return e

    def destroy_tables(self):
        users = "DROP TABLE IF EXISTS users CASCADE"
        queries = [users]
        try:
            for query in queries:
                self.curr.execute(query)
            self.conn.commit()
            self.curr.close()
        except Exception as e:
            return e
