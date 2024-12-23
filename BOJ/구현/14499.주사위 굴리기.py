import sys
input = sys.stdin.readline

# 주사위를 굴렸을 때 전개도의 변화가 중요!
def roll_dice(direction):
    if direction == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif direction == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    elif direction == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0] * 6

for command in commands:
    nx = x + dx[command - 1]
    ny = y + dy[command - 1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx, ny = x, y
        continue

    roll_dice(command)

    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0
    
    x, y = nx, ny

    print(dice[0])