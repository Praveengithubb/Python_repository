import heapq


def maxScore(nums1, nums2, k):
    pair = [(nums1[i], nums2[i]) for i in range(len(nums1))]
    pair.sort(key=lambda x: x[1], reverse=True)
    res = 0
    curr_sum = 0
    pq = []
    for i in range(k - 1):
        heapq.heappush(pq, pair[i][0])
        curr_sum += pair[i][0]
    for i in range(k - 1, len(nums1)):
        heapq.heappush(pq, pair[i][0])
        curr_sum += pair[i][0]
        res = max(res, curr_sum * pair[i][1])
        curr_sum -= heapq.heappop(pq)
        return res


nums1 = [1, 3, 3, 2]
nums2 = [2, 1, 3, 4]
k = 3
print(maxScore(nums1, nums2, k))
