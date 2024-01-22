import unittest
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = deque()
        dir = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == 'R':
                rad.append(i)
            else:
                dir.append(i)
        while rad and dir:
            if rad[0] < dir[0]:
                rad.append(n)
            else:
                dir.append(n)
            rad.popleft()
            dir.popleft()
            n += 1
        return "Dire" if not rad else "Radiant"


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        senate = "RD"
        res = solution.predictPartyVictory(senate)
        self.assertEqual("Radiant", res)

    def test_something1(self):
        solution = Solution()
        senate = "RDD"
        res = solution.predictPartyVictory(senate)
        self.assertEqual("Dire", res)

    def test_something2(self):
        solution = Solution()
        senate = "RDDDRDRRDR"
        res = solution.predictPartyVictory(senate)
        self.assertEqual("Dire", res)


if __name__ == '__main__':
    unittest.main()
