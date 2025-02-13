# 1
import sys
from collections import deque
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

n, m, t = map(int, input().split())
circle = [deque(list(map(int, input().split()))) for _ in range(n)]
for _ in range(t):
    x, d, k = map(int, input().split())
    for i in range(n):
        if (i + 1) % x == 0:
            if d == 0:
                circle[i].rotate(k)
            elif d == 1:
                circle[i].rotate(-k)
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    is_adjacent = False
    for i in range(n):
        for j in range(m):
            if circle[i][j] != 0:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                num = circle[i][j]
                circle[i][j] = 0
                adjacent_cnt = 0

                while queue:
                    now_i, now_j = queue.popleft()

                    for d in range(4):
                        next_i = now_i + di[d]
                        next_j = (now_j + dj[d]) % m

                        if next_i < 0 or next_i >= n:
                            continue

                        if circle[next_i][next_j] == num and not visited[next_i][next_j]:
                            is_adjacent = True
                            queue.append((next_i, next_j))
                            visited[next_i][next_j] = True
                            circle[next_i][next_j] = 0
                            adjacent_cnt += 1
                
                if adjacent_cnt == 0:
                    circle[i][j] = num

    if not is_adjacent:
        num_sum = 0
        num_cnt = 0
        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    num_sum += circle[i][j]
                    num_cnt += 1
        
        average = 0
        if num_cnt > 0:
            average = num_sum / num_cnt

        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    if circle[i][j] > average:
                        circle[i][j] -= 1
                    elif circle[i][j] < average:
                        circle[i][j] += 1

answer = 0
for i in range(n):
    for j in range(m):
        answer += circle[i][j]
print(answer)



# 2
import sys
from collections import deque
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

n, m, t = map(int, input().split())
circle = [deque(list(map(int, input().split()))) for _ in range(n)]
for _ in range(t):
    x, d, k = map(int, input().split())
    for i in range(n):
        if (i + 1) % x == 0:
            if d == 0:
                circle[i].rotate(k)
            elif d == 1:
                circle[i].rotate(-k)
    
    is_adjacent = False
    for i in range(n):
        for j in range(m):
            if circle[i][j] == 0:
                continue
            num = circle[i][j]
            queue = deque()
            queue.append((i, j))

            while queue:
                now_i, now_j = queue.popleft()

                for d in range(4):
                    next_i = now_i + di[d]
                    next_j = (now_j + dj[d]) % m

                    if next_i < 0 or next_i >= n:
                        continue

                    if circle[next_i][next_j] == num:
                        is_adjacent = True
                        queue.append((next_i, next_j))
                        circle[now_i][now_j] = 0
                        circle[next_i][next_j] = 0

    if not is_adjacent:
        num_sum = 0
        num_cnt = 0
        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    num_sum += circle[i][j]
                    num_cnt += 1
        
        average = 0
        if num_cnt > 0:
            average = num_sum / num_cnt

        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    if circle[i][j] > average:
                        circle[i][j] -= 1
                    elif circle[i][j] < average:
                        circle[i][j] += 1

answer = 0
for i in range(n):
    for j in range(m):
        answer += circle[i][j]
print(answer)



# 3
import sys
from collections import deque
input = sys.stdin.readline

n, m, t = map(int, input().split())
circle = [deque(list(map(int, input().split()))) for _ in range(n)]
for _ in range(t):
    x, d, k = map(int, input().split())
    for i in range(n):
        if (i + 1) % x == 0:
            if d == 0:
                circle[i].rotate(k)
            elif d == 1:
                circle[i].rotate(-k)

    remove_num = set()
    for i in range(n):
        for j in range(m):
            if circle[i][j] != 0 and circle[i][j] == circle[i][(j + 1) % m]:
                remove_num.add((i, j))
                remove_num.add((i, (j + 1) % m))
    for j in range(m):
        for i in range(n - 1):
            if circle[i][j] != 0 and circle[i][j] == circle[i + 1][j]:
                remove_num.add((i, j))
                remove_num.add((i + 1, j))

    for i, j in remove_num:
        circle[i][j] = 0
    
    if not remove_num:
        num_sum = 0
        num_cnt = 0
        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    num_sum += circle[i][j]
                    num_cnt += 1
        
        average = 0
        if num_cnt > 0:
            average = num_sum / num_cnt

        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    if circle[i][j] > average:
                        circle[i][j] -= 1
                    elif circle[i][j] < average:
                        circle[i][j] += 1

answer = 0
for i in range(n):
    for j in range(m):
        answer += circle[i][j]
print(answer)