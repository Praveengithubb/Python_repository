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


solution = Solution()
nums = [1, 2, 3, 4]
res = solution.productExceptSelf(nums)
print(res)
