import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class CartPrintTests(unittest.TestCase):
    def test_print_empty_cart(self):
        self.assertEqual(Cart().print_cart(), "The cart is empty")

    def test_print_populated_cart(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("The Lion King", cost=19.95))
        self.assertIn("The Lion King", cart.print_cart())


if __name__ == "__main__":
    unittest.main()
