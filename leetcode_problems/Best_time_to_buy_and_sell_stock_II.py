class Stock:
    def maxProfit(self, prices, fee):
        buy = float('-inf')
        sell = 0
        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)
        return sell


s = Stock()
prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(s.maxProfit(prices, fee))
