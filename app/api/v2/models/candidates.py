from app.api.v2.models.dbconfig import Database
import json



class CandidatesModel(Database):
    '''Base class for all methods of candidates'''

    def __init__(self, office_id=None, party_id=None, candidate_id=None):
        super().__init__()
        '''Defining the constructor method of the class
        and self is the instance of the object'''
        self.office_id = office_id
        self.party_id = party_id
        self.candidate_id = candidate_id

    def create(self, office_id, party_id, candidate_id):
        """create candidate admin only function"""
        self.curr.execute(
            '''
        INSERT INTO candidates(office_id, party_id, candidate_id) VALUES
        ('{}','{}','{}') RETURNING office_id, party_id, candidate_id'''
            .format(office_id, party_id, candidate_id))
        new_candidate = self.curr.fetchone()
        self.save()
        return new_candidate

    def get_all_candidates(self):
        """
            method to get all candidates from db.
        """
        self.curr.execute(
            """
        SELECT office, candidate FROM candidates
        """)
        candidates = self.curr.fetchall()
        self.save()
        return json.dumps(candidates, default=str)

    def get_by_id(self, candidate_id):
        '''Defining method to get
        candidate by user id'''
        self.curr.execute(
            """SELECT * FROM candidates WHERE\
                candidate_id={}""".format(candidate_id))
        candidate = self.curr.fetchone()
        self.save()
        return candidate
