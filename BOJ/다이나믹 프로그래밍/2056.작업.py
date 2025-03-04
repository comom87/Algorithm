import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
times = [0]
for i in range(1, n + 1):
    time, m, *nums = map(int, input().split())
    times.append(time)
    for num in nums:
        graph[num].append(i)
    indegree[i] += m

dp = [0] * (n + 1)

queue = deque()
for i in range(n):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = times[i]


while queue:
    now = queue.popleft()

    for next in graph[now]:
        indegree[next] -= 1
        dp[next] = max(dp[next], dp[now] + times[next])
        if indegree[next] == 0:
            queue.append(next)
print(max(dp))