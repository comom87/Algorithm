import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
times = []
for i in range(1, n + 1):
    time, *nums = map(int, input().split())
    for j in range(len(nums) - 1):
        graph[nums[j]].append(i)
        indegree[i] += 1
    times.append(time)

dp = [0] * (n + 1)

queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = times[i - 1]
    
while queue:
    now = queue.popleft()
    
    for i in graph[now]:
        indegree[i] -= 1
        dp[i] = max(dp[i], dp[now] + times[i - 1])
        if indegree[i] == 0:
            queue.append(i)

for i in range(1, n + 1):
    print(dp[i])