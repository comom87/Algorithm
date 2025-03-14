import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1e9] * n
dp[0] = 0
for i in range(n):
    for j in range(1, a[i] + 1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[n - 1] == 1e9:
    print(-1)
else:
    print(dp[n - 1])