"""importing modules to be used in the parties db queries"""
import json
from psycopg2.extras import RealDictCursor
from app.api.v2.models.dbconfig import Database


class PartyModel(Database):
    '''Base class for all methods of offices'''

    def __init__(self, name=None, hqaddress=None, logourl=None):
        super().__init__()
        '''Defining the constructor method of the class
        and self is the instance of the object'''
        self.name = name
        self.hqaddress = hqaddress
        self.logourl = logourl

    def create(self, name, hqaddress, logourl):
        """create party admin only function"""
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        create_party = '''INSERT INTO parties(name, hqaddress, logourl) VALUES('{}','{}','{}')\
            RETURNING name, hqaddress, logourl'''.format(name, hqaddress, logourl)
        return Database().query_data(create_party)

    def get_all_parties(self):
        """ method to get all parties from db."""
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        query = """ SELECT party_id, name, hqaddress, logourl FROM parties"""
        all_parties = Database().fetch(query)
        return json.dumps(all_parties, default=str)

    def get_party_by_name(self, name):
        """Retrieve party with specific name."""
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        party_name = """ SELECT * FROM parties WHERE parties.name = '{}';""".format(name)
        return Database().query_data(party_name)

    def get_party_by_id(self, party_id):
        '''Defining method to get
        party by id, and passing parameters to it.'''
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        query = """SELECT * FROM parties WHERE party_id='{}';""".format(party_id)
        one_party = Database().query_data(query)
        return json.dumps(one_party, default=str)

    def delete_party(self, party_id):
        """Method to delete party"""
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        self.curr.execute(
            """DELETE FROM parties WHERE party_id='{}';""".format(party_id))
        self.conn.commit()
        self.curr.close()

    def update_party(self, name, party_id):
        """Admin can alter name of party."""
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        self.curr.execute(
            """UPDATE parties SET name='{}' WHERE parties.party_id='{}'; """.format(name, party_id
                                                                                    ))
        self.conn.commit()
        self.curr.close()
