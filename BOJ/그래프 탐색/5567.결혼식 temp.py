import sys
input = sys.stdin.readline

def dfs(depth, friend):
    if depth == 2:
        return
    
    for f in friends[friend]:
        invited[f] = True
        dfs(depth + 1, f)

n = int(input())
m = int(input())
friends = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
invited = [False] * (n + 1)

invited[1] = True
dfs(0, 1)

invited_cnt = 0
for i in range(2, n + 1):
    if invited[i]:
        invited_cnt += 1
print(invited_cnt)