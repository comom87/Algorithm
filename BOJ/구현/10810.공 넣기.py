n, m = map(int, input().split())
basckets = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for order in range(i, j + 1):
        basckets[order - 1] = k
print(*basckets)