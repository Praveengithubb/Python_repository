class MinCostClimbingStairs:
    def minCostClimbingStairs(self, cost):
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[-2], dp[-1])


m = MinCostClimbingStairs()
cost = [10, 15, 20]
print(m.minCostClimbingStairs(cost))
