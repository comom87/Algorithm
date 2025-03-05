# 참고: https://galaxyexpress1999.tistory.com/55

import sys
input = sys.stdin.readline

dp = [[0 for _ in range(31)] for _ in range(31)]
for i in range(1, 31):
    dp[0][i] = 1
for i in range(1, 31):
    for j in range(i, 31):
        # 알약 반개를 i개 먹고 1개를 j가 먹은 경우 = 알약 반개를 (i - 1)개 먹고 1개를 j개 먹은 경우 + 알약 반개를 i개 먹고 1개를 (j - 1)개 먹은 경우
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

while True:
    n = int(input())

    if n == 0:
        break
    
    print(dp[n][n])