from database import Database
import unittest


class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        Database.initialize()

    def test_insert_data(self):
        data = {
            'name': 'samuel',
            'age': '20'
        }

        status = Database.insert(collection="test", data=data)
        self.assertEqual('ok', status)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
