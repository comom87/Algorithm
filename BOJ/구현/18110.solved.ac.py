import sys
input = sys.stdin.readline

def round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())
if n == 0:
    print(0)
else:
    level = [int(input()) for _ in range(n)]
    level.sort()
    trimmed_cnt = int(round(n * 0.15))
    level = level[trimmed_cnt:n - trimmed_cnt]
    print(int(round(sum(level) / (n - 2 * trimmed_cnt))))