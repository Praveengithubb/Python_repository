import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(s.strip().split())
        splited = s.split(" ")
        reversed_str = " ".join(reversed(splited))
        return reversed_str


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        s = "the sky is blue"
        self.assertEqual(solution.reverseWords(s), "blue is sky the")

    def test_something1(self):
        solution = Solution()
        s = "  hello world  "
        self.assertEqual(solution.reverseWords(s), "world hello")

    def test_something2(self):
        solution = Solution()
        s = "a good   example"
        self.assertEqual(solution.reverseWords(s), "example good a")


if __name__ == '__main__':
    unittest.main()
