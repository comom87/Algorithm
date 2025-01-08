import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
classroom = [[0 for _ in range(n)] for _ in range(n)]
students = {}
for _ in range(n * n):
    student, *like_student = map(int, input().split())
    students[student] = like_student

    candidate_seat = []
    for x in range(n):
        for y in range(n):
            if classroom[x][y] == 0:
                like = 0
                empty = 0

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    if classroom[nx][ny] in like_student:
                        like += 1
                    
                    if classroom[nx][ny] == 0:
                        empty += 1
                
                candidate_seat.append([x, y, like, empty])
    
    candidate_seat.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    classroom[candidate_seat[0][0]][candidate_seat[0][1]] = student

satisfaction = 0
for x in range(n):
    for y in range(n):
        like_cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if classroom[nx][ny] in students[classroom[x][y]]:
                like_cnt += 1
        
        if like_cnt > 0:
            satisfaction += 10 ** (like_cnt - 1)

print(satisfaction)