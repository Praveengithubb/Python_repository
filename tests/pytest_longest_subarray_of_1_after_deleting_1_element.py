import unittest


class Solution:
    def longestSubarray(self, nums):
        zero_count = 0
        right = 0
        left = 0
        max_length = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left - zero_count + 1)
            right += 1

        if zero_count != 0:
            return max_length
        else:
            return len(nums) - 1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        nums = [1, 1, 0, 1]
        res = solution.longestSubarray(nums)
        exp_res = 3
        self.assertEqual(res, exp_res)

    def test_something1(self):
        solution = Solution()
        nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
        res = solution.longestSubarray(nums)
        exp_res = 5
        self.assertEqual(res, exp_res)

    def test_something2(self):
        solution = Solution()
        nums = [1, 1, 1]
        res = solution.longestSubarray(nums)
        exp_res = 2
        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    unittest.main()
