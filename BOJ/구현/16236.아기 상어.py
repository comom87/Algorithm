import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    edible_fish = []
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] <= shark_size and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                if graph[nx][ny] != 0 and graph[nx][ny] < shark_size:
                    edible_fish.append([nx, ny, visited[nx][ny]])

    return sorted(edible_fish, key=lambda x: (-x[2], -x[0], -x[1]))    

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

shark_size = 2
eaten_fish_cnt = 0
time = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
            graph[i][j] = 0

while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]

    edibale_fish = BFS(x, y)
    if not edibale_fish:
        break
    
    x, y, distance = edibale_fish.pop()
    
    graph[x][y] = 0
    eaten_fish_cnt += 1
    if eaten_fish_cnt == shark_size:
        shark_size += 1
        eaten_fish_cnt = 0
    time += distance
print(time)