"""importing modules to be used in the vote model queries"""
import json
from psycopg2.extras import RealDictCursor
from app.api.v2.models.dbconfig import Database


class VoteModel(Database):
    """Base class for all votemodel methods"""

    def __init__(self, createdby=None, office_id=None, candidate_id=None):
        super().__init__()

        self.createdby = createdby
        self.office_id = office_id
        self.candidate_id = candidate_id

    def create_new_vote(self, createdby=None, office_id=None, candidate_id=None):
        """Add a new vote to the voters table."""
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        new_vote = """INSERT INTO voters(createdby, office_id, candidate_id) VALUES('{}', '{}', '{}') RETURNING createdby, office_id, candidate_id
            """.format(createdby, office_id, candidate_id)
        return Database().query_data(new_vote)

    def check_if_voter_voted(self, createdby, office_id):
        """checks if voter voted in the voters table"""
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        check_vote = """SELECT * FROM voters WHERE createdby = '{}' AND office_id = '{}'""".format(createdby, office_id)
        return Database().query_data(check_vote)

    def get_results_by_office_id(self, office_id):
        """gets vote results from the vote table using office id"""
        self.curr.execute("""
        SELECT office_id, candidate_id, count(createdby) as result
        FROM voters WHERE office_id= {} GROUP BY office_id, candidate_id""".format(office_id))
        results = self.curr.fetchall()
        self.save()
        return results
