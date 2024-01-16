import unittest


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26
        for i in word1:
            freq1[ord(i) - ord('a')] += 1
        for i in word2:
            freq2[ord(i) - ord('a')] += 1
        for i in range(26):
            if (freq1[i] != 0 and freq2[i] == 0) or (freq1[i] == 0 and freq2[i] != 0):
                return False
        freq1.sort()
        freq2.sort()
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        return True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        word1 = "abc"
        word2 = "bca"
        res = solution.closeStrings(word1, word2)
        self.assertEqual(res, True)  # add assertion here

    def test_something1(self):
        solution = Solution()
        word1 = "a"
        word2 = "aa"
        res = solution.closeStrings(word1, word2)
        self.assertEqual(res, False)

    def test_something2(self):
        solution = Solution()
        word1 = "cabbba"
        word2 = "abbccc"
        res = solution.closeStrings(word1,word2)
        self.assertEqual(res, True)

if __name__ == '__main__':
    unittest.main()
