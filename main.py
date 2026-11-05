from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


def main() -> None:
    cart = Cart()
    for dvd in (
        DigitalVideoDisc("The Lion King", cost=19.95),
        DigitalVideoDisc("Finding Nemo", cost=24.99),
        DigitalVideoDisc("Inception", cost=18.95),
    ):
        cart.add_dvd(dvd)
    print(cart.print_cart())
    print(f"Total cost: {cart.total_cost():.2f} $")


if __name__ == "__main__":
    main()
