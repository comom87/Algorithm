while True:
    n = int(input())
    factors = set()
    
    if n == -1:
        break

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    
    factors = list(factors)
    factors.sort()
    if sum(factors[:-1]) == n:
        print(f'{n} = {' + '.join(map(str, factors[:-1]))}')
    else:
        print(f'{n} is NOT perfect.')