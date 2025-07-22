# 되든 안되든 일단 구현하기!

import sys
input = sys.stdin.readline

def count_side(paper):
    sides = 0
    for i in range(102):
        for j in range(101):
            if paper[i][j] != paper[i][j + 1]:  # 현재 칸의 색과 다음 칸의 색이 다른 경우
                sides += 1  # 변이 존재
    return sides             

n = int(input())
# 도화지를 한 칸 단위로 생각
horizontal_paper = [[0 for _ in range(102)] for _ in range(102)]
for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            horizontal_paper[i][j] = 1
vertical_paper = list(zip(*horizontal_paper))
sides = count_side(horizontal_paper) + count_side(vertical_paper)
print(sides)