import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
_, *knwon_people = map(int, input().split())
for known_person in knwon_people:
    parent[known_person] = 0
party_people = []
for _ in range(m):
    present_cnt, *present_people = map(int, input().split())
    party_people.append(present_people)
    for i in range(present_cnt - 1):
        union(present_people[i], present_people[i + 1])

cnt = 0
for present_people in party_people:
    flag = True
    for present_person in present_people:
        if find(present_person) == 0:
            flag= False
            break
    
    if flag:
        cnt += 1
print(cnt)