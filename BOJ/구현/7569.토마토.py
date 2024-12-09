import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def BFS():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue

            if tomatoes[nx][ny][nz] == 0:
                queue.append((nx, ny, nz))
                tomatoes[nx][ny][nz] = tomatoes[x][y][z] + 1

m, n, h = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

queue = deque()
for x in range(h):
    for y in range(n):
        for z in range(m):
            if tomatoes[x][y][z] == 1:
                queue.append((x, y, z))

BFS()

day = 0
for x in range(h):
    for y in range(n):
        for z in range(m):
            if tomatoes[x][y][z] == 0:
                print(-1)
                exit(0)
            day = max(day, tomatoes[x][y][z])
print(day - 1)