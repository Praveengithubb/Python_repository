import unittest
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        asteroids = [-8, 8]
        res = solution.asteroidCollision(asteroids)
        self.assertEqual(res, [-8, 8])

    def test_something1(self):
        solution = Solution()
        asteroids = [8, -8]
        res = solution.asteroidCollision(asteroids)
        self.assertEqual(res, [])

    def test_something2(self):
        solution = Solution()
        asteroids = [10, 2, -5]
        res = solution.asteroidCollision(asteroids)
        self.assertEqual(res, [10])


if __name__ == '__main__':
    unittest.main()
