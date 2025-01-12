import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
minCnt = 1e9
for i in range(n - 7):
    for j in range(m - 7):
        # 검은색으로 시작하는 경우
        BCnt = 0
        # 흰색으로 시작하는 경우
        WCnt = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    # board[i][j] = 'B'인 경우 = 검은색으로 시작하는 경우
                    if board[x][y] != 'B':
                        BCnt += 1
                    # board[i][j] = 'W'인 경우 = 흰색으로 시작하는 경우
                    if board[x][y] != 'W':
                        WCnt += 1
                else:
                    # board[i][j] = 'B'인 경우 = 검은색으로 시작하는 경우
                    if board[x][y] != 'W':
                        BCnt += 1
                    # board[i][j] = 'W'인 경우 = 흰색으로 시작하는 경우
                    if board[x][y] != 'B':
                         WCnt += 1
        minCnt = min(minCnt, BCnt, WCnt)
print(minCnt)