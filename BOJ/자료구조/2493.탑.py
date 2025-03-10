import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
stack = []
nums = [0] * n
for i in range(n):
    while stack:
        if stack[-1][1] >= towers[i]:
            nums[i] = stack[-1][0]
            break
        else:
            stack.pop()
    stack.append((i + 1, towers[i]))
print(' '.join(map(str, nums)))