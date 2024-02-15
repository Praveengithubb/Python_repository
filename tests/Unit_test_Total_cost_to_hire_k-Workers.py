import heapq
import unittest


class HireKWorker:
    def totalCost(self, cost, k, candidates):
        i = 0
        j = len(cost) - 1
        pq1 = []
        pq2 = []
        ans = 0
        while k > 0:
            while i <= j and len(pq1) < candidates:
                heapq.heappush(pq1, cost[i])
                i += 1
            while j >= i and len(pq2) < candidates:
                heapq.heappush(pq2, cost[j])
                j -= 1
            a = pq1[0] if pq1 else float('inf')
            b = pq2[0] if pq2 else float('inf')
            if a <= b:
                ans += a
                heapq.heappop(pq1)
            else:
                ans += b
                heapq.heappop(pq2)
            k -= 1
        return ans


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = HireKWorker()
        costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
        k = 3
        candidates = 4
        self.assertEqual(11, s.totalCost(costs, k, candidates))  # add assertion here

    def test_something1(self):
        s = HireKWorker()
        costs = [1, 2, 4, 1]
        k = 3
        candidates = 3
        self.assertEqual(4, s.totalCost(costs, k, candidates))  # add assertion here


if __name__ == '__main__':
    unittest.main()
