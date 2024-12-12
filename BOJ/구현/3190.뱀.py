import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

l = int(input())
direction = {}
for _ in range(l):
    second, direct = input().split()
    direction[int(second)] = direct

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

head_x, head_y = 0, 0
snake_tail = deque()
snake_tail.append((0, 0))
board[0][0] = 2
snake_direction = 1
time = 0
while True:
    head_x += dx[snake_direction]
    head_y += dy[snake_direction]
    time += 1

    if head_x < 0 or head_x >= n or head_y < 0 or head_y >= n or board[head_x][head_y] == 2:
        break

    if board[head_x][head_y] == 0:
        tail_x, tail_y = snake_tail.popleft()
        board[tail_x][tail_y] = 0
    snake_tail.append((head_x, head_y))
    board[head_x][head_y] = 2

    if time in direction.keys():
        if direction[time] == 'L':
            snake_direction = (snake_direction - 1) % 4
        elif direction[time] == 'D':
            snake_direction = (snake_direction + 1) % 4

print(time)