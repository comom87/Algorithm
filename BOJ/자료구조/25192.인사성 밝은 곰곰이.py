import sys
input = sys.stdin.readline

n = int(input())
enter_people = set()
cnt = 0
for _ in range(n):
    person = input().rstrip()
    if person == 'ENTER':
        cnt += len(enter_people)
        enter_people = set()
    else:
        enter_people.add(person)
cnt += len(enter_people)
print(cnt)