import heapq


class HireKWorker:
    def totalCost(self, cost, k, candidates):
        i = 0
        j = len(cost) - 1
        pq1 = []
        pq2 = []
        ans = 0
        while k > 0:
            while i <= j and len(pq1) < candidates:
                heapq.heappush(pq1, cost[i])
                i += 1
            while j >= i and len(pq2) < candidates:
                heapq.heappush(pq2, cost[j])
                j -= 1
            a = pq1[0] if pq1 else float('inf')
            b = pq2[0] if pq2 else float('inf')
            if a <= b:
                ans += a
                heapq.heappop(pq1)
            else:
                ans += b
                heapq.heappop(pq2)
            k -= 1
        return ans


s = HireKWorker()
costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
k = 3
candidates = 4
res = s.totalCost(costs, k, candidates)
print(res)
