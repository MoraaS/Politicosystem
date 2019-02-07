from test.v1.base_test import BaseTestCase
import json

class TestPartyCase(BaseTestCase):
    def test_create_party(self):
        data = {
            "name": "Wiper",
            "hqAddress": "Kitui",
            "logoUrl": "http://sample._url"
        }
        response = self.post('/api/v1/parties', data=data)
        self.assertEqual(response.status_code, 201)
    def test_create_party_with_empty_data(self):
        data = {
        }
        response = self.post('/api/v1/parties', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data),
        {
            "status": 400,
            "error": "You have not provided all the fields"
        })
        

