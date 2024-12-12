import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

prefix_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for x in range(1, n + 1):
    for y in range(1, m + 1):
        prefix_sum[x][y] = nums[x - 1][y - 1] + prefix_sum[x - 1][y] + prefix_sum[x][y - 1] - prefix_sum[x - 1][y - 1]


k = int(input())
for _ in range(k):
    start_x, start_y, end_x, end_y = map(int, input().split())
    print(prefix_sum[end_x][end_y] - prefix_sum[start_x - 1][end_y] - prefix_sum[end_x][start_y - 1] + prefix_sum[start_x - 1][start_y -1])