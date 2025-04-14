import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()
for _ in range(n):
    command = input().split()
    if command[0] == '1':
        dq.appendleft(command[1])
    elif command[0] == '2':
        dq.append(command[1])
    elif command[0] == '3':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif command[0] == '4':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif command[0] == '5':
        print(len(dq))
    elif command[0] == '6':
        if dq:
            print(0)
        else:
            print(1)
    elif command[0] == '7':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif command[0] == '8':
        if dq:
            print(dq[-1])
        else:
            print(-1)