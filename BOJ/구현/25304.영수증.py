x = int(input())
n = int(input())
item_sum = 0
for _ in range(n):
    a, b = map(int, input().split())
    item_sum += a * b

if item_sum == x:
    print('Yes')
else:
    print('No')