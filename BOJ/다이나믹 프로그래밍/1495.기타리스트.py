# 1
import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [-1] * (m + 1)
dp[s] = 0
for i in range(n):
    temp = {}
    for j in range(m + 1):
        if dp[j] == i:
            if 0 <= j - v[i] <= m:
                temp[j - v[i]] = i + 1
            if 0 <= j + v[i] <= m:
                temp[j + v[i]] = i + 1
    
    for key, value in temp.items():
        dp[key] = value

last_volume = []
for i in range(m + 1):
    if dp[i] == n:
        last_volume.append(i)

if last_volume:
    print(max(last_volume))
else:
    print(-1)



# 2
import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
dp[0][s] = True
for i in range(n):
    for j in range(m + 1):
        if dp[i][j]:
            if 0 <= j - v[i] <= m:
                dp[i + 1][j - v[i]] = True
            if 0 <= j + v[i] <= m:
                dp[i + 1][j + v[i]] = True

max_volumne = -1
for i in range(m + 1):
    if dp[n][i]:
        max_volumne = i
print(max_volumne)