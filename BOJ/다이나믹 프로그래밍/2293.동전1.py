import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k + 1)
dp[0] = 1
# 동전의 구성은 같은데 순서만 다른 것을 제외하기 위하여 동전 하나에 대하여 연산을 진행하고 이를 갱신하는 방식으로 진행
for _ in range(n):
    coin = int(input())
    for i in range(coin, k + 1):
        # dp[i] += dp[i - 동전의 가치]
        dp[i] += dp[i - coin]
print(dp[k])