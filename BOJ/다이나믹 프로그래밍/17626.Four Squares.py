n = int(input())
dp = [1e9] * (n + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, n + 1):
    num = int(i ** 0.5)
    if num ** 2 == i:
        dp[i] = 1
        continue

    for j in range(1, num + 1):
        dp[i] = min(dp[i], dp[i - j ** 2] + 1)
print(dp[n])