class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currentNo = 0
        curString = " "
        for c in s:
            if c.isdigit():
                currentNo = currentNo * 10 + int(c)
            elif c == '[':
                stack.append(curString)
                stack.append(currentNo)
                curString = ""
                currentNo = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            else:
                curString += c

        return curString


solution = Solution()
s = "3[a]2[bc]"
res = solution.decodeString(s)
print(res)
