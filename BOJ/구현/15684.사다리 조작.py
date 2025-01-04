import sys
input = sys.stdin.readline

def is_equal():
    for y in range(1, n + 1):
        num = y
        for x in range(1, h + 1):
            if line[x][num]:
                num += 1
            elif num > 0 and line[x][num - 1]:
                num -= 1
        if num != y:
            return False
    return True

def DFS(cnt, x, y):
    global answer

    if cnt > 3:
        return

    if is_equal():
        answer = min(answer, cnt)
        return

    for i in range(x, h + 1):
        for j in range(1, n):
            if line[i][j]:
                continue

            line[i][j] = True
            DFS(cnt + 1, i, j + 2)
            line[i][j] = False

n, m, h = map(int, input().split())
line = [[False for _ in range(n + 1)] for _ in range(h + 2)]
for _ in range(m):
    a, b = map(int, input().split())
    line[a][b] = True

answer = 1e9
DFS(0, 0, 0)
if answer > 3:
    answer = -1
print(answer)