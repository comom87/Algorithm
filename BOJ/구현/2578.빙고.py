def is_bingo():
    line = 0

    # 가로
    for x in range(5):
        space = 0
        for y in range(5):
            if visited[x][y]:
                space += 1
        
        if space == 5:
            line += 1
    
    # 세로
    for y in range(5):
        space = 0
        for x in range(5):
            if visited[x][y]:
                space += 1
        
        if space == 5:
            line += 1
    
    # 대각선
    space = 0
    for i in range(5):
        if visited[i][i]:
            space += 1
    
    if space == 5:
        line += 1

    space = 0
    for i in range(5):
        if visited[i][4 - i]:
            space += 1
    
    if space == 5:
        line += 1
    
    if line >= 3:
        return True
    return False

board = [list(map(int, input().split())) for _ in range(5)]
nums = []
for _ in range(5):
    nums += list(map(int, input().split()))
visited = [[False for _ in range(5)] for _ in range(5)]

for i in range(25):
    for x in range(5):
        for y in range(5):
            if board[x][y] == nums[i]:
                visited[x][y] = True

                if is_bingo():
                    print(i + 1)
                    exit()