# 아무리 고민해도 어떻게 풀어야할지 감이 안 잡혀서 블로그를 참고했다...!
# 힌트는 DFS
# 'ㅗ'자 모양을 제외한 다른 모양들은 DFS를 통해 풀 수 있는데 'ㅗ자 모양은 어떻게 풀어야 할지 모르겠어서 유튜브 참고
# 참고: https://www.youtube.com/watch?v=6RMKLbGGRNg

import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(depth, tetromino_sum, positions):
    global max_tetromino

    # 가지치기
    # 현재까지 정사각형이 놓인 칸에 쓰인 수들의 합과 남은 칸에 쓰인 수들이 graph의 최대값일 때의 합이 max_tetromino보다 작은 경우
    if tetromino_sum + (4 - depth) * max_num < max_tetromino:
        return

    if depth == 4:
        max_tetromino = max(max_tetromino, tetromino_sum)
        return

    for x, y in positions:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                DFS(depth + 1, tetromino_sum + graph[nx][ny], positions + [(nx, ny)])
                visited[nx][ny] = False


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
max_num = max(map(max, graph))
max_tetromino = 0

for x in range(n):
    for y in range(m):
        visited[x][y] = True
        DFS(1, graph[x][y], [(x, y)])
        visited[x][y] = False

print(max_tetromino)