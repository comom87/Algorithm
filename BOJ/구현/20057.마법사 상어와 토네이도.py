import sys
input = sys.stdin.readline

n = int(input())
sand_field = [list(map(int, input().split())) for _ in range(n)]

def tornado(x, y, direction, step):
    global out_sand

    while True:
        for _ in range(2):
            for _ in range(step):
                x, y = x + dx[direction], y + dy[direction]

                if y < 0:
                    return

                spread_sand = 0
                for rx, ry, r in ratio[direction]:
                    nx = x + rx
                    ny = y + ry
                    if r == 0:
                        sand = sand_field[x][y] - spread_sand
                    else:
                        sand = int(sand_field[x][y] * r)
                
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        out_sand += sand
                    else:
                        sand_field[nx][ny] += sand
                    # 각 칸을 한 번씩만 방문하므로 모래가 이동한 후의 칸에 대한 연산은 하지 않아도 된다.
                    spread_sand += sand
            
            direction = (direction + 1) % 4
        step += 1

# 네 방향 모두 구하기
left = [(-2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01), (0, -2, 0.05), (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02), (0, -1, 0)]
down = [(-y, x, r) for x, y, r in left]
right = [(x, -y, r) for x, y, r in left]
up = [(y, x, r) for x, y, r in left]
ratio = {0: left, 1: down, 2: right, 3: up}

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x, y = n // 2, n // 2
step = 1
direction = 0
out_sand = 0

tornado(x, y, direction, step)
print(out_sand)