n, m, k = map(int, input().split())
dp = [[0 for _ in range(m)] for _ in range(n)]
row, column = n - 1, m - 1
if k != 0:
    row, column = (k - 1) // m, (k - 1) % m

for i in range(column + 1):
    dp[0][i] = 1
for i in range(row + 1):
    dp[i][0] = 1
for i in range(1, row + 1):
    for j in range(1, column + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

for i in range(column + 1, m):
    dp[row][i] = dp[row][column]
for i in range(row + 1, n):
    dp[i][column] = dp[row][column]
for i in range(row + 1, n):
    for j in range(column + 1, m):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
print(dp[n - 1][m - 1])