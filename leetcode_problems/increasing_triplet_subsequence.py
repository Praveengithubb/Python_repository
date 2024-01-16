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


solution = Solution()
numm = [1, 2, 3, 4, 5]
res = solution.increasingTriplet(numm)
print(res)
