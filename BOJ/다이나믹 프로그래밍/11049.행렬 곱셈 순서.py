import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[1e9 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 0

for length in range(1, n):
    for i in range(n - length):
        for j in range(i, i + length):
            dp[i][i + length] = min(dp[i][i + length], dp[i][j] + dp[j + 1][i + length] + matrix[i][0] * matrix[j][1] * matrix[i + length][1])
print(dp[0][n - 1])