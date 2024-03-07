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


spanner = StockSpanner()
print(spanner.next(100))
print(spanner.next(80))
print(spanner.next(60))
print(spanner.next(70))
print(spanner.next(60))
print(spanner.next(75))
print(spanner.next(85))
