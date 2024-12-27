# 1
# 시간: 1336ms
n = int(input())
num = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

matrix = [[0 for _ in range(n)] for _ in range(n)]
mid = n // 2
x, y = mid, mid
matrix[x][y] = 1
direction = 0
for i in range(mid + 1):
    while True:
        nx = x + dx[direction % 4]
        ny = y + dy[direction % 4]

        if x == y == mid - i:
            break

        if nx < mid - i or nx > mid + i or ny < mid - i or ny > mid + i:
            direction += 1
            continue

        matrix[nx][ny] = matrix[x][y] + 1
        x, y = nx, ny

for i in range(n):
    print(*matrix[i])
    for j in range(n):
        if matrix[i][j] == num:
            num_x = i + 1
            num_y = j + 1
print(num_x, num_y)



# 2
# 시간: 744ms
n = int(input())
target = int(input())

matrix = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = n // 2, n // 2
num = 1
matrix[x][y] = num
direction = 0
step = 1

target_x, target_y = x, y

while num < n * n:
    for _ in range(2):
        for _ in range(step):
            if num >= n * n:
                break
            x += dx[direction]
            y += dy[direction]
            num += 1

            matrix[x][y] = num
            if matrix[x][y] == target:
                target_x, target_y = x, y
        direction = (direction + 1) % 4
    step += 1

for row in matrix:
    print(' '.join(map(str, row)))
print(target_x + 1, target_y + 1)