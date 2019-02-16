'''psycopg is a database adapter it helps
create a connection using a cursor. . Extras is a library in psycopg
that converts lists to dictionaries'''
from psycopg2.extras import RealDictCursor
import psycopg2
import os


# conn_url = "dbname = 'postgres' host = 'localhost' port = '5432' password = 'postgres'"
# url = os.getenv(['DB_URL'])
# test_url=os.getenv(['TEST_DB_URL'])


class Database:
    '''Base class to setup DB'''

    def __init__(self):
        self.db_url = os.getenv('DB_URL')
        # self.db_host = os.getenv('DB_HOST')
        # self.db_user = os.getenv('DB_USER')
        # self.db_password = os.getenv('DB_PASSWORD')
        self.conn = psycopg2.connect(database=self.db_url)
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)

    def save(self):
        self.conn.commit()
        self.curr.close()

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
        );""",
            """CREATE TABLE IF NOT EXISTS office (
               id serial PRIMARY KEY NOT NULL,
               name VARCHAR (50) NOT NULL,
               office_type VARCHAR (50) NOT NULL
           );"""
        ]
        try:
            for query in queries:
                self.curr.execute(query)
            self.save()
        except Exception as e:
            print(e)
            return e

    def destroy_tables(self):
        users = "DROP TABLE IF EXISTS users CASCADE"
        office = "DROP TABLE IF EXISTS office CASCADE"
        queries = [users, office]
        try:
            for query in queries:
                self.curr.execute(query)
            self.save()
        except Exception as e:
            print(e)
            return e

    # def select_data_from_database(query):
    #     """Handles select query"""
    # rows = None
    # conn, cursor = connect_to_db(query)
    # if conn:

    #     rows = cursor.fetchall()
    #     conn.close()

    # return rows

    # def query_data_from_db(query)
    # try:
    #     conn = connect_to_db(query)
    #     conn.close()
    #     except psycopg2.error as error:
    #         sys.exit(1)
