# BFS로 풀었지만 DFS로도 가능할 것 같다..!
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS():
    queue = deque()
    queue.append(red + blue + [1])
    visited.append(tuple(red + blue))

    while queue:
        rx, ry, bx, by, cnt = queue.popleft()

        if cnt > 10:
            break

        for i in range(4):
            nrx, nry, rdist = rx, ry, 0
            while True:
                nrx += dx[i]
                nry += dy[i]
                rdist += 1
                if board[nrx][nry] == '#':
                    nrx -= dx[i]
                    nry -= dy[i]
                    rdist -= 1
                    break
                elif board[nrx][nry] == 'O':
                    break
            
            nbx, nby, bdist = bx, by, 0
            while True:
                nbx += dx[i]
                nby += dy[i]
                bdist += 1
                if board[nbx][nby] == '#':
                    nbx -= dx[i]
                    nby -= dy[i]
                    bdist -= 1
                    break
                elif board[nbx][nby] == 'O':
                    break
            
            # 파란 구슬이 구멍에 빠진 경우
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬이 구멍에 빠진 경우
            if board[nrx][nry] == 'O':
                print(cnt)
                return
            
            # 빨간 구슬과 파란 구슬이 같은 위치인 경우
            if nrx == nbx and nry == nby:
                # 더 먼 거리를 이동한 구슬이 1칸 뒤에 있는 구슬
                if rdist > bdist:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            
            if (nrx, nry, nbx, nby) not in visited:
                queue.append((nrx, nry, nbx, nby, cnt + 1))
                visited.append((nrx, nry, nbx, nby))
    print(-1)

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = []
for x in range(n):
    for y in range(m):
        if board[x][y] == 'R':
            red = [x, y]
            board[x][y] = '.'
        elif board[x][y] == 'B':
            blue = [x, y]
            board[x][y] = '.'
BFS()