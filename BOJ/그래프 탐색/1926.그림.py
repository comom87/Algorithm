import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    size = 1
    paper[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if paper[nx][ny] == 1:
                queue.append((nx, ny))
                size += 1
                paper[nx][ny] = 0
    return size

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
picture_cnt = 0
picture_sizes = []
for x in range(n):
    for y in range(m):
        if paper[x][y] == 1:
            picture_cnt += 1
            picture_sizes.append(bfs(x, y))
print(picture_cnt)
print(0 if picture_cnt == 0 else max(picture_sizes))