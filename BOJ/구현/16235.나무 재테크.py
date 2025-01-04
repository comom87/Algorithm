import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def spring():
    for x in range(n):
        for y in range(n):
            tree[x][y].sort()
            for i in range(len(tree[x][y])):
                if tree[x][y][i] <= farm[x][y]:
                    farm[x][y] -= tree[x][y][i]
                    tree[x][y][i] += 1
                else:
                    for _ in range(i, len(tree[x][y])):
                        dead_tree.append([x, y, tree[x][y].pop()])
                    break

def summer():
    while dead_tree:
        x, y, age = dead_tree.pop()
        farm[x][y] += age // 2

def autumn():
    for x in range(n):
        for y in range(n):
            for i in range(len(tree[x][y])):
                if tree[x][y][i] % 5 == 0:
                    for d in range(8):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue

                        tree[nx][ny].append(1)

def winter():
    for x in range(n):
        for y in range(n):
            farm[x][y] += nourishment[x][y]

n, m, k = map(int, input().split())
nourishment = [list(map(int, input().split())) for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)
farm = [[5 for _ in range(n)] for _ in range(n)]
dead_tree = []

for _ in range(k):
    spring()
    summer()
    autumn()
    winter()

cnt = 0
for x in range(n):
    for y in range(n):
        cnt += len(tree[x][y])
print(cnt)