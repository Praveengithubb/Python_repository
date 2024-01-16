import unittest


class Solution:
    @staticmethod
    def is_vowel(c):
        return c == 'a' or c == 'i' or c == 'e' or c == 'o' or c == 'u'

    @staticmethod
    def max_vowels(s, k):
        count = 0
        start = 0
        max_count = 0
        for end in range(len(s)):
            if Solution.is_vowel(s[end]):
                count += 1
            if end >= k:
                if Solution.is_vowel(s[start]):
                    count -= 1
                start += 1
            max_count = max(max_count, count)
        return max_count


class MyTestCase(unittest.TestCase):
    def test_max_vowels(self):
        s1 = "abciiidef"
        k1 = 3
        self.assertEqual(Solution.max_vowels(s1, k1), 3)

    def test_max_vowels1(self):
        s2 = "aeiou"
        k2 = 2
        self.assertEqual(Solution.max_vowels(s2, k2), 2)

    def test_max_vowels2(self):
        s2 = "leetcode"
        k2 = 3
        self.assertEqual(Solution.max_vowels(s2, k2), 2)


if __name__ == '__main__':
    unittest.main()
