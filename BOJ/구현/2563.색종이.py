import sys
input = sys. stdin.readline

n = int(input())
# 도화지를 한 칸 단위로 생각
paper = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

area = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            area += 1

print(area)