import sys
input = sys.stdin.readline

def DFS(depth):
    
    if depth == len(blank):
        for line in board:
            print(''.join(map(str, line)))
        exit()
    
    x, y = blank[depth]
    valid_num = [True] * 9

    for i in range(9):
        if board[x][i] != 0:
            valid_num[board[x][i] - 1] = False
        if board[i][y] != 0:
            valid_num[board[i][y] - 1] = False
    
    for i in range(3 * (x // 3), 3 * (x // 3) + 3):
        for j in range(3 * (y // 3), 3 * (y // 3) + 3):
            if board[i][j] != 0:
                valid_num[board[i][j] - 1] = False
    
    for num in range(9):
        if valid_num[num]:
            board[x][y] = num + 1
            DFS(depth + 1)
            board[x][y] = 0

blank = []
board = [list(map(int, input().rstrip())) for _ in range(9)]
for x in range(9):
    for y in range(9):
        if board[x][y] == 0:
            blank.append((x, y))

DFS(0)