import unittest


class NumberOfProvinces:
    def dfs(self, graph, visited, i):
        for j in range(len(graph)):
            if graph[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(graph, visited, j)

    def find_circle_num(self, graph):
        n = len(graph)
        visited = [0] * n
        ans = 0

        for i in range(n):
            if visited[i] == 0:
                ans += 1
                self.dfs(graph, visited, i)

        return ans


class MyTestCase(unittest.TestCase):
    def test_find_circle_num(self):
        arr = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        provinces = NumberOfProvinces()
        self.assertEqual(2, provinces.find_circle_num(arr))

    def test_find_circle_num1(self):
        arr = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        provinces = NumberOfProvinces()
        self.assertEqual(3, provinces.find_circle_num(arr))


if __name__ == '__main__':
    unittest.main()
