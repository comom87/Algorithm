import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [[0 for _ in range(21)] for _ in range(n - 1)]
dp[0][nums[0]] = 1
for i in range(n - 2):
    for j in range(21):
        if dp[i][j] != 0:
            if 0 <= j - nums[i + 1] <= 20:
                dp[i + 1][j - nums[i + 1]] += dp[i][j]
            if 0 <= j + nums[i + 1] <= 20:
                dp[i + 1][j + nums[i + 1]] += dp[i][j]
print(dp[-1][nums[-1]])