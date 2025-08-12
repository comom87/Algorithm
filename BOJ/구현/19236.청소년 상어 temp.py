import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def move_fish(n):
    if n == 16:
    queue = deque(fish)

    while queue:
        num, x, y, d = queue.popleft()

        if num == 3:

        for i in range(8):
            nx = x + dx[(d + i) % 8]
            ny = y + dy[(d + i) % 8]

            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue

            if graph[nx][ny][0] == -1:
                continue

            if num == 3:
                print(x, y, nx, ny)

            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
            break
        print(graph)



graph = [[] for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        graph[i].append([data[2 * j], data[2 * j + 1] - 1])
graph[0][0] = [-1, graph[0][0][1]]

while True:
    
    for x in range(4):
        for y in range(4):
            if graph[x][y][0] > 0:
                fish.append((graph[x][y][0], x, y, graph[x][y][1]))
    fish.sort()

    move_fish(1)
    break
print(graph)