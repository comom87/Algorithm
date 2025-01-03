# 1
# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())
# t = int(input())
# hands = deque(list(map(int, input().split())))
# nums = list(map(int, input().split()))
# for i in range(t):
#     hands.rotate(-nums[i] + 1)
#     print(hands[0], end=' ')



# 2
import sys
input = sys.stdin.readline

n = int(input())
t = int(input())
hands = list(map(int, input().split()))
nums = list(map(int, input().split()))
bottom = 0

for num in nums:
    bottom = (bottom + num - 1) % (2 * n)
    print(hands[bottom], end=' ')