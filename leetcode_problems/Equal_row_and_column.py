from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pair = 0
        row = 0
        temp = 0
        while temp < len(grid):
            gridmap = {}
            for i in range(len(grid)):
                gridmap[i] = grid[row][i]
            for i in range(len(grid)):
                curr = 0
                for k in range(len(grid)):
                    if gridmap[k] != grid[k][i]:
                        curr = 0
                        break
                    else:
                        curr = 1

                pair += curr
            row += 1
            temp += 1
        return pair


solution = Solution()
gridd = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
res = solution.equalPairs(gridd)
print(res)
