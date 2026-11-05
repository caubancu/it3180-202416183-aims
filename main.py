from cart import Cart
from dvd import DVD


def main():
    cart = Cart()
    for dvd in (
        DVD("The Lion King", 19.99),
        DVD("Finding Nemo", 14.95),
        DVD("Inception", 28.95),
    ):
        cart.add_dvd(dvd)
    print(f"Total cost: {cart.total_cost():.2f} $")


if __name__ == "__main__":
    main()
