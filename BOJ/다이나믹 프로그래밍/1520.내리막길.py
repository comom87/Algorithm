# 1
# BFS와 Heap 사용
import sys
import heapq
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS(height, x, y):
    heap = []
    heapq.heappush(heap, (-height, x, y))
    dp[0][0] = 1

    while heap:
        _, x, y = heapq.heappop(heap)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] < graph[x][y]:
                if dp[nx][ny] == 0:
                    heapq.heappush(heap, (-graph[nx][ny], nx, ny))
                dp[nx][ny] += dp[x][y]
                
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[0 for _ in range(n)] for _ in range(m)]
BFS(graph[0][0], 0, 0)
print(dp[m - 1][n - 1])

# 2
# DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] < graph[x][y]:
            dp[x][y] += DFS(nx, ny)
    return dp[x][y]

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
# dp의 원소를 0으로 설정하면 내리막길로만 이동하는 경우의 수가 없는 경우와 방문 여부를 확인하는 경우를 구분할 수 없다.
dp = [[-1 for _ in range(n)] for _ in range(m)]
print(DFS(0, 0))