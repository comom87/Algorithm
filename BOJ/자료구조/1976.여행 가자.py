import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n = int(input())
parent = [i for i in range(n)]
m = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1:
            union(i, j)

city = list(map(int, input().split()))
can_visit = 'YES'
for i in range(m - 1):
    if find(city[i] - 1) != find(city[i + 1] - 1):
        can_visit = 'NO'
        break
print(can_visit)