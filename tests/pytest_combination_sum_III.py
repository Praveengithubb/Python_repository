import unittest


class CombinationSumIII:
    @staticmethod
    def combinationSum3(k, n):
        combinations = []
        CombinationSumIII.backtracking(combinations, [], k, n, 1)
        return combinations

    @staticmethod
    def backtracking(result, current, k, n, start):
        if len(current) == k and n == 0:
            result.append(list(current))
            return
        for i in range(start, 10):
            current.append(i)
            CombinationSumIII.backtracking(result, current, k, n - i, i + 1)
            current.pop()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        c = CombinationSumIII
        k = 3
        n = 7
        res = c.combinationSum3(k, n)
        expected = [[1, 2, 4]]
        self.assertEqual(expected, res)

    def test_something1(self):
        c = CombinationSumIII
        k = 4
        n = 1
        res = c.combinationSum3(k, n)
        expected = []
        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()
