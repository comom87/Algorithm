'''
    BOJ 17472. 다리 만들기2
    메모리: 35,084KB
    시간: 68ms
'''

'''
    아이디어
    - 각각의 섬을 구분하기 위해 섬을 찾고 서로 다른 번호를 할당 → BFS 사용
    - 모든 섬을 연결하는 다리 길이의 최솟값 찾기 → 최소 신장 트리를 구하기 위한 크루스칼 알고리즘 사용
                                           → 크루스칼 알고리즘을 사용하는 과정에서 유니온 파인드 알고리즘 사용
'''

import sys
from collections import deque
input = sys.stdin.readline

# 다리를 연결할 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, index):
    queue = deque()
    queue.append((x, y, index))
    maps[x][y] = index

    while queue:
        x, y, index = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if maps[nx][ny] == 1:
                queue.append((nx, ny, index))
                maps[nx][ny] = index

# 유니온 파인드 알고리즘
# 트리의 현재 노드에서 최상위 조상을 찾아서 반환하는 함수
def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

# 2개의 트리를 하나의 트리로 합치는 함수
def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 최소 신장 트리를 구하기 위한 크루스칼 알고리즘
def kruskal():
    edges.sort()

    total_cost = 0
    for edge in edges:
        cost, x, y = edge
        
        if find(x) != find(y):
            union(x, y)
            total_cost += cost
    return total_cost

n, m = map(int, input().split())    # n: 지도의 세로 크기, m: 지도의 가로 크기
maps = [list(map(int, input().split())) for _ in range(n)]  # maps: 지도의 정보

# 각각의 섬을 찾고 서로 다른 번호를 할당
index = 2   # index: 섬의 번호
for x in range(n):
    for y in range(m):
        if maps[x][y] == 1: # 현재 위치가 땅인 경우
            bfs(x, y, index)
            index += 1

parents = [i for i in range(index)]
edges = []

for x in range(n):
    for y in range(m):
        if maps[x][y] > 1:  # 각 섬의 현재 위치에서
            for d in range(4):  # 다리를 연결할 각각의 방향에 대하여
                nx, ny = x, y   # nx, ny: 다음 위치
                length = 0  # length: 다리의 길이
                
                while True:
                    nx += dx[d]
                    ny += dy[d]

                    if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == maps[x][y]:    # 다음 위치가 지도의 범위를 벗어나거나 다음 위치가 현재 위치와 같은(= 다음 위치가 같은 섬인 경우) 경우
                        break

                    if maps[nx][ny] == 0:   # 다음 위치가 바다인 경우
                        length += 1 # 다리의 길이 1 증가
                    else:   # 다음 위치가 땅인 경우
                        if length >= 2: # 다리의 길이가 2 이상이라면
                            edges.append((length, maps[x][y], maps[nx][ny]))    # 간선(= 다리)의 정보 저장
                        break

min_total_cost = kruskal()  # 크루스칼 알고리즘을 사용하여 최소 신장 트리 구하기
for i in range(2, index):   # 각 노드에 대하여
    parents[i] = find(parents[i])   # 최상위 조상 노드 갱신

print(min_total_cost if len(set(parents[2:])) == 1 else -1) # 모든 섬을 연결하는 것이 가능하면 다리의 최솟값 출력, 불가능하면 -1 출력
