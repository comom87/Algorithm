n, m = map(int, input().split())
j = int(input())
basket = [0, m - 1]
distance = 0
for _ in range(j):
    x = int(input())
    dist = 0
    if x - 1 < basket[0]:
        dist = (x - 1) - basket[0]
    elif x - 1 > basket[1]:
        dist = (x - 1) - basket[1]
    basket[0] += dist
    basket[1] += dist
    distance += abs(dist)
print(distance)