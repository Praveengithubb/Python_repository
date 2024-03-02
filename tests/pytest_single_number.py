import unittest


class SingleNumber:
    def singleNumber(self, nums):
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        return ans


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = SingleNumber()
        nums = [2, 2, 1]
        self.assertEqual(1, s.singleNumber(nums))  # add assertion here

    def test_something1(self):
        s = SingleNumber()
        nums = [1]
        self.assertEqual(1, s.singleNumber(nums))


if __name__ == '__main__':
    unittest.main()
