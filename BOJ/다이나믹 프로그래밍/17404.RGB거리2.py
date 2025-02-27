import sys
input = sys.stdin.readline

n = int(input())
colors = [list(map(int, input().split())) for _ in range(n)]
min_cost = 1e9
for i in range(3):
    dp = [[1e9 for _ in range(3)] for _ in range(n)]
    dp[0][i] = colors[0][i]
    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + colors[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + colors[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + colors[j][2]
    dp[n - 1][i] = 1e9
    min_cost = min(min_cost, min(dp[n - 1]))
print(min_cost)