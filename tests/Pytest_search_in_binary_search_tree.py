import unittest


class SearchInABinaryTree:
    class Node:
        def __init__(self, value):
            self.key = value
            self.left = None
            self.right = None

    def __init__(self, val):
        self.root = self.Node(val)

    def insert_left(self, parentNode, val):
        parentNode.left = self.Node(val)

    def insert_right(self, parentNode, val):
        parentNode.right = self.Node(val)

    @staticmethod
    def search_bst(root, val):
        if root is None or root.key == val:
            return root
        if val < root.key:
            return SearchInABinaryTree.search_bst(root.left, val)
        else:
            return SearchInABinaryTree.search_bst(root.right, val)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = SearchInABinaryTree(4)
        s.insert_left(s.root, 2)
        s.insert_right(s.root, 7)
        s.insert_left(s.root.left, 1)
        s.insert_left(s.root.right, 3)

        result = SearchInABinaryTree.search_bst(s.root, 2)
        self.assertEqual(2, result.key)

    def test_something1(self):
        s = SearchInABinaryTree(4)
        s.insert_left(s.root, 2)
        s.insert_right(s.root, 7)
        s.insert_left(s.root.left, 1)
        s.insert_left(s.root.right, 3)

        result = SearchInABinaryTree.search_bst(s.root, 9)
        self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()
