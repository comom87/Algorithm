import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
minCnt = 1e9
for i in range(n - 7):
    for j in range(m - 7):
        # 검은색으로 변경해야 하는 칸의 수
        paintBCnt = 0
        # 흰색으로 변경해야 하는 칸의 수
        paintWCnt = 0
        for y in range(i, i + 8):
            for x in range(j, j + 9):
                if (i + j) % 2 == 0:
                    if (x + y) % 2 == 0:
                        # board[i][j] = 'B'인 경우 = 검은색으로 시작하는 경우
                        if board[y][x] != 'B':
                            paintBCnt += 1
                        # board[i][j] = 'W'인 경우 = 흰색으로 시작하는 경우
                        if board[y][x] != 'W':
                            paintWCnt += 1
                    else:
                        # board[i][j] = 'B'인 경우 = 검은색으로 시작하는 경우
                        if board[y][x] != 'W':
                            paintWCnt += 1
                        # board[i][j] = 'W'인 경우 = 흰색으로 시작하는 경우
                        if board[y][x] != 'B':
                            paintBCnt += 1
                else:
                    if (x + y) % 2 == 0:
                        # board[i][j] = 'B'인 경우 = 검은색으로 시작하는 경우
                        if board[y][x] != 'W':
                            paintWCnt += 1
                        # board[i][j] = 'W'인 경우 = 흰색으로 시작하는 경우
                        if board[y][x] != 'B':
                            paintBCnt += 1
                    else:
                        # board[i][j] = 'B'인 경우 = 검은색으로 시작하는 경우
                        if board[y][x] != 'B':
                            paintBCnt += 1
                        # board[i][j] = 'W'인 경우 = 흰색으로 시작하는 경우
                        if board[y][x] != 'W':
                            paintWCnt += 1
        minCnt = min(minCnt, paintBCnt, paintWCnt)
print(minCnt)