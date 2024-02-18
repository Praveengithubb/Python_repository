import unittest


class PeakElement:
    def findPeakElement(self, arr):
        i = 0
        j = len(arr) - 1
        index = 0
        while i < j:
            if arr[i] < arr[j]:
                index = j
                i += 1
            elif arr[i] > arr[j]:
                index = i
                j -= 1
            else:
                i += 1
        return index


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p = PeakElement()
        nums = [1]
        self.assertEqual(0, p.findPeakElement(nums))

    def test_something1(self):
        p = PeakElement()
        nums = [1, 2, 3, 1]
        self.assertEqual(2, p.findPeakElement(nums))


if __name__ == '__main__':
    unittest.main()
