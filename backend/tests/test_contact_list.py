import json
from falcon import testing
from contacts.app import api


class ContactListTests(testing.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = testing.TestClient(api)

    def test_get_contact_list(self):
        cl = {
            'name': 'A contact list',
            'contacts': []
        }
        response = self.client.simulate_get('/contact')
        result = json.loads(response.content)
        self.assertEqual(cl, result)
