import unittest
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left = 1
        right = 1
        for i in range(len(nums)):
            res[i] = left
            left = left * nums[i]
        a = len(nums) - 1
        for a in range(len(nums) - 1, -1, -1):
            res[a] = res[a] * right
            right = right * nums[a]
        return res


class MyTestCase(unittest.TestCase):
    def test_productExceptSelf(self):
        solution = Solution()
        nums = [1, 2, 3, 4]
        res = solution.productExceptSelf(nums)
        expected_result = [24, 12, 8, 6]
        self.assertEqual(res, expected_result)

    def test_productExceptSelf1(self):
        solution = Solution()
        nums = [-1, 1, 0, -3, 3]
        res = solution.productExceptSelf(nums)
        expected_result = [0, 0, 9, 0, 0]
        self.assertEqual(res, expected_result)

    def test_productExceptSelf2(self):
        solution = Solution()
        nums = [-5, -1, 0, 0]
        res = solution.productExceptSelf(nums)
        expected_result = [0, 0, 0, 0]
        self.assertEqual(res, expected_result)


if __name__ == '__main__':
    unittest.main()
