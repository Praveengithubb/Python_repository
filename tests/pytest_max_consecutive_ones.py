import unittest
from typing import List


class Solution:
    def longestones(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        zero_count = 0
        max_length = 0
        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_length = max(right - left + 1, max_length)
            right += 1
        return max_length


class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_list = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        n = 2
        solution = Solution()
        self.assertEqual(solution.longestones(my_list, n), 6)

    def test_something1(self):
        my_list = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        n = 3
        solution = Solution()
        self.assertEqual(solution.longestones(my_list, n), 10)

    def test_something2(self):
        my_list = [0, 0, 1, 1, 0, 0, 1]
        n = 2
        solution = Solution()
        self.assertEqual(solution.longestones(my_list, n), 5)


if __name__ == '__main__':
    unittest.main()
