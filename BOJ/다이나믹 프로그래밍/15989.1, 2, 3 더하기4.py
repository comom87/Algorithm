import sys
input = sys.stdin.readline

dp = [0] * 10001
dp[0] = 1
for i in range(1, 4):
    for j in range(i, 10001):
        dp[j] += dp[j - i]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])