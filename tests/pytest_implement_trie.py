import unittest


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            char_index = ord(char) - ord('a')
            if not node.children[char_index]:
                node.children[char_index] = TrieNode()
            node = node.children[char_index]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            char_index = ord(char) - ord('a')
            if not node.children[char_index]:
                return False
            node = node.children[char_index]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            char_index = ord(char) - ord('a')
            if not node.children[char_index]:
                return False
            node = node.children[char_index]
        return True


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class MyTestCase(unittest.TestCase):
    def test_something(self):
        trie = Trie()
        trie.insert("apple")
        self.assertEqual(False, trie.search("appl"))
        self.assertEqual(True, trie.starts_with("apple"))

    def test_something1(self):
        trie = Trie()
        trie.insert("apple")
        self.assertEqual(True, trie.search("apple"))
        self.assertEqual(True, trie.starts_with("apple"))


if __name__ == '__main__':
    unittest.main()
