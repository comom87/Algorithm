import sys
input = sys.stdin.readline

n, d = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(n)]
shortcuts.sort()
dp = [i for i in range(d + 1)]
for start, end, distance in shortcuts:
    if end > d:
        continue

    dp[end] = min(dp[end], dp[start] + distance)
    for i in range(end + 1, d + 1):
        dp[i] = min(dp[i], dp[i - 1] + 1)
print(dp[d])