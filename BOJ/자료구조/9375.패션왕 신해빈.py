import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = defaultdict(list)
    for _ in range(n):
        name, kind = input().split()
        clothes[kind].append(name)
    
    cnt = 1
    for value in clothes.values():
        cnt *= len(value) + 1
    cnt -= 1
    print(cnt)