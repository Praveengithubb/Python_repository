
class TreeNode:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


class PathSumIII:
    count = 0

    @staticmethod
    def path_sum(root, target):
        pre_sum = {0: 1}
        PathSumIII.helper(root, 0, target, pre_sum)
        return PathSumIII.count

    @staticmethod
    def helper(root, curr_sum, target, pre_sum):
        if not root:
            return
        curr_sum += root.data
        if curr_sum - target in pre_sum:
            PathSumIII.count += pre_sum.get(curr_sum - target)
        pre_sum[curr_sum] = pre_sum.get(curr_sum, 0) + 1
        PathSumIII.helper(root.left, curr_sum, target, pre_sum)
        PathSumIII.helper(root.right, curr_sum, target, pre_sum)
        pre_sum[curr_sum] -= 1


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    result = PathSumIII.path_sum(root, 22)
    print(result)
