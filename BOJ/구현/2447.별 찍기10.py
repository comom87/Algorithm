import sys
input = sys.stdin.readline

def draw_stars(n):
    if n == 1:
        return ['*']
    
    stars = draw_stars(n // 3)
    pattern = []

    for star in stars:
        pattern.append(star * 3)
    for star in stars:
        pattern.append(star + ' ' * (n //3) + star)
    for star in stars:
        pattern.append(star * 3)
    
    return pattern

n = int(input())
result = draw_stars(n)
print('\n'.join(result))