# 1
import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))
total_weight = sum(weights)
dp = [[False for _ in range(total_weight * 2 + 1)] for _ in range(n)]
dp[0][total_weight + weights[0]] = True
dp[0][total_weight - weights[0]] = True
for i in range(1, n):
    for j in range(total_weight * 2 + 1):
        if dp[i - 1][j]:
            dp[i][j] = True
            dp[i][j + weights[i]] = True
            dp[i][j - weights[i]] = True
    dp[i][total_weight + weights[i]] = True
    dp[i][total_weight - weights[i]] = True

for marble in marbles:
    if total_weight + marble >= total_weight * 2 + 1:
        print('N', end=' ')
    else:
        if dp[n - 1][total_weight + marble]:
            print('Y', end=' ')
        else:
            print('N', end=' ')



# 2
import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))
total_weight = sum(weights)
dp = [[False for _ in range(total_weight + 1)] for _ in range(n)]
dp[0][weights[0]] = True
for i in range(1, n):
    for j in range(total_weight + 1):
        if dp[i - 1][j]:
            dp[i][j] = True
            dp[i][j + weights[i]] = True
            dp[i][abs(j - weights[i])] = True
    dp[i][weights[i]] = True

for marble in marbles:
    if marble >= total_weight + 1:
        print('N', end=' ')
    else:
        if dp[n - 1][marble]:
            print('Y', end=' ')
        else:
            print('N', end=' ')



# 3
import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))

nums = {0}
for weight in weights:
    new_nums = set()
    for num in nums:
        new_nums.add(num + weight)
        new_nums.add(num - weight)
    for new_num in new_nums:
        nums.add(new_num)

for marble in marbles:
    if marble in nums:
        print('Y', end=' ')
    else:
        print('N', end=' ')