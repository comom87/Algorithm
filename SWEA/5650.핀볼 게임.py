'''
    SWEA 5650. 핀볼 게임
    메모리: 66,432KB
    시간: 5,705ms
'''

'''
    아이디어
    - 핀볼은 현재 방향을 유지하면서 계속 직진
    - 핀볼은 블록의 수평면이나 수직면을 만날 경우 방향을 바꿔 반대로 돌아오고, 경사면을 만날 경우에는 직각으로 진행 방향이 꺾임
    - 핀볼은 벽을 만난 경우에도 반대 방향으로 돌아옴
    - 핀볼이 웜홀에 빠지면 동일한 숫자를 가진 다른 반대편 웜홀로 빠져나오게 되며 진행방향은 그대로 유지
    - 핀볼이 출발 위치로 돌아오거나, 블랙홀에 빠질 때 게임 종료
    - 점수는 벽이나 블록에 부딪힌 횟수
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# blocks: 핀볼이 1~5의 블록을 만날 때 바뀌는 진행 방향
blocks = {
    1: [2, 3, 1, 0],
    2: [1, 3, 0, 2],
    3: [3, 2, 0, 1],
    4: [2, 0, 3, 1],
    5: [2, 3, 0, 1]
}

t = int(input())    # t: 테스트 케이스의 수
for test_case in range(t):
    n = int(input())    # n: 게임판의 크기
    board = [list(map(int, input().split())) for _ in range(n)] # 게임판의 모양
    wormholes = {}  # wormholdes: 웜홀의 위치

    for x in range(n):
        for y in range(n):
            if 6 <= board[x][y] <= 10:  # 현재 위치의 숫자가 6~10인 경우 = 즉, 현재 위치가 웜홀이라면
                if board[x][y] not in wormholes:
                    wormholes[board[x][y]] = []
                wormholes[board[x][y]].append((x, y))   # 웜홀의 위치

    max_score = 0   # max_score: 점수의 최댓값
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:    # 현재 위치가 빈 공간인 경우 = 핀볼의 출발 위치
                for d in range(4):  # 핀볼의 진행 방향
                    nx, ny = x, y
                    score = 0
                    while True:
                        nx += dx[d]
                        ny += dy[d]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 핀볼이 벽을 만난 경우
                            d = blocks[5][d]    # 진행 방향이 반대 방향으로 바뀜
                            score += 1
                            continue

                        if 1 <= board[nx][ny] <= 5: # 핀볼이 블록을 만난 경우
                            d = blocks[board[nx][ny]][d]    # 블록의 종류에 현재 진행 방향에 따라서 진행 방향이 바뀜
                            score += 1
                        elif 6 <= board[nx][ny] <= 10:  # 핀볼이 웜홀에 빠진 경우
                            for i in range(2):
                                if (nx, ny) != wormholes[board[nx][ny]][i]:
                                    nx, ny = wormholes[board[nx][ny]][i]    # 동일한 숫자를 가진 다른 반대편 웜홀로 빠져나옴
                                    break
                        elif (nx == x and ny == y) or board[nx][ny] == -1:  # 핀볼이 출발 위치로 돌아오거나 블랙홀에 빠진 경우
                            break   # 게임 종료
                    
                    max_score = max(max_score, score)

    print(f'#{test_case + 1} {max_score}')