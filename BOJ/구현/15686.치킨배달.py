import sys
input = sys.stdin.readline

def DFS(idx, cnt):
    global min_distnace

    if cnt == m:
        total_distance = 0
        for h in house:
            distance = 1e9
            for i in range(len(chicken)):
                if visited[i]:
                    distance = min(distance, abs(h[0] - chicken[i][0]) + abs(h[1] - chicken[i][1]))
            total_distance += distance
        min_distnace = min(min_distnace, total_distance)
        return

    for i in range(idx, len(chicken)):
        visited[i] = True
        DFS(i + 1, cnt + 1)
        visited[i] = False

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            house.append([r, c])
        elif city[r][c] == 2:
            chicken.append([r, c])
visited = [False for _ in range(len(chicken))]

min_distnace = 1e9
DFS(0, 0)
print(min_distnace)