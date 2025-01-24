import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
dice = list(map(int, input().split()))
min_dice_sum = sys.maxsize

if n == 1:
    min_dice_sum = sum(dice) - max(dice)
else:
    for d in combinations(range(6), 3):
        if (0 in d and 5 in d) or (1 in d and 4 in d) or (2 in d and 3 in d):
            continue

        nums = []
        for i in d:
            nums.append(dice[i])
        nums.sort()

        dice_sum = nums[0] * (n - 2) * (n - 1) * 4 + nums[0] * (n - 2) * (n - 2) + sum(nums[:2]) * (n - 1) * 4 + sum(nums[:2]) * (n - 2) * 4 + sum(nums) * 4
        min_dice_sum = min(min_dice_sum, dice_sum)
print(min_dice_sum)