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


solution = Solution()
num = [1, 7, 3, 6, 5, 6]
res = solution.pivotIndex(num)
print(res)
