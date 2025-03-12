import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    word = input().rstrip()
    stack = []
    for letter in word:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    
    if not stack:
        cnt += 1
print(cnt)