# 이항 계수의 성질 이용
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 1
for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
print(dp[n][k] % 10007)