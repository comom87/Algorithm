import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [1e9] * (k + 1)
dp[0] = 0
for _ in range(n):
    coin = int(input())
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)
if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])