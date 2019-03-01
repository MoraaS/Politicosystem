"""import modules to be used in the office model"""
import json
from psycopg2.extras import RealDictCursor
from app.api.v2.models.dbconfig import Database


class OfficeModel(Database):
    '''Base class for all methods of offices'''

    def __init__(self, name=None, office_type=None):
        super().__init__()
        self.name = name
        self.office_type = office_type

    def create(self, name, office_type):
        """create office admin only function"""
        query = '''
        INSERT INTO office(name, office_type) VALUES
        ('{}','{}') RETURNING name, office_type'''.format(name, office_type)
        return Database().query_data(query)

    def get_all_offices(self):
        """method to get all offices from db."""
        query = """ SELECT office_id, name,office_type FROM office"""
        offices = Database().fetch(query)
        return json.dumps(offices, default=str)

    def get_by_id(self, office_id):
        '''Defining method to get office by id'''
        query = """SELECT * FROM office WHERE office_id={}""".format(office_id)
        office_id = Database().query_data(query)
        return json.dumps(office_id, default=str)

    def get_office_by_name(self, name):
        """Retrieve office with specific name."""
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        query = """ SELECT * FROM office WHERE office.name = '{}';""".format(name)
        return Database().query_data(query)
