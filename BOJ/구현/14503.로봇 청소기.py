import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

visited[r][c] = True
cnt = 1

while True:
    cleaned_all = True
    for _ in range(4):
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]

        if nr < 0 or nr >= n or nc < 0 or nc > m:
            continue

        if room[nr][nc] == 0 and not visited[nr][nc]:
            visited[nr][nc] = True
            cnt += 1
            r, c = nr, nc
            cleaned_all = False
            break
    
    if cleaned_all:
        nr = r - dr[d]
        nc = c - dc[d]
        if room[nr][nc] == 1:
            break
        else:
            r, c = nr, nc
print(cnt)