import unittest
from app import create_app

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_ask(self):
        response = self.client.post('/ask', data={'query': 'Quais são os produtos mais populares entre os clientes corporativos?'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('query', response.json)

if __name__ == '__main__':
    unittest.main()
