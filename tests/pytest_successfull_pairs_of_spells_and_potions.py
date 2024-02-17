import unittest


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


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = SuccessfullPairs()
        spells = [5, 1, 3]
        potions = [1, 2, 3, 4, 5]
        success = 7
        res = [4, 0, 3]
        self.assertEqual(res, s.successfulPairs(spells, potions, success))  # add assertion here

    def test_something1(self):
        s = SuccessfullPairs()
        spells = [3, 1, 2]
        potions = [8, 5, 8]
        success = 16
        res = [2, 0, 2]
        self.assertEqual(res, s.successfulPairs(spells, potions, success))


if __name__ == '__main__':
    unittest.main()
