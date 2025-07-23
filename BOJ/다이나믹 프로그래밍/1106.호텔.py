# 1
import sys
input = sys.stdin.readline

c, n = map(int, input().split())
dp = [1e9] * (c + 1)
dp[0] = 0
for _ in range(n):
    cost, customer = map(int, input().split())
    # 비용으로 얻을 수 있는 고객의 수(customer) > 늘력야 하는 최소 고객의 수(c)인 가능성을 고려하여 min(customer, c + 1)을 사용
    for i in range(min(customer, c + 1)):
        dp[i] = min(dp[i], cost)
    for i in range(min(customer, c + 1), c + 1):
        dp[i] = min(dp[i], dp[i - customer] + cost)
print(dp[c])

# 2
# 참고: https://bio-info.tistory.com/218

import sys
input = sys.stdin.readline

c, n = map(int, input().split())
dp = [1e9] * (c + 100)
dp[0] = 0
for _ in range(n):
    cost, customer = map(int, input().split())
    for i in range(customer, c + 100):
        dp[i] = min(dp[i], dp[i - customer] + cost)
print(min(dp[c:]))