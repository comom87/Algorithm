# 처음에는 DFS라고 생각했지만...! BFS
# DFS로 해결하려고 했을 때 발생하는 문제점
# 처음으로 수빈이가 동생과 같은 위치에 도달할 때까지 걸린 시간을 출력하고 종료
# DFS를 사용하면 처음으로 수빈이가 동생과 같은 위치에 도달할 때까지 걸린 시간을 출력하고 종료하지 않고 계속 진행
# 즉, DFS를 사용하면 모든 경로를 탐색

from collections import deque

def BFS(x):
    queue = deque()
    queue.append(x)

    while queue:
        x = queue.popleft()
        if x == k:
            print(second[k])
            break

        for nx in [x + 1, 2 * x, x - 1]:
            if nx < 0 or nx > 100000:
                continue

            # second[nx] != 0은 이미 해당 위치에 도달한 최단 시간 경로가 있다는 것을 의미
            if second[nx] == 0:
                queue.append(nx)
                second[nx] = second[x] + 1

n, k = map(int, input().split())
second = [0] * 100001
BFS(n)