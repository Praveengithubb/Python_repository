from typing import List
import pytest


class Solution:
    @staticmethod
    def maxOperations(nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1
        result = 0
        while start < end:
            if nums[start] + nums[end] < k:
                start += 1
            elif nums[start] + nums[end] > k:
                end -= 1
            else:
                start += 1
                end -= 1
                result += 1

        return result


def test_maxOperations():
    solution = Solution()

    my_list = [3, 1, 3, 4, 3]
    n1 = 6
    assert solution.maxOperations(my_list, n1) == 1


def test_maxOperations1():
    solution = Solution()
    my_list1 = [3, 1, 1, 1]
    n2 = 2
    assert solution.maxOperations(my_list1, n2) == 1


def test_maxOperations2():
    solution = Solution()
    my_list1 = [1, 4, 5, 4, 1]
    n2 = 5
    assert solution.maxOperations(my_list1, n2) == 2


if __name__ == "__main__":
    pytest.main()
