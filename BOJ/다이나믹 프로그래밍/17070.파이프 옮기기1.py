# 1
# 참고: https://velog.io/@eunseokim/BOJ-17070%EB%B2%88-%ED%8C%8C%EC%9D%B4%ED%94%84-%EC%98%AE%EA%B8%B0%EA%B8%B0-1-dp-%ED%92%80%EC%9D%B4-python
import sys
input = sys.stdin.readline

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(2, n):
    if house[0][i] == 0:
        dp[0][i][0] += dp[0][i - 1][0]

for i in range(1, n):
    for j in range(1, n):
        if house[i][j] == 0:
            dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][2]
            dp[i][j][1] += dp[i - 1][j][1] + dp[i - 1][j][2]
            if house[i][j - 1] == 0 and house[i - 1][j] == 0:
                dp[i][j][2] += dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]
print(sum(dp[-1][-1]))