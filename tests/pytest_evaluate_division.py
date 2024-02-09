import unittest
from collections import defaultdict


class Evaluate_division:
    @staticmethod
    def dfs(node, dest, gr, vis, ans, temp):
        if node in vis:
            return
        vis.add(node)
        if node == dest:
            ans[0] = temp
            return
        for ne, val in gr[node].items():
            Evaluate_division.dfs(ne, dest, gr, vis, ans, temp * val)

    @staticmethod
    def build_graph(equations, values):
        gr = defaultdict(dict)
        for i in range(len(equations)):
            dividend, divisor = equations[i]
            value = values[i]
            gr[dividend][divisor] = value
            gr[divisor][dividend] = 1.0 / value
        return gr

    @staticmethod
    def calc_equation(equations, values, queries):
        gr = Evaluate_division.build_graph(equations, values)
        final_ans = []
        for dividend, divisor in queries:
            if dividend not in gr or divisor not in gr:
                final_ans.append(-1.0)
            else:
                vis = set()
                ans = [-1.0]
                temp = 1.0
                Evaluate_division.dfs(dividend, divisor, gr, vis, ans, temp)
                final_ans.append(ans[0])
        return final_ans


class MyTestCase(unittest.TestCase):
    def test_something(self):
        e = Evaluate_division()
        equations = [["a", "b"], ["b", "c"]]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        values = [2.0, 3.0]
        expected_results = [6.0, 0.5, -1.0, 1.0, -1.0]
        self.assertListEqual(expected_results, e.calc_equation(equations, values, queries))

    def test_something1(self):
        e = Evaluate_division()
        equations = [["a","b"],["b","c"],["bc","cd"]]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        values = [1.5, 2.5, 5.0]
        expected_results = [3.75000, 0.40000, 5.00000, 0.20000]
        self.assertListEqual(expected_results, e.calc_equation(equations, values, queries))


if __name__ == '__main__':
    unittest.main()
