# import os
# import json
# import unittest
# import datetime
# import jwt
# from test.v2.basetest import BaseTestCase
# from app import create_app


# class TestParties(BaseTestCase):
#     def setUp(self):
#         super().setUp()

#         self.voter_data = {
#             "firstname": "Mary",
#             "lastname": "Jane",
#             "othername": "Donald",
#             "email": "mary@gmail.com",
#             "phonenumber": "0713452678",
#             "password": "Password@123",
#             "passporturl": "passporturl"
#         }
  
#     def test_vote(self):
#         # create office
#         office = self.create_office(self.office_data)
#         print(office.json)
#         office_id = office.json['data'][0]['office_id']
#         # create party
#         party = self.create_party(self.parties_data)
#         print(party.json)
#         party_id = party.json['party'][0]['party_id']
#         # create a candidate
#         cand = self.post("api/v2/auth/signup", data=self.user_data)
#         cand_id = cand.json['data'][0]['user_id']
#         # create candidate
#         self.create_candidate(office_id, party_id, cand_id)
#         # create voter
#         voter = self.post("api/v2/auth/signup", data=self.voter_data)
#         voter_id = voter.json['data'][0]['user_id']

#         data = {
#             "createdby": voter_id,
#             "office_id": office_id,
#             "candidate_id": candidate_id
#         }
#         vote = self.post("api/v2/votes", data=data)
#         print(vote.json)
#         self.assertEqual(vote.status_code, 201)
