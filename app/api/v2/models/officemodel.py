from app.api.v2.models.dbconfig import Database
import json
from psycopg2.extras import RealDictCursor


class OfficeModel(Database):
    '''Base class for all methods of offices'''

    def __init__(self, name=None, office_type=None):
        super().__init__()
        '''Defining the constructor method of the class
        and self is the instance of the object'''
        self.name = name
        self.office_type = office_type

    def create(self, name, office_type):
        """create office admin only function"""
        query = '''
        INSERT INTO office(name, office_type) VALUES
        ('{}','{}') RETURNING name, office_type'''.format(name, office_type)
        return Database().query_data(query)

    def get_all_offices(self):
        """
            method to get all offices from db.
        """
        query = """ SELECT office_id, name,office_type FROM office"""
        offices = Database().fetch(query)
        return json.dumps(offices, default=str)

    def get_by_id(self, office_id):
        '''Defining method to get
        office by id, and passing parameters to it.'''
        self.curr.execute(
            """SELECT * FROM office WHERE office_id={}""".format(office_id))
        offices = self.curr.fetchone()
        self.save()
        return json.dumps(offices, default=str)

    def get_office_by_name(self, name):
        """Retrieve office with specific name."""
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        self.curr.execute(
            """ SELECT * FROM office WHERE office.name = '{}';""".format(name))
        office_name = self.curr.fetchone()
        self.save()
        return office_name
