# 1
# import sys
# from itertools import permutations
# input = sys.stdin.readline

# n, m, k = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# rotation = [list(map(int, input().split())) for _ in range(k)]
# min_row_sum = 1e9
# for p in permutations(rotation):
#     temp_matrix = [[matrix[i][j] for j in range(m)] for i in range(n)]
#     for r, c, s in p:
#         for i in range(s):
#             temp = temp_matrix[r - s + i - 1][c - s + i - 1]
#             for j in range(r - s + i - 1, r + s - i - 1):
#                 temp_matrix[j][c - s + i - 1] = temp_matrix[j + 1][c - s + i - 1]
#             for j in range(c - s + i - 1, c + s - i - 1):
#                 temp_matrix[r + s - i - 1][j] = temp_matrix[r + s - i - 1][j + 1]
#             for j in range(r + s - i - 1, r - s + i - 1, -1):
#                 temp_matrix[j][c + s - i - 1] = temp_matrix[j - 1][c + s - i - 1]
#             for j in range(c + s - i - 1, c - s + i - 1, -1):
#                 temp_matrix[r - s + i - 1][j] = temp_matrix[r - s + i - 1][j - 1]
#             temp_matrix[r - s + i - 1][c - s + i] = temp
#     min_row_sum = min(min_row_sum, min(sum(row) for row in temp_matrix))
# print(min_row_sum)


# 2
import sys
from itertools import permutations
input = sys.stdin.readline

n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
rotation = [list(map(int, input().split())) for _ in range(k)]
min_row_sum = 1e9
for p in permutations(rotation):
    temp_matrix = [[matrix[i][j] for j in range(m)] for i in range(n)]
    for r, c, s in p:
        for i in range(s, 0, -1):
            sr, sc = r - i - 1, c - i - 1
            er, ec = r + i - 1, c + i - 1

            temp = temp_matrix[sr][sc]
            for j in range(sr, er):
                temp_matrix[j][sc] = temp_matrix[j + 1][sc]
            temp_matrix[er][sc:ec] = temp_matrix[er][sc + 1:ec + 1]
            for j in range(er, sr, -1):
                temp_matrix[j][ec] = temp_matrix[j - 1][ec]
            temp_matrix[sr][sc + 1:ec + 1] = temp_matrix[sr][sc:ec]
            temp_matrix[sr][sc + 1] = temp
    min_row_sum = min(min_row_sum, min(sum(row) for row in temp_matrix))
print(min_row_sum)