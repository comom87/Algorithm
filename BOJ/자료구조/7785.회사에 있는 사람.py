import sys
input = sys.stdin.readline

n = int(input())
people = set()
for _ in range(n):
    name, history = input().split()
    if history == 'enter':
        people.add(name)
    elif history == 'leave':
        people.remove(name)
people = list(people)
people.sort(reverse=True)
for person in people:
    print(person)