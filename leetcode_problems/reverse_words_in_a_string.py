class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(s.strip().split())
        splited = s.split(" ")
        reversed_str = " ".join(reversed(splited))
        return reversed_str


solution = Solution()
strr = "the sky is blue"
res = solution.reverseWords(strr)
print(res)
