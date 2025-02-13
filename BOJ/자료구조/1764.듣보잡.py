import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listen = set([input().rstrip() for _ in range(n)])
see = set([input().rstrip() for _ in range(n)])
listensee = sorted(list(listen & see))
print(len(listensee))
for name in listensee:
    print(name)