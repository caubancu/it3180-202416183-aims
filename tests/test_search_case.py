import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchCaseTests(unittest.TestCase):
    def test_title_search_is_case_insensitive(self):
        items = [DigitalVideoDisc("The Lion King", cost=19.95)]
        self.assertEqual(search_by_title(items, "lion"), items)


if __name__ == "__main__":
    unittest.main()
