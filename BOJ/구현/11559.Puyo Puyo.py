import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS(x, y):
    queue = deque()
    same_puyo = []
    queue.append((x, y))
    same_puyo.append([x, y])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                continue

            if board[nx][ny] == board[x][y] and not visited[nx][ny]:
                queue.append((nx, ny))
                same_puyo.append([nx, ny])
                visited[nx][ny] = True
    return same_puyo

board = [list(input().rstrip()) for _ in range(12)]
cnt = 0
while True:
    visited = [[False for _ in range(6)] for _ in range(12)]
    same_puyo_cnt = 0

    for x in range(12):
        for y in range(6):
            if board[x][y] != '.' and not visited[x][y]:
                same_puyo = BFS(x, y)

                if len(same_puyo) >= 4:
                    for px, py in same_puyo:
                        board[px][py] = '.'
                    same_puyo_cnt += 1

    if same_puyo_cnt == 0:
        break
    
    for y in range(6):
        blank_cnt = 0
        for x in range(11, -1, -1):
            if board[x][y] == '.':
                blank_cnt += 1
            else:
                board[x + blank_cnt][y], board[x][y] = board[x][y], board[x + blank_cnt][y]
    
    cnt += 1

print(cnt)
    