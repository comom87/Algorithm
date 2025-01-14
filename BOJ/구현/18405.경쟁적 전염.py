import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS(s, x, y):
    queue = deque(virus)

    while queue:
        now_x, now_y, now_v, now_t = queue.popleft()

        if now_t == s:
            break

        for d in range(4):
            next_x = now_x + dx[d]
            next_y = now_y + dy[d]

            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
                continue

            if graph[next_x][next_y] == 0:
                graph[next_x][next_y] = now_v
                queue.append((next_x, next_y, now_v, now_t + 1))
    return graph[x - 1][y - 1]

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((i, j, graph[i][j], 0))
    
    virus.sort(key=lambda x: x[2])
print(BFS(s, x, y))