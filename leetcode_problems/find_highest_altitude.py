from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxx = 0
        ress = 0
        i = 0
        for i in range(len(gain)):
            ress += gain[i]
            maxx = max(maxx, ress)
        return maxx


solution = Solution()
gains = [-5, 1, 5, 0, -7]
res = solution.largestAltitude(gains)
print(res)
