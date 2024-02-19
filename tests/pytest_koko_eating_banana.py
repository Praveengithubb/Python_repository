import unittest


class KokoEatingBanana:

    @staticmethod
    def calculateTotalHours(piles, hourly):
        total_hours = 0
        for pile in piles:
            total_hours += -(-pile // hourly)
        return total_hours

    def minEatingSpeed(self, piles, h):
        piles.sort()
        i = 1
        j = piles[-1]
        while i <= j:
            mid = (i + j) // 2
            totalH = self.calculateTotalHours(piles, mid)
            if totalH < h:
                j = mid - 1
            elif totalH > h:
                i = mid + 1
            else:
                j = mid - 1
        return i


class MyTestCase(unittest.TestCase):
    def test_something(self):
        k = KokoEatingBanana()
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(4, k.minEatingSpeed(piles, h))  # add assertion here

    def test_something1(self):
        k = KokoEatingBanana()
        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(23, k.minEatingSpeed(piles, h))


if __name__ == '__main__':
    unittest.main()
