import sys
from itertools import permutations
input = sys.stdin.readline

nums = list(permutations(list(map(str, range(1, 10))), 3))
n = int(input())
for _ in range(n):
    expected_num, strike, ball = map(int, input().split())
    expected_num = str(expected_num)
    candidates = []

    for num in nums:
        strike_cnt, ball_cnt = 0, 0
        for i in range(3):
            if expected_num[i] == num[i]:
                strike_cnt += 1
            else:
                if expected_num[i] in num:
                    ball_cnt += 1
        
        if strike_cnt == strike and ball_cnt == ball:
            candidates.append(num)
    nums = candidates
print(len(nums))