from collections import deque


class RoomsAndKeys:
    def __init__(self, v):
        self.adjList = [[] for _ in range(v)]

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    def canVisitAllRooms(self, adjList2):
        n = len(adjList2)
        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        while queue:
            size = len(queue)
            while size > 0:
                v = queue.popleft()
                for edge in adjList2[v]:
                    if not visited[edge]:
                        visited[edge] = True
                        queue.append(edge)
                size -= 1
        for i in range(1, n):
            if not visited[i]:
                return False
        return True


if __name__ == "__main__":
    r = RoomsAndKeys(4)
    r.addEdge(0, 1)
    r.addEdge(1, 2)
    r.addEdge(2, 3)
    print(r.canVisitAllRooms(r.adjList))
