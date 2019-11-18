import unittest


class MainTest(unittest.TestCase):
    def setUp(self):
        self.data = "fake data"

    def test_given_none_when_assert_then_true(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
