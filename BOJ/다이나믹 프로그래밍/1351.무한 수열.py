def progression(n, p, q):
    if n in dp:
        return dp[n]
    dp[n] = progression(n // p, p, q) + progression(n // q, p, q)
    return dp[n]

n, p, q = map(int, input().split())
dp = {}
dp[0] = 1
progression(n, p, q)
print(dp[n])