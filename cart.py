MAX_NUMBERS_ORDERED = 20


class Cart:
    """Shopping cart with a maximum of 20 DVDs."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd) -> bool:
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        return True

    def total_cost(self) -> float:
        return sum(dvd.cost for dvd in self.items)
