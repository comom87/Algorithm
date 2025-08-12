# import sys
# input = sys.stdin.readline

# n = int(input())
# nums_A = list(map(int, input().split()))

# is_sequence = True
# if n <= 2:
#     print("YES")
# else:
#     difference = nums_A[n - 1] - nums_A[n - 2]
#     for i in range(n - 2, 0, -1):
#         if difference != nums_A[i] - nums_A[i - 1]:
#             is_sequence = False
#             print("NO")
#             break
#     if is_sequence:
#         print("YES")

# if is_sequence:
#     nums_B = [num + 1 for num in nums_A]
#     print(' '.join(map(str, nums_B)))
#     print(' '.join([str(nums_A[i] - nums_B[i]) for i in range(n)]))

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

is_sequence = True
for i in range(n - 2):
    if nums[i + 1] - nums[i] != nums[i + 2] - nums[i + 1]:
        is_sequence = False
        break

if is_sequence:
    print("YES")
    print(*nums)
    print(*([0] * n))
else:
    print("NO")
