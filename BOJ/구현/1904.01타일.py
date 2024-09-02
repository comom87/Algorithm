n = int(input())
dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
for i in range(3, 1000001):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
print(dp[n])

# n = 1일 때, 1개 -> 1
# n = 2일 때, 2개 -> 00, 11
# n = 3일 때, 3개 -> 001, 100, 111
# n = 4일 때, 5개 -> 0000, 0011, 1001, 1100, 1111
# n = 5일 때, 8개 -> 00001, 00100, 00111, 10000, 10011, 11001, 11100, 11111