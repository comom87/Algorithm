# BFS 느낌으로...!

import sys
input = sys.stdin.readline

dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]

def omok():
    for x in range(19):
        for y in range(19):
            if board[x][y] != 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1

                    while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == board[x][y]:
                        cnt += 1

                        if cnt == 5:
                            if 0 <= x - dx[i] < 19 and 0 <= x - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == board[x][y]:
                                break
                            if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == board[x][y]:
                                break
                            return x + 1, y + 1, board[x][y]

                        nx += dx[i]
                        ny += dy[i]
    return -1, -1, 0

board = [list(map(int, input().split())) for _ in range(19)]
x, y, color = omok()
if color == 0:
    print(0)
else:
    print(color)
    print(x, y)