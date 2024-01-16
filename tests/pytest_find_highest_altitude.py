import unittest
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxx = 0
        ress = 0
        i = 0
        for i in range(len(gain)):
            ress += gain[i]
            maxx = max(maxx, ress)
        return maxx


class MyTestCase(unittest.TestCase):
    def test_largestAltitude(self):
        solution = Solution()
        gains = [-4, -3, -2, -1, 4, 3, 2]
        res = solution.largestAltitude(gains)
        self.assertEqual(res, 0)

    def test_largestAltitude1(self):
        solution = Solution()
        gains = [-5, 1, 5, 0, -7]
        res = solution.largestAltitude(gains)
        self.assertEqual(res, 1)


if __name__ == '__main__':
    unittest.main()
