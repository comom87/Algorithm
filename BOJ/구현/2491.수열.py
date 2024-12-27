import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

sorted_dp = [1] * n
for i in range(n - 1):
    if num[i + 1] >= num[i]:
        sorted_dp[i + 1] = sorted_dp[i] + 1

reversed_dp = [1] * n
for i in range(n - 1, 0, -1):
    if num[i - 1] >= num[i]:
        reversed_dp[i - 1] = reversed_dp[i] + 1

print(max(max(sorted_dp), max(reversed_dp)))