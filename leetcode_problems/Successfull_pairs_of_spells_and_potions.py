class SuccessfullPairs:
    def validposition(self, portions, success, spells):
        position = (success + spells - 1) // spells
        l = 0
        r = len(portions)
        while l < r:
            mid = (l + r) // 2
            if portions[mid] >= position:
                r = mid
            else:
                l = mid + 1
        return l

    def successfulPairs(self, spells, potions, success):
        potions.sort()
        res = []
        for spell in spells:
            res.append(len(potions) - self.validposition(potions, success, spell))
        return res


s = SuccessfullPairs()
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(s.successfulPairs(spells, potions, success))
