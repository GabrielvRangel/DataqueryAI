import unittest
from app.services.database import generate_sql, execute_query

class ServicesTestCase(unittest.TestCase):
    def test_generate_sql(self):
        query = 'Quais são os produtos mais populares entre os clientes corporativos?'
        sql_query = generate_sql(query)
        self.assertIn('SELECT', sql_query.upper())

    def test_execute_query(self):
        sql_query = 'SELECT * FROM customers LIMIT 1'
        result = execute_query(sql_query)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
