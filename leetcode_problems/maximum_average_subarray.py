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


solution_instance = Solution()
my_list = [1, 12, -5, -6, 50, 3]
n = 4
result = solution_instance.findMaxAverage(my_list, n)
print(result)
