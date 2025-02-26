# 위상 정렬
# 개념: https://www.youtube.com/watch?v=xeSz3pROPS8
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())

    dp = [0] * (n + 1)

    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = d[i - 1]
    
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + d[i - 1])
            if indegree[i] == 0:
                queue.append(i)
    
    print(dp[w])