submissions = [False] * 30
for _ in range(28):
    n = int(input())
    submissions[n - 1] = True

for i in range(30):
    if not submissions[i]:
        print(i + 1)