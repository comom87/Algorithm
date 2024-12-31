n, m = map(int, input().split())
k = int(input())

width = [0, n]
height = [0, m]
for _ in range(k):
    i, j = map(int, input().split())
    if i == 0:
        height.append(j)
    elif i == 1:
        width.append(j)
width.sort()
height.sort()

max_area = 0
for i in range(len(width) - 1):
    for j in range(len(height) - 1):
        x = width[i + 1] - width[i]
        y = height[j + 1] - height[j]
        max_area = max(max_area, x * y)
print(max_area)