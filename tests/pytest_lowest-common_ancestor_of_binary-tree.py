import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LongestCommonAncestorOfBinaryTree:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        else:
            return root


class MyTestCase(unittest.TestCase):
    def test_something(self):
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        p = root.left
        q = root.right
        result = LongestCommonAncestorOfBinaryTree().lowestCommonAncestor(root, p, q)
        self.assertEqual(3, result.val)

    def test_something1(self):
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        p = root
        q = root.right
        result = LongestCommonAncestorOfBinaryTree().lowestCommonAncestor(root, p, q)
        self.assertEqual(3, result.val)


if __name__ == '__main__':
    unittest.main()
