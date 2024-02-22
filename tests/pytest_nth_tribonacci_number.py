import unittest


class tribonacciNumber:

    def tribonacci(self, n):
        s1, s2, s3 = 0, 1, 1
        if n == 0:
            return s1
        if n == 1:
            return s2
        if n == 2:
            return s3
        a = 3
        while a <= n:
            ans = s1 + s2 + s3
            s1, s2, s3 = s2, s3, ans
            a += 1
        return ans


class MyTestCase(unittest.TestCase):
    def test_something(self):
        t = tribonacciNumber()
        n = 4
        self.assertEqual(4, t.tribonacci(n))  # add assertion here

    def test_something1(self):
        t = tribonacciNumber()
        n = 25
        self.assertEqual(1389537, t.tribonacci(n))  # add assertion here


if __name__ == '__main__':
    unittest.main()
