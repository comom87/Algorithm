# 1. 적이 이동하는 방법
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# n, m, d = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# max_dead_enemy_cnt = 0
# for archers in combinations([i for i in range(m)], 3):
#     temp = [[graph[x][y] for y in range(m)] for x in range(n)]
#     dead_enemy_cnt = 0
#     flag = True

#     while True:
#         attack_enemy = []
#         for archer in archers:
#             attackable_enemy = []
#             enemy_cnt = 0
#             for x in range(n):
#                 for y in range(m):
#                     if temp[x][y] == 1:
#                         distance = abs(n - x) + abs(archer - y)
#                         if distance <= d:
#                             attackable_enemy.append([x, y, distance])
#                         enemy_cnt += 1
#             if enemy_cnt == 0:
#                 flag = False
#                 break
#             attackable_enemy.sort(key=lambda x: (x[2], x[1]))
#             if attackable_enemy:
#                 attack_enemy.append(attackable_enemy[0])

#         if not flag:
#             break

#         for ae in attack_enemy:
#             x, y, _ = ae
#             if temp[x][y] == 1:
#                 temp[x][y] = 0
#                 dead_enemy_cnt += 1

#         for i in range(n - 1, 0, -1):
#             temp[i] = temp[i - 1]
#         temp[0] = [0 for _ in range(m)]

#     print(archers, dead_enemy_cnt)
# print(max_dead_enemy_cnt)

# 2 궁수가 이동하는 방법
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, 0]
dy = [-1, 0, 1]

max_dead_enemy_cnt = 0
for archers_x in combinations([i for i in range(m)], 3):
    temp = [[graph[x][y] for y in range(m)] for x in range(n)]
    dead_enemy_cnt = 0

    for enemy_y in range(n - 1, -1, -1):
        dead_enemy = set()
        for archer_x in archers_x:
            queue = deque()
            visited = [[False for _ in range(m)] for _ in range(n)]
            queue.append((enemy_y, archer_x, 1))
            visited[enemy_y][archer_x] = True
            while queue:
                x, y, distance = queue.popleft()
                if temp[x][y] == 1:
                    dead_enemy.add((x, y))
                    break

                if distance < d:
                    for i in range(3):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if nx < 0 or ny < 0 or ny >= m:
                            continue

                        if not visited[nx][ny]:
                            queue.append((nx, ny, distance + 1))
                            visited[nx][ny] = True
        
        dead_enemy_cnt += len(dead_enemy)
        for x, y in dead_enemy:
            temp[x][y] = 0
    
    max_dead_enemy_cnt = max(max_dead_enemy_cnt, dead_enemy_cnt)
print(max_dead_enemy_cnt)