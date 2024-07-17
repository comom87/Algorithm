import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
bags = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    weight, value = items[i]
    for j in range(1, k + 1):
        if weight > j:
            bags[i][j] = bags[i - 1][j]
        else:
            bags[i][j] = max(bags[i - 1][j], bags[i - 1][j - weight] + value)
print(bags[n][k])