n = int(input())
front_people= list(map(int, input().split()))

line = [0] * n
for height, front_person in enumerate(front_people, start=1):
    cnt = 0
    for i in range(n):
        if line[i] == 0 and cnt == front_person:
            line[i] = height
            break
        # 키가 작은 사람부터 위치가 정해지므로 현재 순서인 사람의 앞에 위치한 사람은 항상 현재 순서인 사람보다 키가 작다.
        # 따라서, line[i] > height인 경우는 고려하지 않아도 된다.
        elif line[i] == 0 and cnt < front_person:
            cnt += 1
print(*line)