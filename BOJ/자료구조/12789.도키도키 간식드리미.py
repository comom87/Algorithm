import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
stack = []
i = 1
for num in nums:
    stack.append(num)
    while stack and stack[-1] == i:
        stack.pop()
        i += 1

if stack:
    print('Sad')
else:
    print('Nice')