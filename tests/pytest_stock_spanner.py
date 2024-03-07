import unittest


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            x, s = self.stack.pop()
            span += s
        self.stack.append((price, span))
        return span


class MyTestCase(unittest.TestCase):
    def test_something(self):
        spanner = StockSpanner()
        self.assertEqual(1, spanner.next(100))  # add assertion here
        self.assertEqual(1, spanner.next(80))
        self.assertEqual(1, spanner.next(60))
        self.assertEqual(2, spanner.next(70))
        self.assertEqual(1, spanner.next(60))
        self.assertEqual(4, spanner.next(75))
        self.assertEqual(6, spanner.next(85))


if __name__ == '__main__':
    unittest.main()
