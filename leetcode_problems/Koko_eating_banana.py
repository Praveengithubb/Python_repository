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


k = KokoEatingBanana()
piles = [3, 6, 7, 11]
h = 8
print(k.minEatingSpeed(piles, h))
