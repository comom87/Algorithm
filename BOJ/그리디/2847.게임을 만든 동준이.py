import sys
input = sys.stdin.readline

n = int(input())
score = [int(input()) for _ in range(n)]
score.reverse()
cnt = 0
for i in range(n - 1):
    if score[i] <= score[i + 1]:
        temp = score[i + 1] - score[i] + 1
        score[i + 1] -= temp
        cnt += temp
print(cnt)