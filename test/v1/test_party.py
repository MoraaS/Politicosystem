from test.v1.basetest import BaseTestCase
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
        data = {}
        response = self.post('/api/v1/parties', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data),
                         {
            "status": 400,
            "error": "You have not provided all the fields"
        })

    def test_get_all_parties(self):
        response = self.get('/api/v1/parties')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_party(self):
        response = self.get('/api/v1/parties/1')
        self.assertEqual(response.status_code, 200)

    def test_non_existent_party(self):
        response = self.get('/api/v1/parties/100')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data),
                         {
            "status": 404,
            "error": "The party does not exist"
        })
    
