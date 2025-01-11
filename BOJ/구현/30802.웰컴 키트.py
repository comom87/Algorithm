n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
shirt_cnt = 0
for s in size:
    if s % t == 0:
        shirt_cnt += s // t
    else:
        shirt_cnt += s // t + 1
print(shirt_cnt)
print(n // p, n % p)