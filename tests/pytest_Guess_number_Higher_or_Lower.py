import unittest


class GuessNumber:
    def guessNumber(self, n):
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            guess_result = self.guess(mid)
            if guess_result == 0:
                return mid
            elif guess_result == 1:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def guess(self, guessed_number):
        target = 72
        if guessed_number == target:
            return 0
        elif guessed_number > target:
            return 1
        else:
            return -1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        g = GuessNumber()
        n = 100
        self.assertEqual(72, g.guessNumber(n))  # add assertion here


if __name__ == '__main__':
    unittest.main()
