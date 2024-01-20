import unittest


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        return curString


class TestSolution(unittest.TestCase):
    def test_decodeString(self):
        solution = Solution()
        s = "3[a]2[bc]"
        res = solution.decodeString(s)
        self.assertEqual(res, "aaabcbc")  # Add your assertions here

    def test_decodeString1(self):
        solution = Solution()
        s = "3[a2[c]]"
        res = solution.decodeString(s)
        self.assertEqual(res, "accaccacc")

    def test_decodeString2(self):
        solution = Solution()
        s = "2[abc]3[cd]ef"
        res = solution.decodeString(s)
        self.assertEqual(res, "abcabccdcdcdef")


if __name__ == '__main__':
    unittest.main()
