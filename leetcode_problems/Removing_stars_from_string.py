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


solution = Solution()
s1 = "leet**cod*e"
res = solution.removeStars(s1)
print(res)
