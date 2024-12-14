import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(m)]

matrix3 = [[0 for _ in range(k)] for _ in range(n)]
for a in range(n):
    for b in range(m):
        for c in range(k):
            matrix3[a][c] += matrix1[a][b] * matrix2[b][c]

for i in range(n):
    for j in range(k):
        print(matrix3[i][j], end=' ')
    print()