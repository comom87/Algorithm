# DFS 문제....
# 참고: https://sooz.tistory.com/106

import sys
from collections import deque
input = sys.stdin.readline

def left(idx, direct):
    if idx < 0:
        return
    
    if gears[idx + 1][6] != gears[idx][2]:
        left(idx - 1, -direct)
        gears[idx].rotate(direct)

def right(idx, direct):
    if idx > 3:
        return
    
    if gears[idx - 1][2] != gears[idx][6]:
        right(idx + 1, -direct)
        gears[idx].rotate(direct)

gears = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
k = int(input())
for _ in range(k):
    index, direction = map(int, input().split())
    left(index - 2, -direction)
    right(index, -direction)
    gears[index - 1].rotate(direction)

score = 0
for i in range(4):
    if gears[i][0] == 1:
        score += 2 ** i
print(score)