from test.v1.basetest import BaseTestCase
import json


class TestPartyCase(BaseTestCase):
    
    def test_create_party(self):
        data = {
            "name": "Wipper",
            "hqaddress": "Kitui",
            "logourl": "http://sample._url"
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

    def test_create_with_empty_name(self):
        data = {
            "name": "",
            "hqaddress": "Nairobi",
            "logourl": "http://sample._url"
        }
        response = self.post('/api/v1/parties', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data),
                         {
            "status": 400,
            "error": "Name cant be left blank"
        })

    def test_create_with_empty_hqAddress(self):
        data = {
            "name": "Wipper",
            "hqaddress": "",
            "logourl": "sample.com"
        }
        response = self.post('/api/v1/parties', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data),
                         {
            "status": 400,
            "error": "hqaddress cant be blank"
        })

    def test_create_with_empty_logoUrl(self):
        data = {
            "name": "Wipper",
            "hqaddress": "Kitui",
            "logourl": ""
        }
        response = self.post('/api/v1/parties', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data),
                         {
            "status": 400,
            "error": "logourl cant be blank"
        })

    def test_create_with_short_name(self):
        data = {
            "name": "Wip",
            "hqaddress": "Nairobi",
            "logourl": "http://sample._url"
        }
        response = self.post('/api/v1/parties', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data),
                         {
            "status": 400,
            "error": "Name cannot be less than 6 characters"
        })

    def test_get_all_parties(self):
        response = self.get('/api/v1/parties')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_party(self):
        data = {
            "name": "Future Tomorrow",
            "hqaddress": "Kitui",
            "logourl": "http://sample._url"
        }
        self.post('/api/v1/parties', data=data)
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

    def test_delete_party(self):
        response = self.delete('/api/v1/parties/1')
        self.assertEqual(response.status_code, 200)
