import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 미세먼지 확산
def spread_dust():
    temp_spread_dust = [[0 for _ in range(c)] for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if room[x][y] > 0:
                temp = 0

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        continue

                    if room[nx][ny] == -1:
                        continue

                    temp_spread_dust[nx][ny] += room[x][y] // 5
                    temp += room[x][y] // 5
                temp_spread_dust[x][y] -= temp

    for x in range(r):
        for y in range(c):
            room[x][y] += temp_spread_dust[x][y]

# 위쪽 공기청정기
def blow_up():
    x, y = up, 1
    direct = 3
    temp = 0
    while True:
        nx = x + dx[direct % 4]
        ny = y + dy[direct % 4]

        if x == up and y == 0:
            break

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct -= 1
            continue

        room[x][y], temp = temp, room[x][y]
        x, y = nx, ny

# 아래쪽 공기청정기
def blow_down():
    x, y = down, 1
    direct = 3
    temp = 0
    while True:
        nx = x + dx[direct % 4]
        ny = y + dy[direct % 4]

        if x == down and y == 0:
            break

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue

        room[x][y], temp = temp, room[x][y]
        x, y = nx, ny

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

up = -1
down = -1
# 공기청정기 위치 찾기
for x in range(r):
    if room[x][0] == -1:
        up = x
        down = x + 1
        break

for _ in range(t):
    spread_dust()
    blow_up()
    blow_down()

dust_amount = 0
for x in range(r):
    for y in range(c):
        if room[x][y] != -1:
            dust_amount += room[x][y]
print(dust_amount)