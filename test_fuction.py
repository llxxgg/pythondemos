import unittest
from function import get_formatted_name


class FuctionTestCase(unittest.TestCase):

    def test_get_formatted_name(self):
        formatted_name = get_formatted_name('li', 'chris')
        self.assertEqual(formatted_name, 'Li Chris')


if __name__ == '__main__':
    unittest.main()
