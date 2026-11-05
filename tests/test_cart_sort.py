import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class CartSortTests(unittest.TestCase):
    def test_sort_by_title(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Zulu", cost=20.0))
        cart.add_dvd(DigitalVideoDisc("alpha", cost=10.0))
        self.assertEqual([d.title for d in cart.sort_by_title()], ["alpha", "Zulu"])

    def test_sort_by_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Expensive", cost=20.0))
        cart.add_dvd(DigitalVideoDisc("Cheap", cost=10.0))
        self.assertEqual([d.cost for d in cart.sort_by_cost()], [10.0, 20.0])


if __name__ == "__main__":
    unittest.main()
