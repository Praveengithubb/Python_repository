class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


class LeafSimilarTrees:
    def __init__(self, d):
        self.root = Node(d)

    def insert_left(self, r, val):
        new_node = Node(val)
        r.left = new_node

    def insert_right(self, r, val):
        new_node = Node(val)
        r.right = new_node

    @staticmethod
    def leaf_similar(root1, root2):
        node_list1 = []
        node_list2 = []
        LeafSimilarTrees.find(root1, node_list1)
        LeafSimilarTrees.find(root2, node_list2)
        return node_list1 == node_list2

    @staticmethod
    def find(root, node_list):
        if root is None:
            return
        if root.left is None and root.right is None:
            node_list.append(root.data)
        else:
            LeafSimilarTrees.find(root.left, node_list)
            LeafSimilarTrees.find(root.right, node_list)


if __name__ == "__main__":
    tree = LeafSimilarTrees(10)
    tree.insert_left(tree.root, 5)
    tree.insert_right(tree.root, 15)
    tree.insert_left(tree.root.left, 3)
    tree.insert_right(tree.root.left, 8)
    tree.insert_left(tree.root.right, 12)

    tree1 = LeafSimilarTrees(1)
    tree1.insert_left(tree1.root, 50)
    tree1.insert_right(tree1.root, 5)
    tree1.insert_left(tree1.root.left, 3)
    tree1.insert_right(tree1.root.left, 8)
    tree1.insert_left(tree1.root.right, 11)

    print(LeafSimilarTrees.leaf_similar(tree.root, tree1.root))
