'''psycopg is a database adapter it helps
create a connection using a cursor. . Extras is a library in psycopg
that converts lists to dictionaries'''
from datetime import datetime
from psycopg2.extras import RealDictCursor
import psycopg2
import os
from sys import modules


class Database:
    '''Base class to setup DB'''

    def __init__(self):
        if 'pytest' in modules:
            self.db_name = os.getenv('DB_TEST_NAME')
            self.db_host = os.getenv('DB_TEST_HOST')
            self.db_user = os.getenv('DB_TEST_USER')
            self.db_password = os.getenv('DB_TEST_PASSWORD')
        else:
            self.db_name = os.getenv('DB_NAME')
            self.db_host = os.getenv('DB_HOST')
            self.db_user = os.getenv('DB_USER')
            self.db_password = os.getenv('DB_PASSWORD')

        self.conn = psycopg2.connect(database=self.db_name, host=self.db_host,
                                     user=self.db_user,
                                     password=self.db_password)
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)

    def save(self):
        self.conn.commit()
        self.curr.close()

    def query_data(self, query):
        self.curr.execute(query)
        data = self.curr.fetchone()
        self.save()
        return data
        

    def create_tables(self):
        queries = [
            """
             CREATE TABLE IF NOT EXISTS users(
                user_id serial PRIMARY KEY NOT NULL,
                firstname VARCHAR (24) NOT NULL,
                lastname VARCHAR (24) NOT NULL,
                othername VARCHAR (24),
                email VARCHAR (30) NOT NULL UNIQUE,
                phonenumber VARCHAR (30) NOT NULL,
                password VARCHAR (128) NOT NULL,
                passportUrl VARCHAR (200),
                isAdmin BOOLEAN DEFAULT FALSE
        );""",
            """CREATE TABLE IF NOT EXISTS office (
               office_id serial PRIMARY KEY NOT NULL,
               name VARCHAR (50) NOT NULL,
               office_type VARCHAR (50) NOT NULL
           );""",
            """CREATE TABLE IF NOT EXISTS voters (
               voter_id serial PRIMARY KEY NOT NULL,
               createdOn TIMESTAMP NULL DEFAULT NOW(),
               createdBy INTEGER NOT NULL,
               office_id INTEGER,
               candidate_id INTEGER
           );""",
            """CREATE TABLE IF NOT EXISTS parties(
                party_id SERIAL PRIMARY KEY NOT NULL,
                name VARCHAR(50) NOT NULL,
                hqaddress VARCHAR(50) NOT NULL,
                logourl VARCHAR(50) NOT NULL
            );""",
            """CREATE TABLE IF NOT EXISTS candidates(
                id SERIAL PRIMARY KEY NOT NULL,
                office_id INTEGER NOT NULL,
                party_id INTEGER NOT NULL,
                candidate_id INTEGER NOT NULL
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
        voters = "DROP TABLE IF EXISTS voters CASCADE"
        parties = "DROP TABLE IF EXISTS parties CASCADE"
        candidates = "DROP TABLE IF EXISTS candidates CASCADE"
        queries = [users, office, voters, parties, candidates]
        try:
            for query in queries:
                self.curr.execute(query)
            self.save()
        except Exception as e:
            print(e)
            return e
