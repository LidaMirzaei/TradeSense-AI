"""Top-of-book features for the first learning milestone."""
from dataclasses import dataclass

@dataclass(frozen=True)
class TopOfBook:
    bid_price: float
    ask_price: float
    bid_size: float
    ask_size: float

    def __post_init__(self):
        if self.bid_price <= 0 or self.ask_price <= 0:
            raise ValueError("Prices must be positive")
        if self.bid_price > self.ask_price:
            raise ValueError("Bid price must not exceed ask price")
        if self.bid_size < 0 or self.ask_size < 0:
            raise ValueError("Sizes cannot be negative")
        if self.bid_size + self.ask_size == 0:
            raise ValueError("At least one displayed size must be positive")

def spread(book: TopOfBook) -> float:
    """Quoted spread (ask minus bid), in price units."""
    return book.ask_price - book.bid_price

def mid_price(book: TopOfBook) -> float:
    """Arithmetic midpoint of best bid and ask."""
    return (book.bid_price + book.ask_price) / 2

def queue_imbalance(book: TopOfBook) -> float:
    """Displayed best-level size imbalance in [-1, 1]; not a forecast."""
    return (book.bid_size - book.ask_size) / (book.bid_size + book.ask_size)

if __name__ == "__main__":
    example = TopOfBook(100.00, 100.02, 800, 500)
    print(f"Spread: {spread(example):.4f}")
    print(f"Mid-price: {mid_price(example):.4f}")
    print(f"Queue imbalance: {queue_imbalance(example):.4f}")
