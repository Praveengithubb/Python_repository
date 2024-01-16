import unittest
from typing import List


class Solution:

    def find_difference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        set1 = set(nums1)
        set2 = set(nums2)

        difference1 = list(set1 - set2)
        difference2 = list(set2 - set1)

        res.append(difference1)
        res.append(difference2)

        return res


def test_findDifference():
    solution = Solution()
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    result = solution.find_difference(nums1, nums2)
    assert result == [[1, 3], [4, 6]]


def test_findDifference1():
    solution = Solution()
    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    result = solution.find_difference(nums1, nums2)
    assert result == [[3], []]


if __name__ == '__main__':
    unittest.main()
