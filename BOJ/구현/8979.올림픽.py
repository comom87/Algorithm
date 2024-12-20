import sys
input = sys.stdin.readline

n, k = map(int, input().split())
national_medals = [list(map(int, input().split())) for _ in range(n)]
national_medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
for i in range(n):
    if national_medals[i][0] == k:
        index = i
for i in range(n):
    if national_medals[i][1:] == national_medals[index][1:]:
        print(i + 1)
        break