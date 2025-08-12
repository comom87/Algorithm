import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] += maze[x][y]
    
    return maze[n - 1][m - 1]

n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
print(bfs(0, 0))