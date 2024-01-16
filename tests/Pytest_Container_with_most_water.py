import unittest


class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            result = max(result, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        res = solution.maxArea(height)
        exp_res = 49
        self.assertEqual(res, exp_res)

    def test_something1(self):
        solution = Solution()
        height = [1, 1]
        res = solution.maxArea(height)
        exp_res = 1
        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    unittest.main()
