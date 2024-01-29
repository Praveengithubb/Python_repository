import unittest


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


class Countgoodnodes:
    def __init__(self, d):
        self.root = Node(d)

    def insert_left(self, r, val):
        new_node = Node(val)
        r.left = new_node

    def insert_right(self, r, val):
        new_node = Node(val)
        r.right = new_node

    def good_nodes(self, root):
        self.ans = 0
        self.traversal(root, root.data)
        return self.ans

    def traversal(self, root, data):
        if root is None:
            return

        if root.data >= data:
            self.ans += 1
            data = root.data

        self.traversal(root.left, data)
        self.traversal(root.right, data)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        tree = Countgoodnodes(10)
        tree.insert_left(tree.root, 5)
        tree.insert_right(tree.root, 15)
        tree.insert_left(tree.root.left, 3)
        tree.insert_right(tree.root.left, 8)
        tree.insert_left(tree.root.right, 12)
        self.assertEqual(2, tree.good_nodes(tree.root))  # add assertion here

    def test_something1(self):
        tree = Countgoodnodes(10)
        self.assertEqual(1, tree.good_nodes(tree.root))


if __name__ == '__main__':
    unittest.main()
