x = list(map(int, input().rstrip()))
cnt = 0
while len(x) > 1:
    x = list(map(int, str(sum(x))))
    cnt += 1
print(cnt)
if sum(x) % 3 == 0:
    print('YES')
else:
    print('NO')