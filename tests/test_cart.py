import unittest

from aims.cart import MAX_NUMBERS_ORDERED, Cart
from aims.dvd import DigitalVideoDisc


class CartLimitTests(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for index in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(str(index))))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("21st DVD")))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)


if __name__ == "__main__":
    unittest.main()
