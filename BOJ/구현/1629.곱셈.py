def modular_arithmetic(a, b, c):
    if b == 1:
        return a % c
    
    temp = modular_arithmetic(a, b // 2, c)
    if b % 2 == 0:
        return (temp * temp) % c
    else:
        return (temp * temp * a) % c

a, b, c = map(int, input().split())
answer = modular_arithmetic(a, b, c)
print(answer)