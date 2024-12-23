import sys
input = sys.stdin.readline

n = int(input())
students = [list(input().split()) for _ in range(n)]
students.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])), reverse=True)
print(students[0][0])
print(students[-1][0])