import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
durability = deque(list(map(int, input().split())))
robot = deque([False] * n)

stage = 1
while True:
    durability.rotate(1)
    robot.rotate(1)

    robot[-1] = False

    for i in range(n - 2, -1, -1):
        if robot[i] and not robot[i + 1] and durability[i + 1] > 0:
            robot[i] = False
            robot[i + 1] = True
            durability[i + 1] -= 1
    
    robot[-1] = False

    if durability[0] > 0:
        robot[0] = True
        durability[0] -= 1
    
    if durability.count(0) >= k:
        break

    stage += 1
print(stage)