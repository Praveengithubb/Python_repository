from typing import List


def find_difference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    res = []
    set1 = set(nums1)
    set2 = set(nums2)

    difference1 = list(set1 - set2)
    difference2 = list(set2 - set1)

    res.append(difference1)
    res.append(difference2)

    return res
