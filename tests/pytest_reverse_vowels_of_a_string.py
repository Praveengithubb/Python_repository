import unittest


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        copy = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            elif s[l] in vowels and s[r] in vowels:
                copy[l], copy[r] = copy[r], copy[l]
                l += 1
                r -= 1

        return ''.join(copy)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        s = "hello"
        res = solution.reverseVowels(s)
        self.assertEqual(res, "holle")

    def test_something1(self):
        solution = Solution()
        s = "leetcode"
        res = solution.reverseVowels(s)
        self.assertEqual(res, "leotcede")

    def test_something2(self):
        solution = Solution()
        s = "aeiou"
        res = solution.reverseVowels(s)
        self.assertEqual(res, "uoiea")

if __name__ == '__main__':
    unittest.main()
