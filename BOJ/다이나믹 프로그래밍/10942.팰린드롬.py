import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = True
for i in range(n - 1):
    if num[i] == num[i + 1]:
        dp[i][i + 1] = True

for length in range(2, n):
    for i in range(n - length):
        if num[i] == num[i + length] and dp[i + 1][i + length - 1]:
            dp[i][i + length] = True

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    if dp[s - 1][e - 1]:
        print(1)
    else:
        print(0)
