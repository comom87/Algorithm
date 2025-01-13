import sys
input = sys.stdin.readline

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())
basket = [list(map(int, input().split())) for _ in range(n)]
cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
for _ in range(m):
    d, s = map(int, input().split())

    moved_cloud = set()
    for x, y in cloud:
        nx = (x + dx[d - 1] * s) % n
        ny = (y + dy[d - 1] * s) % n
        moved_cloud.add((nx, ny))
        basket[nx][ny] += 1
    
    for x, y in moved_cloud:
        for i in range(1, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if basket[nx][ny] > 0:
                basket[x][y] += 1
    
    new_cloud = []
    for x in range(n):
        for y in range(n):
            if (x, y) not in moved_cloud and basket[x][y] >= 2:
                new_cloud.append((x, y))
                basket[x][y] -= 2
    cloud = new_cloud

print(sum(sum(b) for b in basket))