import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vips = [int(input()) for _ in range(m)]
dp = [0] * 41
dp[0] = 1
dp[1] = 1
dp[2] = 2
# dp[i] = dp[i - 1]에서 i를 추가 → 자리 변경 X + dp[i - 2]에서 dp[i - 1]과 i의 자리를 변경
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

cnt = 1
previous = 1
for vip in vips:
    cnt *= dp[vip - previous]
    previous = vip + 1
cnt *= dp[n + 1 - previous]
print(cnt)