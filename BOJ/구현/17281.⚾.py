# 구현 순서
# 1. 타자의 순서를 정한다.
# 2. 3아웃 전까지는 현재 이닝에 대한 득점을 계산한다.
# 3. 3아웃이면 다음 이닝을 시작한다.

import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
inning = [list(map(int, input().split())) for _ in range(n)]
max_score = 0
for batter in permutations(range(1, 9), 8):
    batter = list(batter)
    lineup = batter[:3] + [0] + batter[3:]
    order = 0
    score = 0

    for i in range(n):
        base1, base2, base3 = 0, 0, 0
        out = 0
        while out < 3:
            if inning[i][lineup[order]] == 0:
                out += 1
            elif inning[i][lineup[order]] == 1:
                score += base3
                base3, base2, base1 = base2, base1, 1
            elif inning[i][lineup[order]] == 2:
                score += base2 + base3
                base3, base2, base1 = base1, 1, 0
            elif inning[i][lineup[order]] == 3:
                score += base1 + base2 + base3
                base3, base2, base1 = 1, 0, 0
            elif inning[i][lineup[order]] == 4:
                score += base1 + base2 + base3 + 1
                base3, base2, base1 = 0, 0, 0
            
            order = (order + 1) % 9

    max_score = max(max_score, score)
print(max_score)