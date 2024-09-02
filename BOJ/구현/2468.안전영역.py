import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS(x, y, rainHeight):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if lands[nx][ny] > rainHeight and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

n = int(input())
lands = [list(map(int, input().split())) for _ in range(n)]
maxRainHeight = max(max(land) for land in lands)

maxSafeArea = 0
for rainHeight in range(maxRainHeight):
    visited = [[False for _ in range(n)] for _ in range(n)]
    safeArea = 0
    for x in range(n):
        for y in range(n):
            if lands[x][y] > rainHeight and not visited[x][y]:
                BFS(x, y, rainHeight)
                safeArea += 1
    maxSafeArea = max(maxSafeArea, safeArea)
print(maxSafeArea)