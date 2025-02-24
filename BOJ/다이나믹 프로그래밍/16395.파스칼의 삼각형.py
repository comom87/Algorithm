n, k = map(int, input().split())
dp = [[0 for _ in range(30)] for _ in range(30)]
for i in range(30):
    dp[i][0] = 1
    dp[i][i] = 1
for i in range(2, 30):
    for j in range(1, 29):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
print(dp[n - 1][k - 1])