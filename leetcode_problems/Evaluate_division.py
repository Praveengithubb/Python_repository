from collections import defaultdict


def dfs(node, dest, gr, vis, ans, temp):
    if node in vis:
        return
    vis.add(node)
    if node == dest:
        ans[0] = temp
        return
    for ne, val in gr[node].items():
        dfs(ne, dest, gr, vis, ans, temp * val)


def build_graph(equations, values):
    gr = defaultdict(dict)
    for i in range(len(equations)):
        dividend, divisor = equations[i]
        value = values[i]
        gr[dividend][divisor] = value
        gr[divisor][dividend] = 1.0 / value
    return gr


def calc_equation(equations, values, queries):
    gr = build_graph(equations, values)
    final_ans = []
    for dividend, divisor in queries:
        if dividend not in gr or divisor not in gr:
            final_ans.append(-1.0)
        else:
            vis = set()
            ans = [-1.0]
            temp = 1.0
            dfs(dividend, divisor, gr, vis, ans, temp)
            final_ans.append(ans[0])
    return final_ans


if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    values = [2.0, 3.0]
    res = calc_equation(equations, values, queries)
    print(res)