from app.api.v2.models.dbconfig import Database
import json


class VoteModel(Database):
    def __init__(self, office, candidate, voter):
        super().__init__()

        self.office = office
        self.candidate = candidate
        self.voter = voter

    def create_new_vote(self, office, candidate, voter):
        """
        Add a new vote to the votes table.
        """
        self.curr.execute("""
        INSERT INTO votes(office, candidate, voter) VALUES(
            '{}', '{}', '{}'
        )""".format(office, candidate, voter))
        votes = self.curr.fetchone()
        self.save()
        return votes
