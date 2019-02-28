import os
import json
import unittest
import datetime
import jwt
from test.v2.basetest import BaseTestCase
from app import create_app


class TestParties(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.parties_data2 = {
            "name": "jubilee",
            "hqaddress": "Nairobi",
            "logourl": "photo.com"
        }

    def test_create_party(self):
        response = self.create_party(self.parties_data)

        self.assertEqual(response.status_code, 201)

    def test_create_party_with_short_name(self):
        """ test for creating an party with a short name"""
        office = {
            "name": "off",
            "hqaddress": "Nairobi",
            "logourl": "logourl"
        }
        response = self.create_office(office)
        self.assertEqual(response.status_code, 400)

    def test_create_party_with_numbers(self):
        """ test for creating an party that contains a number"""
        office = {
            "name": "party123",
            "hqaddress": "Nairobi",
            "logourl": "logourl"
        }
        response = self.create_office(office)
        self.assertEqual(response.status_code, 400)

    def test_create_existing_party(self):
        """ test for creating an existing office"""
        self.create_party(self.parties_data)
        response = self.create_party(self.parties_data)
        self.assertEqual(response.status_code, 400)

    # def test_get_specific_party(self):
    #     party = self.create_party(self.parties_data)
    #     party_id = party.json[0][1]['party_id']
    #     print(party_id)
    #     response = self.get("api/v2/parties/{}".format(party_id))
    #     self.assertEqual(response.status_code, 200)

    def test_get_all_parties(self):
        self.create_party(self.parties_data)
        self.create_party(self.parties_data2)
        response = self.get("api/v2/parties")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['parties']), 2)
