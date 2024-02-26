import unittest


class UniquePath:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        u = UniquePath()
        m = 3
        n = 7
        self.assertEqual(28, u.uniquePaths(m, n))

    def test_something1(self):
        u = UniquePath()
        m = 3
        n = 2
        self.assertEqual(3, u.uniquePaths(m, n))


if __name__ == '__main__':
    unittest.main()
