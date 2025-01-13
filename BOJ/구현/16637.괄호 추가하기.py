# DFS
import sys
input = sys.stdin.readline

def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    
def DFS(index, value):
    global answer

    if index == n - 1:
        answer = max(answer, value)
        return
    
    # 다음 수와 다다음 수가 괄호로 묶여 있지 않은 경우 = 순서대로 연산하는 경우
    # 예시: a + b * c
    if index + 2 < n:
        DFS(index + 2, calculate(value, expression[index + 1], int(expression[index + 2])))
    
    # 다음 수와 다다음 수가 괄호로 묶여 있는 경우
    # 예시: a + (b * c)
    if index + 4 < n:
        DFS(index + 4, calculate(value, expression[index + 1], calculate(int(expression[index + 2]), expression[index + 3], int(expression[index + 4]))))


n = int(input())
expression = input().rstrip()

answer = -1e10
DFS(0, int(expression[0]))
print(answer)