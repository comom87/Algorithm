import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(start):
    visited[start] = True
    for end, dist in graph[start]:
        if not visited[end]:
            distance[end] = distance[start] + dist
            DFS(end)

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
distance = [0 for _ in range(n + 1)]
visited = [False] * (n + 1)

DFS(1)

print(max(distance))