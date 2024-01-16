import unittest
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        high = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= high:
                result.append(True)
            else:
                result.append(False)

        return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        candies = [2, 3, 5, 1, 3]
        extraCandies = 3
        res = solution.kidsWithCandies(candies, extraCandies)
        expected_result = [True, True, True, False, True]
        self.assertEqual(res, expected_result)

    def test_something1(self):
        solution = Solution()
        candies = [12, 1, 12]
        extraCandies = 10
        res = solution.kidsWithCandies(candies, extraCandies)
        expected_result = [True, False, True]
        self.assertEqual(res, expected_result)

    def test_something2(self):
        solution = Solution()
        candies = [4, 2, 1, 1, 2]
        extraCandies = 1
        res = solution.kidsWithCandies(candies, extraCandies)
        expected_result = [True, False, False, False, False]
        self.assertEqual(res, expected_result)


if __name__ == '__main__':
    unittest.main()
