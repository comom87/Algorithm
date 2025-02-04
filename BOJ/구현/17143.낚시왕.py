# 참고: https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-17143-%EB%82%9A%EC%8B%9C%EC%99%95
# 시간 복잡도를 고려하면서 상어를 이동시켜야 한다.
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

r, c, m = map(int, input().split())
area = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(m):
    sr, sc, ss, sd, sz = map(int, input().split())
    area[sr - 1][sc - 1].append([ss, sd, sz])

total_size = 0
# 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
for y in range(c):
    # 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
    for x in range(r):
        if area[x][y]:
            total_size += area[x][y][0][2]
            area[x][y].pop()
            break
    
    # 3. 상어가 이동한다.
    temp = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if area[i][j]:
                sx, sy = i, j
                ss, sd, sz = area[i][j].pop()

                # 시간 초과
                # for _ in range(ss):
                #     sx += dx[sd]
                #     sy += dy[sd]

                #     if sx >= r or sy < 0:
                #         sx -= 2 * dx[sd]
                #         sy -= 2 * dy[sd]
                #         sd -= 1
                #     elif sx < 0 or sy >= c:
                #         sx -= 2 * dx[sd]
                #         sy -= 2 * dy[sd]
                #         sd += 1

                if sd == 1 or sd == 2:
                    # 상어가 0인 위치에서 이동하는 것으로 고정
                    if sd == 1:
                        sx = 2 * (r - 1) - sx
                    sx += ss
                    sx %= 2 * (r - 1)
                    if sx > r - 1:
                        sd = 1
                        sx = 2 * (r - 1) - sx
                    else:
                        sd = 2
                else:
                    if sd == 4:
                        sy = 2 * (c - 1) - sy
                    sy += ss
                    sy %= 2 * (c - 1)
                    if sy > c - 1:
                        sd = 4
                        sy = 2 * (c - 1) - sy
                    else:
                        sd = 3
                
                temp[sx][sy].append([ss, sd, sz])
    
    # 4. 한 칸에 상어가 2마리 이상 있는 경우, 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
    for i in range(r):
        for j in range(c):
            if len(temp[i][j]) > 1:
                temp[i][j].sort(key=lambda x: x[2], reverse=True)
                temp[i][j] = [temp[i][j][0]]
    
    area = temp
print(total_size)