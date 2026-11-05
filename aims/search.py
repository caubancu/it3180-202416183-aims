from aims.dvd import DigitalVideoDisc


def search_by_category(items: list[DigitalVideoDisc], category: str) -> list[DigitalVideoDisc]:
    return [dvd for dvd in items if dvd.category.casefold() == category.casefold()]


undefined