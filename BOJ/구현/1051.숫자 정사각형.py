import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rectangle = [list(input().rstrip()) for _ in range(n)]

for k in range(min(n, m), 0, -1):  # 정사각형 한 변의 길이
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            if rectangle[i][j] == rectangle[i][j + k - 1] == rectangle[i + k - 1][j] == rectangle[i + k - 1][j + k - 1]:
                print(k ** 2)
                exit(0)