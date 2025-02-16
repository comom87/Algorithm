import sys
input = sys.stdin.readline

cipher = ['0'] + list(input().rstrip())
n = len(cipher)
dp = [0] * 50001
dp[0] = 1
if cipher[1] != '0':
    dp[1] = 1

for i in range(2, n):
    if cipher[i] != '0':
        dp[i] += dp[i - 1]
    if cipher[i - 1] != '0' and int(cipher[i - 1] + cipher[i]) <= 26:
        dp[i] += dp[i - 2]
    dp[i] %= 1000000
print(dp[n - 1])