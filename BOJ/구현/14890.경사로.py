import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for x in range(n):
    flag = True
    visited = [False] * n
    for y in range(n - 1):
        if graph[x][y + 1] - graph[x][y] == 1:
            if y - l + 1 < 0:
                flag = False
                break

            for i in range(l):
                if graph[x][y - i] != graph[x][y] or visited[y - i]:
                    flag = False
                    break
            
            for i in range(l):
                visited[y - i] = True
        elif graph[x][y + 1] - graph[x][y] == -1:
            if y + l >= n:
                flag = False
                break

            for i in range(l):
                if graph[x][y + i + 1] != graph[x][y + 1] or visited[y + i + 1]:
                    flag = False
                    break

            for i in range(l):
                visited[y + i + 1] = True
        elif abs(graph[x][y + 1] - graph[x][y]) > 1:
            flag = False
            break

        if not flag:
            break
        
    if flag:
        cnt += 1

for y in range(n):
    flag = True
    visited = [False] * n
    for x in range(n - 1):
        if graph[x + 1][y] - graph[x][y] == 1:
            if x - l + 1 < 0:
                flag = False
                break

            for i in range(l):
                if graph[x - i][y] != graph[x][y] or visited[x - i]:
                    flag = False
                    break
            
            for i in range(l):
                visited[x - 1] = True
        elif graph[x + 1][y] - graph[x][y] == -1:
            if x + l >= n:
                flag = False
                break

            for i in range(l):
                if graph[x + i + 1][y] != graph[x + 1][y] or visited[x + i + 1]:
                    flag = False
                    break
            
            for i in range(l):
                visited[x + i + 1] = True
        elif abs(graph[x + 1][y] - graph[x][y]) > 1:
            flag = False
            break

        if not flag:
            break
        
    if flag:
        cnt += 1
print(cnt)