import sys
input = sys.stdin.readline

n = int(input())
people = []
for _ in range(n):
    weight, height = map(int, input().split())
    people.append((weight, height))

# 본인보다 덩치가 큰 사람만 생각
for person1 in people:
    rank = 1
    w1, h1 = person1
    for person2 in people:
        w2, h2 = person2
        if w2 > w1 and h2 > h1:
            rank += 1
    print(rank, end=' ')