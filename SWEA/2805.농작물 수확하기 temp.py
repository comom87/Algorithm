# 1
t = int(input())
for test_case in range(t):
    n = int(input())
    farm = [list(map(int, input().rstrip())) for _ in range(n)]

    mid = n // 2
    profit = 0
    for j in range(mid):
        for k in range(mid - j, mid + j + 1):
            profit += farm[j][k]
            profit += farm[n - j - 1][k]
    profit += sum(farm[mid])
    print(f'#{test_case + 1} {profit}')

# 2
t = int(input())
for test_case in range(t):
    n = int(input())
    farm = [list(map(int, input().rstrip())) for _ in range(n)]

    mid = n // 2
    profit = 0
    for j in range(mid):
        for k in range(mid - j, mid + j + 1):
            profit += farm[j][k]
            profit += farm[n - j - 1][k]
    profit += sum(farm[mid])
    print(f'#{test_case + 1} {profit}')