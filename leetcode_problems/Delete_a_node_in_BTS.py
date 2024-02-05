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

    def inorder_traversal(root):
        if root:
            DeleteNodeInBST.inorder_traversal(root.left)
            print(root.key, end=" ")
            DeleteNodeInBST.inorder_traversal(root.right)


if __name__ == "__main__":
    s = DeleteNodeInBST(5)
    s.insert_left(s.root, 3)
    s.insert_right(s.root, 6)
    s.insert_left(s.root.left, 2)
    s.insert_left(s.root.right, 4)
    DeleteNodeInBST.delete_node(s.root, 2)
    DeleteNodeInBST.inorder_traversal(s.root)
