import unittest
from app import app


class MainTest(unittest.TestCase):

    def test_transform(self):
        tester = app.test_client(self)
        response = tester.post('/transform', content_type='html/text')
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data, )

if __name__ == '__main__':
    unittest.main()
