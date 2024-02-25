import unittest


class Domino:
    def numTilings(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        arr = [0] * (n + 1)
        arr[1] = 1
        arr[2] = 2
        arr[3] = 5
        md = 1000000007
        for i in range(4, n + 1):
            arr[i] = ((2 * arr[i - 1]) % md + arr[i - 3]) % md
        return arr[n]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        d = Domino()
        n = 3
        result = d.numTilings(n)
        self.assertEqual(5, result)  # add assertion here

    def test_something1(self):
        d = Domino()
        n = 1
        result = d.numTilings(n)
        self.assertEqual(1, result)


if __name__ == '__main__':
    unittest.main()
