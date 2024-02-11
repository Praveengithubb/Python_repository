import collections
from collections import deque


def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    q = collections.deque()
    countfreshorange = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j))
            if grid[i][j] == 1:
                countfreshorange += 1
    if countfreshorange == 0:
        return 0
    if not q:
        return -1

    minutes = -1
    dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    while q:
        size = len(q)
        while size > 0:
            x, y = q.popleft()
            size -= 1
            for dx, dy in dirs:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    grid[i][j] = 2
                    countfreshorange -= 1
                    q.append((i, j))
        minutes += 1
    if countfreshorange == 0:
        return minutes
    return -1


grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(orangesRotting(grid))
