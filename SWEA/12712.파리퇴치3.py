dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]

    max_flies = 0
    for x in range(n):
        for y in range(n):
            # '+' 형태로 분사
            flies1 = area[x][y]
            for i in range(4):
                for j in range(m - 1):
                    nx = x + (j + 1) * dx[2 * i]
                    ny = y + (j + 1) * dy[2 * i]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    flies1 += area[nx][ny]
        
            # 'x' 형태로 분산
            flies2 = area[x][y]
            for i in range(4):
                for j in range(m - 1):
                    nx = x + (j + 1) * dx[2 * i + 1]
                    ny = y + (j + 1) * dy[2 * i + 1]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    flies2 += area[nx][ny]
        
            max_flies = max(max_flies, flies1, flies2)
    
    print(f'#{test_case + 1} {max_flies}')
