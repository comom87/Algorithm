import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
dna = [input().rstrip() for _ in range(n)]
min_distance_dna = ''
min_distance = 0
for i in range(m):
    nucleotide = defaultdict(int)
    for d in dna:
        nucleotide[d[i]] += 1
    nucleotide = sorted(nucleotide.items(), key=lambda x: (-x[1], x[0]))
    min_distance_dna += nucleotide[0][0]
for d in dna:
    for i in range(m):
        if min_distance_dna[i] != d[i]:
            min_distance += 1
print(min_distance_dna)
print(min_distance)