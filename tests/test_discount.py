import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class DiscountTests(unittest.TestCase):
    def test_discount_returns_payable_total(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD", cost=100.0))
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)

    def test_discount_rejects_invalid_percentage(self):
        cart = Cart()
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()
