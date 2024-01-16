import unittest
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total_sum = 0

        if len(nums) == 1:
            return nums[0] / k

        for i in range(k):
            total_sum += nums[i]

        max_sum = total_sum
        ans = max_sum / k

        for i in range(k, len(nums)):
            total_sum = total_sum - nums[i - k] + nums[i]
            if total_sum > max_sum:
                max_sum = total_sum
                ans = max_sum / k

        return ans


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution_instance = Solution()
        result = solution_instance.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
        self.assertEqual(result, 12.75)

    def test_something1(self):
        solution_instance = Solution()
        result = solution_instance.findMaxAverage([5], 1)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()