from app.api.v2.models.dbconfig import Database
import json
from psycopg2.extras import RealDictCursor


class VoteModel(Database):
    def __init__(self, createdby=None, office_id=None, candidate_id=None):
        super().__init__()

        self.createdby = createdby
        self.office_id = office_id
        self.candidate_id = candidate_id

    def create_new_vote(self, createdby, office_id, candidate_id):
        """
        Add a new vote to the voters table.
        """
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        self.curr.execute("""
        INSERT INTO voters(createdby, office_id, candidate_id) VALUES ('{}', '{}', '{}') RETURNING name, hqaddress, logourl
            """).format(self.createdby, self.office_id, self.candidate_id)
        votes = self.curr.fetchone()
        self.save()
        return votes

    def check_if_voter_voted(self, createdby, office_id):
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        self.curr.execute("""
        SELECT * FROM voters WHERE createdby = '{}' AND office_id = '{}'
        """.format(createdby, office_id))
        voter = self.curr.fetchone()
        self.save()
        return voter

    # def get_results_by_office_id(self, office_id):
    #     self.curr.execute("""
    #     SELECT office, candidate, count(voter) as result
    #     FROM test_votes GROUP BY office, candidate
    #     WHERE office={}
    #     """.format(office))
    #     results = self.curr.fetchall()
    #     self.save()
    #     return results
