import unittest


class NonoverlapingIntervals:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        previous = 0
        n = len(intervals)
        ans = 0
        for current in range(1, n):
            if intervals[current][0] < intervals[previous][1]:
                ans += 1
                if intervals[current][1] < intervals[previous][1]:
                    previous = current
            else:
                previous = current
        return ans


class MyTestCase(unittest.TestCase):
    def test_something(self):
        o = NonoverlapingIntervals()
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        self.assertEqual(1, o.eraseOverlapIntervals(intervals))  # add assertion here

    def test_something1(self):
        o = NonoverlapingIntervals()
        intervals = [[1, 2], [2, 3]]
        self.assertEqual(0, o.eraseOverlapIntervals(intervals))


if __name__ == '__main__':
    unittest.main()
