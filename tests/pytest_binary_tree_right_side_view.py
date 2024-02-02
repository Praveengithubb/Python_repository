import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Binarytreerightsideview:
    def rightSideView(self, root):
        result = []
        self.right_view(root, result, 0)
        return result

    def right_view(self, curr, result, curr_depth):
        if not curr:
            return
        if curr_depth == len(result):
            result.append(curr.val)
        self.right_view(curr.right, result, curr_depth + 1)
        self.right_view(curr.left, result, curr_depth + 1)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        r = Binarytreerightsideview()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(4)
        result = r.rightSideView(root)
        self.assertEqual(result, [1, 3, 4])

    def test_something1(self):
        r = Binarytreerightsideview()
        root = TreeNode(1)
        root.left = TreeNode(2)
        result = r.rightSideView(root)
        self.assertEqual(result, [1, 2])


if __name__ == '__main__':
    unittest.main()
