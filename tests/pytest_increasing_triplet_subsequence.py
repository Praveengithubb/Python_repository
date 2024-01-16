import unittest
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if nums is None or len(nums) < 0:
            return False

        a = float('inf')
        b = float('inf')
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True

        return False


class MyTestCase(unittest.TestCase):
    def test_increasingTriplet(self):
        solution = Solution()
        numm = [1, 2, 3, 4, 5]
        self.assertTrue(solution.increasingTriplet(numm))

    def test_increasingTriplet1(self):
        solution = Solution()
        numm = [5, 4, 3, 2, 1]
        self.assertFalse(solution.increasingTriplet(numm))

    def test_increasingTriplet2(self):
        solution = Solution()
        numm = [2, 1, 5, 0, 4, 6]
        self.assertTrue(solution.increasingTriplet(numm))


if __name__ == '__main__':
    unittest.main()
