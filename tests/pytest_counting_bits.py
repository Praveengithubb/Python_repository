import unittest


class CountingBits:
    def countBits(self, n):
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i // 2] + 1
        return dp


class MyTestCase(unittest.TestCase):

    def test_something(self):
        c = CountingBits()
        self.assertEqual([0, 1, 1, 2, 1, 2], c.countBits(5))  # add assertion here

    def test_something1(self):
        c = CountingBits()
        self.assertEqual([0, 1, 1], c.countBits(2))


if __name__ == '__main__':
    unittest.main()
