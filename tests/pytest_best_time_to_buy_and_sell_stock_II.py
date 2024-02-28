import unittest


class Stock:
    def maxProfit(self, prices, fee):
        buy = float('-inf')
        sell = 0
        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)
        return sell


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Stock()
        prices = [1, 3, 2, 8, 4, 9]
        fee = 2
        self.assertEqual(8, s.maxProfit(prices, fee))  # add assertion here

    def test_something1(self):
        s = Stock()
        prices = [1, 3, 7, 5, 10, 3]
        fee = 3
        self.assertEqual(6, s.maxProfit(prices, fee))


if __name__ == '__main__':
    unittest.main()
