from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}
        for nums in arr:
            occurences[nums] = occurences.get(nums, 0) + 1
        unique_set = set(occurences.values())
        return len(unique_set) == len(occurences)


solution = Solution()
ar = [1, 2, 2, 1, 1, 3]
res = solution.uniqueOccurrences(ar)
print(res)
