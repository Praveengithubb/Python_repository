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


my_list = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
n = 2

solution_instance = Solution()
result = solution_instance.longestones(my_list, n)
print(result)
