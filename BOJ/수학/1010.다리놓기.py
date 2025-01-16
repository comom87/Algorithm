import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cnt = math.comb(m, n)
    print(cnt)