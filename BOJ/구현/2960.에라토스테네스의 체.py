n, k = map(int, input().split())

sieve = [True] * (n + 1)
sieve[0] = False
sieve[1] = False

for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if sieve[j]:
            sieve[j] = False
            k -= 1

        if k == 0:
            print(j)
            exit(0)