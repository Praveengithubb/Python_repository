import unittest


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        sb = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        sb.extend(stack)
        return ''.join(sb)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        s1 = "leet**cod*e"
        res = solution.removeStars(s1)
        self.assertEqual(res, "lecoe")  # add assertion here

    def test_something1(self):
        solution = Solution()
        s1 = "erase*****"
        res = solution.removeStars(s1)
        self.assertEqual(res, "")  # add assertion here


if __name__ == '__main__':
    unittest.main()
