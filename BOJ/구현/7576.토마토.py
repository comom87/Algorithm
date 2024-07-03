import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
for x in range(n):
    for y in range(m):
        if farm[x][y] == 1:
            queue.append((x, y))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if farm[nx][ny] == 0:
            queue.append((nx, ny))
            farm[nx][ny] = farm[x][y] + 1

day = 0
for x in range(n):
    for y in range(m):
        if farm[x][y] == 0:
            print(-1)
            exit(0)
        day = max(day, farm[x][y])
print(day - 1)