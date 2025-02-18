# 1
# DP
# 참고: https://velog.io/@eunseokim/BOJ-17070%EB%B2%88-%ED%8C%8C%EC%9D%B4%ED%94%84-%EC%98%AE%EA%B8%B0%EA%B8%B0-1-dp-%ED%92%80%EC%9D%B4-python
# import sys
# input = sys.stdin.readline

# n = int(input())
# house = [list(map(int, input().split())) for _ in range(n)]
# dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
# dp[0][1][0] = 1
# for i in range(2, n):
#     if house[0][i] == 0:
#         dp[0][i][0] += dp[0][i - 1][0]

# for i in range(1, n):
#     for j in range(1, n):
#         if house[i][j] == 0:
#             dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][2]
#             dp[i][j][1] += dp[i - 1][j][1] + dp[i - 1][j][2]
#             if house[i][j - 1] == 0 and house[i - 1][j] == 0:
#                 dp[i][j][2] += dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]
# print(sum(dp[-1][-1]))



# 2
# DFS
# import sys
# input = sys.stdin.readline

# def DFS(x, y, direction):
#     global cnt

#     if x == n - 1 and y == n - 1:
#         cnt += 1
#         return
    
#     if direction == 0:
#         if 0 <= x < n and 0 <= y + 1 < n and house[x][y + 1] == 0:
#             DFS(x, y + 1, 0)
        
#         if 0 <= x + 1 < n and 0 <= y + 1 < n and house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][y + 1] == 0:
#             DFS(x + 1, y + 1, 2)
#     elif direction == 1:
#         if 0 <= x + 1 < n and 0 <= y < n and house[x + 1][y] == 0:
#             DFS(x + 1, y, 1)
        
#         if 0 <= x + 1 < n and 0 <= y + 1 < n and house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][y + 1] == 0:
#             DFS(x + 1, y + 1, 2)
#     elif direction == 2:
#         if 0 <= x < n and 0 <= y + 1 < n and house[x][y + 1] == 0:
#             DFS(x, y + 1, 0)

#         if 0 <= x + 1 < n and 0 <= y < n and house[x + 1][y] == 0:
#             DFS(x + 1, y, 1)

#         if 0 <= x + 1 < n and 0 <= y + 1 < n and house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][y + 1] == 0:
#             DFS(x + 1, y + 1, 2)

# n = int(input())
# house = [list(map(int, input().split())) for _ in range(n)]

# cnt = 0
# DFS(0, 1, 0)
# print(cnt)

# 3
# BFS: python은 시간 초과로 인해 불가능
# import sys
# from collections import deque
# input = sys.stdin.readline

# def BFS(x, y, direction):
#     global cnt
#     queue = deque()
#     queue.append((x, y, direction))

#     while queue:
#         x, y, direction = queue.popleft()

#         if x == n - 1 and y == n - 1:
#             cnt += 1
#             continue
    
#         if direction == 0:
#             if 0 <= x < n and 0 <= y + 1 < n and house[x][y + 1] == 0:
#                 queue.append((x, y + 1, 0))
        
#             if 0 <= x + 1 < n and 0 <= y + 1 < n and house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][y + 1] == 0:
#                 queue.append((x + 1, y + 1, 2))
#         elif direction == 1:
#             if 0 <= x + 1 < n and 0 <= y < n and house[x + 1][y] == 0:
#                 queue.append((x + 1, y, 1))
        
#             if 0 <= x + 1 < n and 0 <= y + 1 < n and house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][y + 1] == 0:
#                 queue.append((x + 1, y + 1, 2))
#         elif direction == 2:
#             if 0 <= x < n and 0 <= y + 1 < n and house[x][y + 1] == 0:
#                 queue.append((x, y + 1, 0))

#             if 0 <= x + 1 < n and 0 <= y < n and house[x + 1][y] == 0:
#                 queue.append((x + 1, y, 1))

#             if 0 <= x + 1 < n and 0 <= y + 1 < n and house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][y + 1] == 0:
#                 queue.append((x + 1, y + 1, 2))

# n = int(input())
# house = [list(map(int, input().split())) for _ in range(n)]

# cnt = 0
# BFS(0, 1, 0)
# print(cnt)



# 4
# 참고~
import sys
input = sys.stdin.readline

def dfs(r, c, d):
    count = 0
    
    if (r, c, d) in cache:
        return cache[(r, c, d)]
    
    if r == n - 1 and c == n - 1:
        return 1

    if d == 0:
        direction = directions[0]
    elif d == 1:
        direction = directions[1]
    else:
        direction = directions[2]
    
    for i in range(len(direction)):
        dr, dc = direction[i]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < n and 0 <= nc < n):
            continue

        if a[nr][nc] == 1:
            continue

        if dr == 1 and dc == 1:
            if a[nr - 1][nc] == 1 or a[nr][nc - 1] == 1:
                continue
        
        if dr == 0 and dc == 1:
            count += dfs(nr, nc, 0)
        elif dr == 1 and dc == 0:
            count += dfs(nr, nc, 1)
        else:
            count += dfs(nr, nc, 2)

    cache[(r, c, d)] = count

    return count

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
directions = [[(0, 1), (1, 1)], [(1, 0), (1, 1)], [(0, 1), (1, 1), (1, 0)]]
cache = {}

print(dfs(0, 1, 0))