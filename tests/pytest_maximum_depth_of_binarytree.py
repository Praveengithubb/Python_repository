import unittest


class MaximumDepthOfBinaryTree:
    class Node:
        def __init__(self, d):
            self.data = d
            self.left = None
            self.right = None

    def __init__(self, d):
        self.root = self.Node(d)

    def insert_left(self, r, val):
        new_node = self.Node(val)
        r.left = new_node

    def insert_right(self, r, val):
        new_node = self.Node(val)
        r.right = new_node

    @staticmethod
    def max_depth(root):
        if root is None:
            return 0
        lh = MaximumDepthOfBinaryTree.max_depth(root.left)
        rh = MaximumDepthOfBinaryTree.max_depth(root.right)
        return max(lh, rh) + 1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        tree = MaximumDepthOfBinaryTree(10)
        tree.insert_left(tree.root, 5)
        tree.insert_right(tree.root, 15)
        tree.insert_left(tree.root.left, 3)
        tree.insert_right(tree.root.left, 8)
        tree.insert_left(tree.root.right, 12)
        self.assertEqual(3, tree.max_depth(tree.root))

    def test_something1(self):
        tree = MaximumDepthOfBinaryTree(10)
        tree.insert_right(tree.root, 15)
        self.assertEqual(2, tree.max_depth(tree.root))


if __name__ == '__main__':
    unittest.main()
