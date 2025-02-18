# 하나의 수를 제거하거나 제거하지 않는 2가지 경우를 모두 고려하는 것까지는 생각했는데...
# 왜 갱신하는 방법을 생각을 못하니!!!
# 11번째줄 관련 반례: https://www.acmicpc.net/board/view/141372
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(2)]
dp[0][0] = nums[0]
dp[1][0] = -1000

for i in range(1, n):
    dp[0][i] = max(dp[0][i - 1] + nums[i], nums[i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + nums[i])
print(max(max(dp[0]), max(dp[1])))