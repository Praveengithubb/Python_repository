from typing import List


class Solution:
    def maxArea(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = 0

        while left < right:
            if nums[left] < nums[right]:
                prod = nums[left] * (right - left)
                if prod > res:
                    res = prod
                left += 1
            else:
                prod = nums[right] * (right - left)
                if prod > res:
                    res = prod
                right -= 1

        return res


solution = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
ress = solution.maxArea(height)
print(ress)
