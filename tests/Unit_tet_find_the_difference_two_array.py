import unittest

from leetcode_python_problemss.find_the_difference_of_two_array import find_difference


def test_findDifference():
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    result = find_difference(nums1, nums2)
    assert result == [[1, 3], [4, 6]]


if __name__ == '__main__':
    unittest.main()
