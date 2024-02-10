from collections import deque


class Nearestexist:
    def __init__(self, first, second, step):
        self.first = first
        self.second = second
        self.step = step


def nearest_exit(maze, entrance):
    n = len(maze)
    m = len(maze[0])
    x, y = entrance
    delRow = [1, -1, 0, 0]
    delCol = [0, 0, 1, -1]
    q = deque()
    q.append((x, y, 0))
    while q:
        row, col, step = q.popleft()
        maze[row][col] = '+'
        for i in range(4):
            nrow = row + delRow[i]
            ncol = col + delCol[i]
            if 0 <= nrow < n and 0 <= ncol < m and maze[nrow][ncol] == '.':
                maze[nrow][ncol] = '+'
                q.append((nrow, ncol, step + 1))
                if nrow == 0 or ncol == 0 or nrow == n - 1 or ncol == m - 1:
                    return step + 1
    return -1


maze = [['+', '.', '+'], ['+', '.', '.'], ['+', '.', '+']]
entrance = [0, 1]
print(nearest_exit(maze, entrance))