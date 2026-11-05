import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class CategorySearchTests(unittest.TestCase):
    def test_category_search_is_case_insensitive(self):
        items = [DigitalVideoDisc("The Lion King", "Animation", 19.95)]
        self.assertEqual(search_by_category(items, "animation"), items)


if __name__ == "__main__":
    unittest.main()
