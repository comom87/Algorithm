import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[0 for _ in range(m + 1)]]
for _ in range(n):
    matrix.append([0] + list(map(int, input().rstrip())))
dp = [[matrix[i][j] for j in range(m + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if matrix[i][j] == 1:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1
print(max(map(max, dp)) ** 2)