t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n < m:
        n, m = m, n
        a, b = b, a
    
    max_sum = -1e9
    for i in range(n - m + 1):
        mutiplication_sum = 0

        for j in range(m):
            mutiplication_sum += a[i + j] * b[j]

        max_sum = max(max_sum, mutiplication_sum)
    
    print(f'#{test_case + 1} {max_sum}')