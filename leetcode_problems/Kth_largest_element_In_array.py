import heapq


class KthLargest:
    def findKthLargest(self, num, k):
        min_heap = []

        for n in num:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            else:
                if min_heap[0] < n:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, n)
        return min_heap[0]


o = KthLargest()
nums = [3, 2, 1, 5, 6, 4]
k1 = 2
res = o.findKthLargest(nums, k1)
print(res)
