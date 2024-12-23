import sys
input = sys.stdin.readline

n = int(input())
room = [list(input().rstrip()) for _ in range(n)]

horizontal_cnt = 0
vertical_cnt = 0
for i in range(n):
    temp_cnt1, temp_cnt2 = 0, 0
    for j in range(n):
        if room[i][j] == '.':
            temp_cnt1 += 1
        else:
            temp_cnt1 = 0
        
        if temp_cnt1 == 2:
            horizontal_cnt += 1
        
        if room[j][i] == '.':
            temp_cnt2 += 1
        else:
            temp_cnt2 = 0

        if temp_cnt2 == 2:
            vertical_cnt += 1
print(horizontal_cnt, vertical_cnt)