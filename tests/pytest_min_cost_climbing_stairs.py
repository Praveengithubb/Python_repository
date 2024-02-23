import unittest


class MinCostClimbingStairs:
    def minCostClimbingStairs(self, cost):
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[-2], dp[-1])


class MyTestCase(unittest.TestCase):
    def test_something(self):
        m = MinCostClimbingStairs()
        cost = [10, 15, 20]
        self.assertEqual(15, m.minCostClimbingStairs(cost))  # add assertion here

    def test_something1(self):
        m = MinCostClimbingStairs()
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        self.assertEqual(6, m.minCostClimbingStairs(cost))


if __name__ == '__main__':
    unittest.main()
