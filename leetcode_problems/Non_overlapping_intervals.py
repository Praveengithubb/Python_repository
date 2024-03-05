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


o = NonoverlapingIntervals()
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(o.eraseOverlapIntervals(intervals))
