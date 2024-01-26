import unittest


class Solution:
    def swap_two_numbers(self, a, b):
        arr = [0, 0]
        if a == 0:
            a = b
            b = 0
            arr[0] = a
            arr[1] = b
            return arr
        if b == 0:
            b = a
            a = 0
            arr[0] = a
            arr[1] = b
            return arr
        else:
            a = a * b
            b = a // b
            a = a // b
            arr[0] = a
            arr[1] = b
            return arr


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        assert solution.swap_two_numbers(0, 5) == [5, 0]

    def test_something1(self):
        solution = Solution()
        assert solution.swap_two_numbers(5, 0) == [0, 5]

    def test_something2(self):
        solution = Solution()
        assert solution.swap_two_numbers(5, 10) == [10, 5]

if __name__ == '__main__':
    unittest.main()
