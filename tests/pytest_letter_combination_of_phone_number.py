import unittest

from typing import List


class LetterCombination:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        output = []

        def backtrack(combination, next_digit):
            if not next_digit:
                output.append(combination)
                return
            else:
                letters = phone_map[int(next_digit[0]) - 2]
                for letter in letters:
                    backtrack(combination + letter, next_digit[1:])
        backtrack("", digits)
        return output


class MyTestCase(unittest.TestCase):
    def test_something(self):
        l = LetterCombination()
        digits = "23"
        res = l.letterCombinations(digits)
        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], res)

    def test_something1(self):
        l = LetterCombination()
        digits = "2"
        res = l.letterCombinations(digits)
        self.assertEqual(["a", "b", "c"], res)


if __name__ == '__main__':
    unittest.main()
