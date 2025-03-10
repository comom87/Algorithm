import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo = {}
for _ in range(n):
    address, password = input().split()
    memo[address] = password
for _ in range(m):
    address = input().rstrip()
    print(memo[address])