class CityZero:
    def dfs(self, gr, visited, from_node):
        change = 0
        visited[from_node] = True
        for to in gr[from_node]:
            if not visited[abs(to)]:
                change += self.dfs(gr, visited, abs(to)) + (1 if to > 0 else 0)
        return change

    @staticmethod
    def minReorder(n, connections):
        gr = [[] for _ in range(n)]
        for c in connections:
            gr[c[0]].append(c[1])
            gr[c[1]].append(-c[0])
        return CityZero().dfs(gr, [False] * n, 0)


if __name__ == "__main__":
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    N = 6
    res = CityZero.minReorder(N, connections)
    print(res)
