dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

t = int(input())
for test_case in range(t):
    n = int(input())
    lands = [list(input().split()) for _ in range(n)]

    max_building_height = 2
    for x in range(n):
        for y in range(n):
            if lands[x][y] == 'B':
                green_surrounded = False

                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    
                    if lands[nx][ny] == 'G':
                        green_surrounded = True
                        break

                building_height = -1
                if not green_surrounded:
                    for k in range(n):
                        if lands[x][k] == 'B':
                            building_height += 1
                        if lands[k][y] == 'B':
                            building_height += 1
                
                max_building_height = max(max_building_height, building_height)
    
    print(f'#{test_case + 1} {max_building_height}')
