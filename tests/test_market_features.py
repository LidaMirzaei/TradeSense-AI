import unittest
from src.market_features import TopOfBook, spread, mid_price, queue_imbalance

class MarketFeaturesTests(unittest.TestCase):
    def test_example(self):
        book = TopOfBook(100, 100.02, 800, 500)
        self.assertAlmostEqual(spread(book), 0.02)
        self.assertAlmostEqual(mid_price(book), 100.01)
        self.assertAlmostEqual(queue_imbalance(book), 300 / 1300)

    def test_balanced(self):
        book = TopOfBook(10, 10, 100, 100)
        self.assertEqual(spread(book), 0)
        self.assertEqual(queue_imbalance(book), 0)

    def test_invalid_quote(self):
        with self.assertRaises(ValueError):
            TopOfBook(101, 100, 1, 1)

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            TopOfBook(99, 100, -1, 10)

    def test_empty_book(self):
        with self.assertRaises(ValueError):
            TopOfBook(99, 100, 0, 0)

    def test_invalid_prices(self):
        with self.assertRaises(ValueError):
            TopOfBook(0, 100, 1, 1)

if __name__ == "__main__":
    unittest.main()
