import unittest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        c = 0
        for i in range(len(t)):
            if s[c] == t[i] and c < n:
                c += 1
        return c == n


class MyTestCase(unittest.TestCase):
    def test_isSubsequence(self):
        solution = Solution()

        s1 = "abc"
        s2 = "ahbgdc"
        self.assertTrue(solution.isSubsequence(s1, s2))

    def test_isSubsequence1(self):
        solution = Solution()
        s3 = "axc"
        s4 = "ahbgdc"
        self.assertFalse(solution.isSubsequence(s3, s4))

    def test_isSubsequence2(self):
        solution = Solution()
        s3 = "axc"
        s4 = "acx"
        self.assertFalse(solution.isSubsequence(s3, s4))


if __name__ == '__main__':
    unittest.main()
