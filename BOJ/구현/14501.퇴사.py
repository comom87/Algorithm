# 참고: https://mxxcode.tistory.com/85

import sys
input = sys.stdin.readline

n = int(input())
schedules = [list(map(int, input().split())) for _ in range(n)]
earnings = [0 for _ in range(n + 1)]

for day in range(n - 1, -1, -1):
    if day + schedules[day][0] > n:
        earnings[day] = earnings[day + 1]
    else:
        earnings[day] = max(earnings[day + 1], earnings[day + schedules[day][0]] + schedules[day][1])
print(earnings[0])