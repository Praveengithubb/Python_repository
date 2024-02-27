import unittest


class LongestCommonSubsequence:
    def longest_common_subsequence(self, text1, text2):
        length1 = len(text1)
        length2 = len(text2)
        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]
        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[length1][length2]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        l = LongestCommonSubsequence()
        text1 = "abc"
        text2 = "abc"
        self.assertEqual(3, l.longest_common_subsequence(text1, text2))  # add assertion here

    def test_something1(self):
        l = LongestCommonSubsequence()
        text1 = "abcde"
        text2 = "ace"
        self.assertEqual(3, l.longest_common_subsequence(text1, text2))


if __name__ == '__main__':
    unittest.main()
