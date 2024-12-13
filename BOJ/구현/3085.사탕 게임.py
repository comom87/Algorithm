import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

def count_max_same_candy():
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
        
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j - 1][i]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
    return max_cnt

result = 0
for i in range(n):
    for j in range(n):
        if j + 1 < n and board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            result = max(result, count_max_same_candy())
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        if i + 1 < n and board[i][j] != board[i + 1][j]:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            result = max(result, count_max_same_candy())
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
print(result)