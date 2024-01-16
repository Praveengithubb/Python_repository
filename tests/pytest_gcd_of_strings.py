import unittest


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2) != (str2 + str1):
            return ""

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        gcd_length = gcd(len(str1), len(str2))
        return str2[:gcd_length]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        s = "ABCABC"
        s1 = "ABC"
        res = solution.gcdOfStrings(s, s1)
        self.assertEqual(res, "ABC")

    def test_something1(self):
        solution = Solution()
        s = "ABABAB"
        s1 = "ABAB"
        res = solution.gcdOfStrings(s, s1)
        self.assertEqual(res, "AB")

    def test_something2(self):
        solution = Solution()
        s = "LEET"
        s1 = "CODE"
        res = solution.gcdOfStrings(s, s1)
        self.assertEqual(res, "")


if __name__ == '__main__':
    unittest.main()
