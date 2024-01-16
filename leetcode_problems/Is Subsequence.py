class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        c = 0
        for i in range(len(t)):
            if s[c] == t[i] and c < n:
                c += 1
        return c == n


solution = Solution()
s1 = "abc"
s2 = "ahbgdc"
result = solution.isSubsequence(s1, s2)
print(result)
