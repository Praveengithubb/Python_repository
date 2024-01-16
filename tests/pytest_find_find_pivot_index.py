import unittest
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        rightsum = 0
        for i in range(len(nums)):
            rightsum += nums[i]
        for i in range(len(nums)):
            rightsum -= nums[i]
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1


class MyTestCase(unittest.TestCase):
    def test_pivotIndex(self):
        solution = Solution()
        num = [1, 7, 3, 6, 5, 6]
        res = solution.pivotIndex(num)
        self.assertEqual(res, 3)

    def test_pivotIndex1(self):
        solution = Solution()
        num = [1, 2, 3]
        res = solution.pivotIndex(num)
        self.assertEqual(res, -1)

    def test_pivotIndex2(self):
        solution = Solution()
        num = [2, 1, -1]
        res = solution.pivotIndex(num)
        self.assertEqual(res, -0)


if __name__ == '__main__':
    unittest.main()
