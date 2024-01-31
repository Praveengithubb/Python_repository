class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LongestZigZagPathInBinaryTree:
    max_length = 0

    def longZigZag(self, root):
        self.solve(root, 0, 0)
        return self.max_length

    def solve(self, root, dir, currLen):
        if not root:
            return
        self.max_length = max(self.max_length, currLen)
        self.solve(root.left, 0, currLen + 1 if dir == 1 else 1)
        self.solve(root.right, 1, 1 if dir == 1 else currLen + 1)


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.right.left = TreeNode(1)

    zigzag = LongestZigZagPathInBinaryTree()
    result = zigzag.longZigZag(root)
    print(result)
