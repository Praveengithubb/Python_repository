import unittest
from typing import List


class DeleteNodeInBST:
    class Node:
        def __init__(self, value):
            self.key = value
            self.left = None
            self.right = None

    def __init__(self, val):
        self.root = self.Node(val)

    def insert_left(self, parent_node, value):
        parent_node.left = self.Node(value)

    def insert_right(self, parent_node, value):
        parent_node.right = self.Node(value)

    @staticmethod
    def delete_node(root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = DeleteNodeInBST.delete_node(root.left, key)
        elif key > root.key:
            root.right = DeleteNodeInBST.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = DeleteNodeInBST.min_val(root.right)
            root.right = DeleteNodeInBST.delete_node(root.right, root.key)
        return root

    @staticmethod
    def min_val(root):
        min_val = root.key
        while root.left:
            min_val = root.left.key
            root = root.left
        return min_val

    @staticmethod
    def inorder_traversal_1(root) -> List[int]:
        result = []
        if root:
            result.extend(DeleteNodeInBST.inorder_traversal_1(root.left))
            result.append(root.key)
            result.extend(DeleteNodeInBST.inorder_traversal_1(root.right))
        return result


class MyTestCase(unittest.TestCase):

    def test_delete_node(self):
        s = DeleteNodeInBST(5)
        s.insert_left(s.root, 3)
        DeleteNodeInBST.delete_node(s.root, 3)
        expected_result = [5]
        result = DeleteNodeInBST.inorder_traversal_1(s.root)
        self.assertEqual(result, expected_result)

    def test_delete_node1(self):
        s = DeleteNodeInBST(None)
        expected_result = [None]
        result = DeleteNodeInBST.inorder_traversal_1(s.root)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
