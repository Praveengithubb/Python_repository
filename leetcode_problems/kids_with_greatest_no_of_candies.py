from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        high = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= high:
                result.append(True)
            else:
                result.append(False)

        return result


solution = Solution()
candies = [2, 3, 5, 1, 3]
extraCandies = 3
res = solution.kidsWithCandies(candies,extraCandies)
print(res)
