import unittest
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


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        gridd = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
        res = solution.equalPairs(gridd)
        self.assertEqual(res, 1)

    def test_something1(self):
        solution = Solution()
        gridd = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
        res = solution.equalPairs(gridd)
        self.assertEqual(res, 3)

    def test_something2(self):
        solution = Solution()
        gridd = [[13, 13], [13, 13]]
        res = solution.equalPairs(gridd)
        self.assertEqual(res, 4)


if __name__ == '__main__':
    unittest.main()
