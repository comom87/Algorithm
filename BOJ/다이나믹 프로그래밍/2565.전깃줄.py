import sys
input = sys.stdin.readline

n = int(input())
wire = [0] * 501
max_b = 0
for _ in range(n):
    a, b = map(int, input().split())
    wire[a] = b

dp = [0] * 501
for i in range(1, 501):
    for j in range(i):
        if wire[i] > wire[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))