# 분배 법칙 사용
import sys
input = sys.stdin.readline

brackets = input().rstrip()
stack = []
answer = 0
temp = 1
for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append(brackets[i])
        temp *= 2
    elif brackets[i] == '[':
        stack.append(brackets[i])
        temp *= 3
    elif brackets[i] == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        if brackets[i - 1] == '(':
            answer += temp
        stack.pop()
        temp //= 2
    elif brackets[i] == ']':
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if brackets[i - 1] == '[':
            answer += temp
        stack.pop()
        temp //= 3
    
if stack:
    print(0)
else:
    print(answer)