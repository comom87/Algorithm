# DFS? 파이프 옮기기1?
import sys
input = sys.stdin.readline

dx = [0, 1, 0]
dy = [1, 0, -1]

def DFS(x, y):
    if x == n - 1 and y == m - 1:
        return
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if not visited[nx][ny] and dp[x][y] + topographic_map[nx][ny] > dp[nx][ny]:
            visited[nx][ny] = True
            dp[nx][ny] = dp[x][y] + topographic_map[nx][ny]
            DFS(nx, ny)
            visited[nx][ny] = False

n, m = map(int, input().split())
topographic_map = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1e9 for _ in range(m)] for _ in range(n)]
dp[0][0] = topographic_map[0][0]
visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True
DFS(0, 0)
print(dp[n - 1][m - 1])