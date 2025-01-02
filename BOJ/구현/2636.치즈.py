import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def BFS():
    queue = deque()
    contact = deque()
    queue.append((0, 0))
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny]:
                if cheeze[nx][ny] == 0:
                    queue.append((nx, ny))
                elif cheeze[nx][ny] == 1:
                    contact.append((nx, ny))
                visited[nx][ny] = True
    return contact, len(contact)

n, m = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(n)]
hour = 0

while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    total = sum(sum(c) for c in cheeze)
    
    contact, cnt = BFS()

    for x, y in contact:
        cheeze[x][y] = 0
    
    hour += 1
    total -= cnt
    if total == 0:
        print(hour)
        print(cnt)
        break