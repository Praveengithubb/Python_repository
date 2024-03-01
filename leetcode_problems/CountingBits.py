class CountingBits:
    def countBits(self, n):
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i // 2] + 1
        return dp


c = CountingBits()
print(c.countBits(5))
