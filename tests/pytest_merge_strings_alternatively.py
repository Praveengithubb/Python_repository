import unittest
import unittest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        minlength = min(len(word1), len(word2))

        for i in range(minlength):
            result.append(word1[i])
            result.append(word2[i])

        if len(word1) > minlength:
            result.append(word1[minlength:])
        elif len(word2) > minlength:
            result.append(word2[minlength:])

        return ''.join(result)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        s = "abc"
        s1 = "pqr"
        res = solution.mergeAlternately(s, s1)
        exp = "apbqcr"
        self.assertEqual(res, exp)

    def test_something1(self):
        solution = Solution()
        s = "ab"
        s1 = "pqrs"
        res = solution.mergeAlternately(s, s1)
        exp = "apbqrs"
        self.assertEqual(res, exp)

    def test_something2(self):
        solution = Solution()
        s = "abcd"
        s1 = "pq"
        res = solution.mergeAlternately(s, s1)
        exp = "apbqcd"
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
