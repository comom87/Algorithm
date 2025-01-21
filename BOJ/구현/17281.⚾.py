import sys
input = sys.stdin.readline

def line_up(depth):
    if depth == 9:
        lineups.append(arr[:])
        return

    if depth == 3:
        line_up(depth + 1)

    for i in range(1, 9):
        if not visited[i]:
            visited[i] = True
            arr[depth] = i
            line_up(depth + 1)
            arr[depth] = 0
            visited[i] = False


n = int(input())
inning = [list(map(int, input().split())) for _ in range(n)]

lineups = []
arr = [0] * 9
visited = [False] * 9
line_up(0)

base = [False] * 3
max_score = 0
for lineup in lineups:
    order = 0
    score = 0
    for i in range(n):
        out = 0
        while out < 3:
            if inning[i][lineup[order]] == 0:
                out += 1
                order = (order + 1) % 9
                continue

            for k in range(3):
                if base[k]:
                    if k + inning[i][lineup[order]] > 2:
                        base[k] = False
                        score += 1
                    else:
                        base[k] = False
                        base[k + inning[i][lineup[order]]] = True

            if inning[i][lineup[order]] == 4:
                score += 1
            else:
                base[inning[i][lineup[order]] - 1] = True
            order = (order + 1) % 9
    
    max_score = max(max_score, score)
print(max_score)




# 1. 타자의 순서를 정한다.
# 2. 각 이닝에 대해 점수를 계산하다가 3아웃이 발생하면 다음 이닝으로 넘어간다.
# 3. 각 타자의 순서에서 최댓값으 구한다.