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


solution = Solution()
x = "ABCABC"
y = "ABC"
res = solution.gcdOfStrings(x, y)
print(res)
