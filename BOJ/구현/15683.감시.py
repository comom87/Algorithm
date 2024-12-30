import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(depth, office):
    global min_cnt

    if depth == len(cctv):
        cnt = 0
        for x in range(n):
            for y in range(m):
                if office[x][y] == 0:
                    cnt += 1
        min_cnt = min(min_cnt, cnt)
        return

    cctv_num, x, y = cctv[depth]
    temp = [[office[x][y] for y in range(m)] for x in range(n)]
    for direction in cctv_direction[cctv_num]:
        for d in direction:
            nx, ny = x, y
            while True:
                nx += dx[d]
                ny += dy[d]

                if nx < 0 or nx >= n or ny < 0 or ny >= m or temp[nx][ny] == 6:
                    break

                if temp[nx][ny] == 0:
                    temp[nx][ny] = '#'
        DFS(depth + 1, temp)
        temp = [[office[x][y] for y in range(m)] for x in range(n)]

            

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cctv_direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

cctv = []
for x in range(n):
    for y in range(m):
        if office[x][y] in range(1, 6):
            cctv.append([office[x][y], x, y])
min_cnt = 1e9

DFS(0, office)

print(min_cnt)