import sys
input = sys.stdin.readline

n = int(input())
robots = {}
for i in range(n):
    x, y, v = map(int, input().split())
    time = (x ** 2 + y ** 2) / (v ** 2)
    robots[i + 1] = time
shooting_down_orders = sorted(robots.items(), key=lambda x: x[1])
for shooting_down_order in shooting_down_orders:
    print(shooting_down_order[0])