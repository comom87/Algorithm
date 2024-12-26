import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))
trucks_on_bridge = deque([0] * w)
time = 0
while trucks_on_bridge:
    trucks_on_bridge.popleft()
    if trucks:
        if sum(trucks_on_bridge) + trucks[0] <= l:
            trucks_on_bridge.append(trucks.popleft())
        else:
            trucks_on_bridge.append(0)
    time += 1
print(time)