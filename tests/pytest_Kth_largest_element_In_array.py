import heapq
import unittest


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


class MyTestCase(unittest.TestCase):
    def test_something(self):
        o = KthLargest()
        nums = [3, 2, 1, 5, 6, 4]
        k1 = 2
        res = o.findKthLargest(nums, k1)
        self.assertEqual(5, res)  # add assertion here

    def test_something1(self):
        o = KthLargest()
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k1 = 4
        res = o.findKthLargest(nums, k1)
        self.assertEqual(4, res)


if __name__ == '__main__':
    unittest.main()
