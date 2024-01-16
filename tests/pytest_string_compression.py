import unittest
from typing import List


class Solution:
    def compress(self, str1: List[str]) -> int:
        if len(str1) == 1:
            return 1
        j = 1
        i = 0
        count = 1
        for j in range(len(str1) + 1):
            if j == len(str1) or str1[j] != str1[j - 1]:
                str1[i] = str1[j - 1]
                i += 1
                if count > 1:
                    countarray = list(str(count))
                    for a in range(len(countarray)):
                        str1[i] = countarray[a]
                        i += 1
                count = 1
            else:
                count += 1
        return i


class MyTestCase(unittest.TestCase):
    def test_compress(self):
        solution = Solution()
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        res = solution.compress(chars)
        self.assertEqual(res, 6)

    def test_compress1(self):
        solution = Solution()
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        res = solution.compress(chars)
        self.assertEqual(res, 4)

    def test_compress2(self):
        solution = Solution()
        chars = ["a"]
        res = solution.compress(chars)
        self.assertEqual(res, 1)


if __name__ == '__main__':
    unittest.main()
