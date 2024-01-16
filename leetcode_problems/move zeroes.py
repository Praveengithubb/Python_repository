import unittest
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break
        if j != -1:

            a = j + 1
            for a in range(len(nums)):
                if nums[a] != 0:
                    nums[j] = nums[a]
                    nums[a] = 0
                    j += 1


class MyTestCase(unittest.TestCase):
    def test_moveZeroes(self):
        solution = Solution()
        nums = [0, 1, 0, 3, 12]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

        nums = [0]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [0])


if __name__ == '__main__':
    unittest.main()
