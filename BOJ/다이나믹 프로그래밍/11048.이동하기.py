import sys
input = sys.stdin.readline

n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
for i in range(n - 1):
    room[i + 1][0] += room[i][0]
for i in range(m - 1):
    room[0][i + 1] += room[0][i]
for i in range(1, n):
    for j in range(1, m):
        room[i][j] = max(room[i - 1][j], room[i][j - 1], room[i - 1][j - 1]) + room[i][j]
print(room[n - 1][m - 1])