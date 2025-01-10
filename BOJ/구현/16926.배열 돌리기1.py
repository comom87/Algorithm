# 1
import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range(min(n, m) // 2):
    queue = deque()
    queue.extend([matrix[j][i] for j in range(i, n - i - 1)])
    queue.extend(matrix[n - i - 1][i:m - i - 1])
    queue.extend([matrix[j][m - i - 1] for j in range(n - i - 1, i, -1)])
    queue.extend(matrix[i][m - i - 1:i:-1])

    cnt = r % len(queue)

    queue.rotate(cnt)

    for j in range(i, n - i - 1):
        matrix[j][i] = queue.popleft()
    for j in range(i, m - i - 1):
        matrix[n - i - 1][j] = queue.popleft()
    for j in range(n - i - 1, i, -1):
        matrix[j][m - i - 1] = queue.popleft()
    for j in range(m - i - 1, i, -1):
        matrix[i][j] = queue.popleft()

for row in matrix:
    print(*row)



# 2
# 시간 초과
# import sys
# input = sys.stdin.readline

# n, m, r = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# for i in range(min(n, m) // 2):
#     for _ in range(r):
#         temp = matrix[i][i]
#         for j in range(i, m - i - 1):
#             matrix[i][j] = matrix[i][j + 1]
#         for j in range(i, n - i - 1):
#             matrix[j][m - i - 1] = matrix[j + 1][m - i - 1]
#         for j in range(m - i - 1, i, -1):
#             matrix[n - i - 1][j] = matrix[n - i - 1][j - 1]
#         for j in range(n - i - 1, i, - 1):
#             matrix[j][i] = matrix[j - 1][i]
#         matrix[i + 1][i] = temp

# for row in matrix:
#     print(*row)