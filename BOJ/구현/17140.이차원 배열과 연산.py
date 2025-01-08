import sys
from collections import defaultdict
input = sys.stdin.readline

def sort_matrix(matrix, operation):
    new_matrix = []

    max_length = 0
    for i in range(len(matrix)):
        num_cnt = defaultdict(int)
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                continue

            num_cnt[matrix[i][j]] += 1
    
        num_cnt = sorted(num_cnt.items(), key=lambda x: (x[1], x[0]))
        line = list(sum(num_cnt, ()))
        max_length = max(max_length, len(line))
        new_matrix.append(line)

    for i in range(len(new_matrix)):
        new_matrix[i] += [0] * (max_length - len(new_matrix[i]))

        if len(new_matrix[i]) > 100:
            new_matrix[i] = new_matrix[i][:100]
    
    if operation == 'R':
        return new_matrix
    elif operation == 'C':
        return list(zip(*new_matrix))

r, c, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(3)]
time = -1
for t in range(101):
    if r - 1 < len(matrix) and c - 1 < len(matrix[0]) and matrix[r - 1][c - 1] == k:
        time = t
        break
    if len(matrix) >= len(matrix[0]):
        matrix = sort_matrix(matrix, 'R')
    else:
        matrix = sort_matrix(list(zip(*matrix)), 'C')
print(time)