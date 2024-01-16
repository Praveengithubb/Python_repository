import unittest
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}
        for nums in arr:
            occurences[nums] = occurences.get(nums, 0) + 1
        unique_set = set(occurences.values())
        return len(unique_set) == len(occurences)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        ar = [1, 2, 2, 1, 1, 3]
        res = solution.uniqueOccurrences(ar)
        self.assertEqual(res, True)  # add assertion here

    def test_something1(self):
        solution = Solution()
        ar = [1, 2]
        res = solution.uniqueOccurrences(ar)
        self.assertEqual(res, False)

    def test_something2(self):
        solution = Solution()
        ar = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
        res = solution.uniqueOccurrences(ar)
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
