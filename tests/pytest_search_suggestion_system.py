import unittest


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False


class Solution:
    def insertWord(self, trie, word):
        for c in word:
            index = ord(c) - ord('a')
            if not trie.children[index]:
                trie.children[index] = TrieNode()
            trie = trie.children[index]
        trie.endOfWord = True

    def searchWord(self, trie, prefix):
        result = []
        for c in prefix:
            index = ord(c) - ord('a')
            if not trie.children[index]:
                return []
            trie = trie.children[index]
        self.dfs(trie, prefix, result)
        return result

    def dfs(self, trie, pre, result):
        if len(result) == 3:
            return
        if trie.endOfWord:
            result.append(pre)

        for i in range(26):
            if trie.children[i]:
                self.dfs(trie.children[i], pre + chr(i + ord('a')), result)

    def suggestedProducts(self, products, search):
        trie = TrieNode()
        for prod in products:
            self.insertWord(trie, prod)
        result = []
        prefix = ""
        for c in search:
            prefix += c
            result.append(self.searchWord(trie, prefix))
        return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
        search = "mouse"
        suggestedProducts = solution.suggestedProducts(products, search)
        expected_result = [["mobile", "moneypot", "monitor"],
                           ["mobile", "moneypot", "monitor"],
                           ["mouse", "mousepad"],
                           ["mouse", "mousepad"],
                           ["mouse", "mousepad"]]
        self.assertEqual(suggestedProducts, expected_result)


if __name__ == '__main__':
    unittest.main()
