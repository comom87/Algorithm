import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
dp = [[[1e9 for _ in range(5)] for _ in range(5)] for _ in range(len(nums))]
dp[0][0][0] = 0

def calculate_cost(previous_point, new_point):
    if previous_point == new_point:
        return 1
    elif previous_point == 0:
        return 2
    elif abs(previous_point - new_point) == 2:
        return 4
    else:
        return 3


for i in range(len(nums) - 1):
    num = nums[i]
    for left in range(5):
        for right in range(5):
            if dp[i][left][right] == 1e9:
                continue
            dp[i + 1][num][right] = min(dp[i + 1][num][right], dp[i][left][right] + calculate_cost(left, num))
            dp[i + 1][left][num] = min(dp[i + 1][left][num], dp[i][left][right] + calculate_cost(right, num))
print(min(map(min, dp[-1])))