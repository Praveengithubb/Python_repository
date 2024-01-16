from typing import List


class Solution:
    @staticmethod
    def maxOperations(nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1
        sum = 0
        result = 0
        while start < end:
            if nums[start] + nums[end] < k:
                start += 1
            elif nums[start] + nums[end] > k:
                end -= 1
            else:
                start += 1
                end -= 1
                result += 1

        return result


solution = Solution()
my_list = [3, 1, 1, 1]
n = 2
res = solution.maxOperations(my_list, n)
print(res)
