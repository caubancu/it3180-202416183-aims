class DVD:
    """A simple DVD item in the AIMS-mini store."""

    def __init__(self, title: str, cost: float):
        self.title = title
        self.cost = float(cost)

    def __str__(self) -> str:
        return f"{self.title} (${self.cost:.2f})"
