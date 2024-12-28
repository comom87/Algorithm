import sys
input = sys.stdin.readline

k = int(input())
for i in range(k):
    n, *math_scores = map(int, input().split())
    math_scores.sort(reverse=True)
    gaps = [math_scores[i] - math_scores[i + 1] for i in range(n - 1)]
    print(f'Class {i + 1}')
    print(f'Max {math_scores[0]} Min {math_scores[-1]} Largest gap {max(gaps)}')