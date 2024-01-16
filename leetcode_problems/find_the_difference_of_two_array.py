from typing import List


from typing import List


class Solution:

    def find_difference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        set1 = set(nums1)
        set2 = set(nums2)

        difference1 = list(set1-set2)
        difference2 = list(set2-set1)

        res.append(difference1)
        res.append(difference2)

        return res


solution = Solution()
num1 = [1, 2, 3]
num2 = [2, 4, 6]
res = solution.find_difference(num1, num2)
print(res)
