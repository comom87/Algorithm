import sys
input = sys.stdin.readline

n = int(input())
row = [0 for _ in range(n)]
result = 0

# 현재 퀸의 위치를 이전 행들의 퀸의 위치와 비교했을 때, 현재 퀸의 위치가 유효한지 확인
def isPromising(y):
    for previousY in range(y):
        if row[previousY] == row[y] or abs(row[y] - row[previousY]) == abs(y - previousY):
            return False
    return True

def nQueens(y):
    global result
    if y == n:
        result += 1
        return

    for x in range(n):
        # 현재 퀸의 위치는 (x, y)
        row[y] = x
        if isPromising(y):
            nQueens(y + 1)

nQueens(0)
print(result)