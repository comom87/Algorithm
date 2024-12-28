n, new_score, p = map(int, input().split())

if n == 0:
    print(1)
    exit()

scores = list(map(int, input().split()))
scores.append(new_score)
scores.sort(reverse=True)

rank = -1
for i in range(p):
    if scores[i] == new_score:
        if len(scores) == p + 1 and scores[p - 1] == scores[p]:
            break
        rank = i + 1
        break
print(rank)