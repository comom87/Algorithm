import sys
input = sys.stdin.readline

# n, k = map(int, input().split())
# nums = list(map(int, input().split()))
# cnt = 0
# for i in range(len(nums) // 2):
#     min_num, max_num = min(nums[i], nums[n - i - 1]), max(nums[i], nums[n - i - 1])
#     difference = max_num - min_num
#     cnt += difference // k
#     remainder = difference % k
#     if remainder > k // 2:
#         cnt += 1
#         cnt += (min_num + k * (difference // k + 1)) - max_num
#     else:
#         cnt += remainder
# print(cnt)

n, k = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
for i in range(len(nums) // 2):
    difference = abs(nums[i] - nums[n - i - 1])
    quotient = difference // k
    remainder = difference % k
    cnt += quotient + min(remainder, k - remainder + 1)
print(cnt)