import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pocketmons1 = {}
pocketmons2 = {}
for i in range(n):
    pocketmon = input().rstrip()
    pocketmons1[i + 1] = pocketmon
    pocketmons2[pocketmon] = i + 1
for _ in range(m):
    question = input().rstrip()
    if question.isalpha():
        print(pocketmons2[question])
    else:
        print(pocketmons1[int(question)])