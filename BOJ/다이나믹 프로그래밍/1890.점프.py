# 1
# 메모리 초과
# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]

# dx = [0, 1]
# dy = [1, 0]

# dp = [[0 for _ in range(n)] for _ in range(n)]
# queue = deque()
# queue.append((0, 0))
# while queue:
#     x, y = queue.popleft()

#     if board[x][y] == 0:
#         continue

#     for i in range(2):
#         nx = x + dx[i] * board[x][y]
#         ny = y + dy[i] * board[x][y]

#         if nx >= n or ny >= n:
#             continue

#         dp[nx][ny] += 1
#         queue.append((nx, ny))
# print(dp[n - 1][n - 1])



# 2
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            continue

        if i + board[i][j] < n:
            dp[i + board[i][j]][j] += dp[i][j]
        if j + board[i][j] < n:
            dp[i][j + board[i][j]] += dp[i][j]
print(dp[n - 1][n - 1])