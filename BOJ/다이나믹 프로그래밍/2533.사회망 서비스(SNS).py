import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def DFS(now):
    visited[now] = True

    for next in tree[now]:
        if visited[next]:
            continue

        DFS(next)
        # 현재 노드가 얼리어답터가 아니다면 자식 노드는 얼리어답터이어야 한다.
        dp[now][0] += dp[next][1]
        # 현재 노드가 얼리어답터라면 자식 노드의 얼리어답터 여부는 상관없다.
        dp[now][1] += min(dp[next][0], dp[next][1])

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
dp = [[0, 1] for _ in range(n + 1)]
visited = [False] * (n + 1)

DFS(1)
print(min(dp[1]))