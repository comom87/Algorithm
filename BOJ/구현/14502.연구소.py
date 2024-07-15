import sys
from collections import deque
import copy
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def makeWall(count):
    if count == 3:
        spreadVirus()
        return

    for x in range(n):
        for y in range(m):
            if laboratory[x][y] == 0:
                laboratory[x][y] = 1
                makeWall(count + 1)
                laboratory[x][y] = 0

def spreadVirus():
    global result

    queue = deque()
    tempLaboratory = copy.deepcopy(laboratory)

    for x in range(n):
        for y in range(m):
            if tempLaboratory[x][y] == 2:
                queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if tempLaboratory[nx][ny] == 0:
                tempLaboratory[nx][ny] = 2
                queue.append((nx, ny))
    
    safetyArea = 0
    for x in range(n):
        for y in range(m):
            if tempLaboratory[x][y] == 0:
                safetyArea += 1
    
    result = max(result, safetyArea)

n, m = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(n)]
result = 0

makeWall(0)
print(result)