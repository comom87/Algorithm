points = [list(map(int, input().split())) for _ in range(4)]
graph = [[0 for _ in range(100)] for _ in range(100)]
for x1, y1, x2, y2 in points:
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = 1

area = 0
for x in range(100):
    for y in range(100):
        if graph[x][y] == 1:
            area += 1
print(area)