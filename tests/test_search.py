import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchTests(unittest.TestCase):
    def test_search_by_title(self):
        items = [DigitalVideoDisc("The Lion King", cost=19.95)]
        self.assertEqual(search_by_title(items, "Lion"), items)
        self.assertEqual(search_by_title(items, "Star Wars"), [])


if __name__ == "__main__":
    unittest.main()
