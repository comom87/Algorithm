import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
balloons = deque(enumerate(map(int, input().split())))
orders = []
while balloons:
    order, num = balloons.popleft()
    orders.append(order + 1)
    if num > 0:
        balloons.rotate(-(num - 1))
    else:
        balloons.rotate(-num)
print(' '.join(map(str, orders)))