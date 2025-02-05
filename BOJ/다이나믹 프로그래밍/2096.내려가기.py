import sys
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
max_dp = graph
min_dp = graph
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    max_dp = [max(max_dp[0], max_dp[1]) + a, max(max_dp) + b, max(max_dp[1], max_dp[2]) + c]
    min_dp = [min(min_dp[0], min_dp[1]) + a, min(min_dp) + b, min(min_dp[1], min_dp[2]) + c]
print(max(max_dp), min(min_dp))