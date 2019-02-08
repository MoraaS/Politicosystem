from test.v1.basetest import BaseTestCase
import json


class TestPartyTest(BaseTestCase):
    def test_create_office(self):
        data = {
            "name": "MCA",
            "office_type": "Local Government",
        }
        response = self.post('/api/v1/offices', data=data)
        self.assertEqual(response.status_code, 201)

    def test_party_with_empty_fields(self):
        data = {"name": "governor"
                }
        response = self.post('/api/v1/offices', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data),
                         {
            "status": 400,
            "error": "Not all fields are provided"
        })

    def test_get_all_offices(self):
        response = self.get('api/v1/offices')
        self.assertEqual(response.status_code, 200)

    def test_get_office_by_id(self):
        response = self.get('api/v1/offices/2')
        self.assertEqual(response.status_code, 200)

    def test_get_office_non_existent_id(self):
        response = self.get('api/v1/offices/15')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data),
                         {
            "status": 404,
            "error": "The office does not exist"
        })
