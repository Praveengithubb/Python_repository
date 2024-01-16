class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        minlength = min(len(word1), len(word2))

        for i in range(minlength):
            result.append(word1[i])
            result.append(word2[i])

        if len(word1) > minlength:
            result.append(word1[minlength:])
        elif len(word2) > minlength:
            result.append(word2[minlength:])

        return ''.join(result)


solution = Solution()
s = "abc"
s1 = "pqr"
res = solution.mergeAlternately(s, s1)
print(res)
