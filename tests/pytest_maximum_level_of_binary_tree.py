import unittest
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MaximumLevelSum:
    def maxLevelSum(self, root: TreeNode) -> int:
        que = deque()
        level = 0
        max_sum = float('-inf')
        cnt = 0
        que.append(root)
        while que:
            cnt += 1
            cur_sum = 0
            n = len(que)
            for _ in range(n):
                cur = que.popleft()
                cur_sum += cur.val
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            if cur_sum > max_sum:
                max_sum = cur_sum
                level = cnt
        return level


class MyTestCase(unittest.TestCase):
    def test_something(self):
        r = MaximumLevelSum()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(4)
        result = r.maxLevelSum(root)
        self.assertEqual(3, result)  # add assertion here

    def test_something1(self):
        r = MaximumLevelSum()
        root = TreeNode(1)
        result = r.maxLevelSum(root)
        self.assertEqual(1, result)


if __name__ == '__main__':
    unittest.main()
