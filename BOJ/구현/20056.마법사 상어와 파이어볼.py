# 1
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
fireball = deque([list(map(int, input().split())) for _ in range(m)])
for _ in range(k):
    while fireball:
        r, c, m, s, d = fireball.popleft()

        nr = (r - 1 + dx[d] * s) % n
        nc = (c - 1 + dy[d] * s) % n
        graph[nr][nc].append([m, s, d])
    
    for x in range(n):
        for y in range(n):
            if len(graph[x][y]) == 1:
                fireball.append([x, y] + graph[x][y].pop())
                continue

            if len(graph[x][y]) >= 2:
                sum_m, sum_s, sum_d, odd_cnt, even_cnt, fireball_cnt = 0, 0, 0, 0, 0, len(graph[x][y])
                while graph[x][y]:
                    now_m, now_s, now_d = graph[x][y].pop()
                    sum_m += now_m
                    sum_s += now_s
                    if now_d % 2 == 0:
                        even_cnt += 1
                    else:
                        odd_cnt += 1
                
                nm = sum_m // 5
                if nm > 0:
                    ns = sum_s // fireball_cnt
                    if odd_cnt == fireball_cnt or even_cnt == fireball_cnt:
                        for nd in [0, 2, 4, 6]:
                            fireball.append((x, y, nm, ns, nd))
                    else:
                        for nd in [1, 3, 5, 7]:
                            fireball.append((x, y, nm, ns, nd))

fireball_m_cnt = 0
for _, _, m, _, _ in fireball:
    fireball_m_cnt += m
print(fireball_m_cnt)

# 2
# 시간 복잡도 개선