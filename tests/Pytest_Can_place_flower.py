import unittest
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
                    i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        solution = Solution()
        flower = [1, 0, 0, 0, 1]
        n = 1
        res = solution.canPlaceFlowers(flower, n)
        self.assertEqual(res, True)

    def test_something2(self):
        solution = Solution()
        flower = [1, 0, 0, 0, 1]
        n = 2
        res = solution.canPlaceFlowers(flower, n)
        self.assertEqual(res, False)

    def test_something3(self):
        solution = Solution()
        flower = [0, 0, 1, 0, 0]
        n = 1
        res = solution.canPlaceFlowers(flower, n)
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()

